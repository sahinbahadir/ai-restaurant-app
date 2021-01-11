import React from "react";
import { ListGroupItem, Button } from "reactstrap";

export default function Recommendation(props) { 
    const addItemsToCart = (evt) => {
    const foodId = Number(evt.target.parentElement.getAttribute('data-key'));
    const newCart = props.cart;

    newCart.push({
        id: foodId,
        quantity: 1
    });

    props.setCartHandler(newCart);
  };

  return (
    <div>
      <ListGroupItem
        data-key={props.foodDetails.id}
        style={{
          background: "#2e3439",
          borderRadius: "10px",
          display: "flex",
          alignItems: "center",
          justifyContent: "space-between",
        }}
      >
        <div>
          <img
            style={{ width: "50px", marginRight: "15px", borderRadius: "10px" }}
            src={"/images/" + props.foodDetails.imagePath}
            alt="coll-img"
          ></img>
          <span style={{ color: "whitesmoke" }}>
            {props.foodDetails.foodName}
          </span>
        </div>
        <Button color="success" onClick={addItemsToCart}>
          +
        </Button>
      </ListGroupItem>
    </div>
  );
}
