import pandas as pd
import datetime
import random

DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

MAIN_TYPES = ['kebaplar', 'izgaralar', 'durumler', 'pideler']

OTHER_TYPES = ['corbalar', 'baslangiclar', 'icecekler', 'tatlilar']
PROBABILITIES = [0.3, 0.3, 0.7, 0.4]

FOODS = {
    "corbalar": ["Süzme Mercimek Çorbası",
        "Tarhana Çorbası",
        "Domates Çorbası",
        "Tavuk Suyu Çorbası",
        "Yayla Çorbası"],

    "baslangiclar": ["Kuruluk Dolması", "Kızartma İçli Köfte (Adet)"],

    "kebaplar": [
        "Adana Kebap",
        "Urfa Kebap",
        "Sarma Beyti Kebabı",
        "Beyti Kebabı",
        "Domatesli Kebap",
        "Patlıcanlı Kebap",
        "Altı Ezmeli Kebap (Kıymadan)",
        "Altı Ezmeli Kebap (Şişten)",
        "Alinazik Kebap (Şişten)",
        "Alinazik Kebap (Kıymadan)",
        "Sac Kavurma",
        "Yoğurtlu Kebap",
        "Yoğurtlu Antep Kebabı",
        "Ali Haydar Kebabı",
        "Karışık Kebap",
    ],

    "izgaralar": [
        "Tavuk Pirzola",
        "Tavuk Kanat",
        "Tavuk Şiş",
        "Çöp Şiş",
        "Kuzu Şiş",
        "Izgara Köfte",
    ],

    "durumler": [
        "Adana Dürüm",
        "Urfa Dürüm",
        "Kuzu Şiş Dürüm",
        "Tavuk Şiş Dürüm",
        "Çöp Şiş Dürüm",
        "Ali Haydar Dürüm",
        "Şefin Dürümü (Spesiyal)",
    ],

    "pideler": [
        "Kaşarlı Pide",
        "Kıymalı Pide",
        "Kuşbaşılı Pide",
        "Kuşbaşılı Kaşarlı Pide",
        "Kavurmalı Pide",
        "Kaşarlı Sucuklu Pide",
        "Karışık Pide",
    ],

    "tatlilar": ["Fırın Sütlaç", "Baklava", "Kazandibi", "Fıstıklı Künefe"],

    "icecekler": [
        "Coca-Cola (33 cl.)",
        "Coca-Cola Şekersiz (33 cl.)",
        "Fanta (33 cl.)",
        "Sprite (33 cl.)",
        "Cappy (33 cl.)",
        "Şalgam Suyu (33 cl.)",
        "Ayran (30 cl.)",
        "Soda (20 cl.)",
    ],
}



def decision(probability):
    return random.random() < probability

def createChoices():
    choices = []
    for i in range(len(OTHER_TYPES)):
        if decision(PROBABILITIES[i]):
            choices.append(OTHER_TYPES[i])

    choices.append(random.sample(MAIN_TYPES, 1)[0])
    return choices

COLUMNS = ['Id', 'DateTime', 'Day', 'Category', 'MenuItem']

def generateOrders():
    sonnn_df = pd.DataFrame(columns=COLUMNS)
    current_date = datetime.datetime.strptime('14/09/2019 09:00', '%d/%m/%Y %H:%M')
    cust_id = 0

    while(current_date.strftime('%d/%m/%Y') != '14/03/2020'):
        cat_types = createChoices()
        selected_foods = list()

        for cat_type in cat_types:
            selected_foods.append([cat_type, random.sample(FOODS[cat_type], 1)])

        for food in selected_foods:
            sonnn_df = sonnn_df.append({'Id': cust_id, 'DateTime': current_date, 'Day': current_date.strftime('%A'),'Category': food[0], 'MenuItem': food[1][0]}, ignore_index = True)
        
        cust_id += 1
        current_date += datetime.timedelta(minutes=random.randint(1, 20))
        
        if(current_date.strftime('%H') == '23'):
            current_date += datetime.timedelta(days=1)
            current_date = current_date.replace(hour=9, minute=0)
    
    return sonnn_df
    

sonnnn_df = generateOrders()
sonnnn_df.to_csv('en_son.csv', encoding='utf-8', index=False)
