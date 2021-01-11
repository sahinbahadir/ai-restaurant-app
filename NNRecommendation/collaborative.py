# %tensorflow_version 2.x
import tensorflow as tf

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import Dense, Flatten, Concatenate, Dropout, Embedding, Input
from tensorflow.keras.models import Model, load_model
from tensorflow.keras.callbacks import EarlyStopping
import matplotlib.pyplot as plt

import os
import DBOperations as db

df = pd.read_csv('new_ratings.csv')

train, test = train_test_split(df, test_size=0.2, random_state=42)

n_customers = df.userId.max()
n_foods = df.foodId.max()
print(len(df.userId.unique()))

food_input = Input(shape=[1], name="FoodInput")
food_embed = Embedding(n_foods + 1, 5, name="FoodEmbed")(food_input)
food_vector = Flatten(name="FoodFlatten")(food_embed)

cust_input = Input(shape=[1], name="CustomerInput")
cust_embed = Embedding(n_customers + 1, 5, name="CustomerEmbed")(cust_input)
cust_vector = Flatten(name="CustomerFlatten")(cust_embed)

concat = Concatenate()([food_vector, cust_vector])
embed_drop = Dropout(0.02)(concat)

with tf.device('/cpu:0'):
  fc1 = Dense(128, activation="relu")(embed_drop)
  drop1 = Dropout(0.4)(fc1)
  fc2 = Dense(128, activation="relu")(drop1)
  drop2 = Dropout(0.4)(fc2)
  fc3 = Dense(32, activation="relu")(drop2)
  drop3 = Dropout(0.4)(fc3)
  out = Dense(1)(drop3)

  es = EarlyStopping('val_loss', mode="min", patience=10, verbose=1)
  model = Model([cust_input, food_input], out)
  model.compile('adam', 'mean_squared_error')

  if os.path.exists('latest1.h5'):
      model = load_model('latest1.h5')
  else:
      history = model.fit([train.userId, train.foodId], train.rating, epochs=100, verbose=1, validation_split=0.3, callbacks=[es]) # 111111111111 11111 1111111
      model.save('latest1.h5')
      plt.plot(history.history['val_loss'], label="Validation Loss")
      plt.xlabel("Epochs")
      plt.ylabel("Loss")

      plt.plot(history.history['loss'], label="Training Loss")
  plt.legend()
  plt.show()
  model.evaluate([test.userId, test.foodId], test.rating)
  foodData = np.array(list(set(df.foodId)))
  user = np.array([63 for i in range(len(foodData))])
  predictions = model.predict([user, foodData])
  predictions = np.array([a[0] for a in predictions])
  food_ids = (-predictions).argsort()[:10]

  eaten = (db.getEatenFoodsOfUser(63))
  new_foods = (db.getFoodsFromFoodIDs(food_ids))
  recomms = [food for food in new_foods if food not in eaten][:5]
  indexes =  [id_ for id_, food in enumerate(new_foods) if food not in eaten][:5]
  print(eaten)
  print()
  print(recomms)
  print(predictions[indexes])