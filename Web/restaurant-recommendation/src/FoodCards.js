import React from "react";
import FoodCard from "./FoodCard";

const FoodCards = (props) => {
    
  
    return (
    <div style={{ display: "flex", justifyContent: "left", flexWrap: "wrap" }}>
      {props.foods &&
        props.foods.map((food) => (
          <FoodCard
            key={food.id}
            data_key={food.id}
            food={food}
            cart={props.cart}
            setCartHandler={props.setCartHandler}
          />
        ))}
    </div>
  );
};

export default FoodCards;
