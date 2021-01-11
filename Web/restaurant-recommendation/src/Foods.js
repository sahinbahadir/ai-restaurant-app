import React from "react";
import FoodCards from "./FoodCards";
import { UncontrolledCollapse, Button } from "reactstrap";

export default function Foods(props) {
  const addCategory = (category) => {
    return (
      <div key={category.id}>
        <Button
          color="success"
          id={"cat-" + category.id}
          style={{ marginBottom: "1em", width: "95%", textAlign: "center" }}
        >
          {category.categoryName}
        </Button>
        <UncontrolledCollapse toggler={"#cat-" + category.id}>
          <FoodCards
            foods={
              props.foods &&
              props.foods.filter((food) => food.categoryId === category.id)
            }
            cart={props.cart}
            setCartHandler={props.setCartHandler}
          />
        </UncontrolledCollapse>
      </div>
    );
  };

  return (
    <div className="mt-5">
      {props.categories &&
        props.categories.map((category) => addCategory(category))}
    </div>
  );
}
