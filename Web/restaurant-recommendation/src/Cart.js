import React from "react";
import { Badge, DropdownItem } from "reactstrap";

export default function Cart(props) {
  const increaseQuantity = (evt) => {
    const productId = Number(
      evt.target.parentElement.parentElement.getAttribute("data-key")
    );
    const newCart = props.cart;
    let item = newCart.find((food) => food.id === productId);

    item.quantity += 1;

    props.setCartHandler(newCart);
    evt.preventDefault();
  };

  const decreaseQuantityOfProduct = (evt) => {
    const foodId = Number(
      evt.target.parentElement.parentElement.getAttribute("data-key")
    );
    let newCart = props.cart;
    const item = newCart.find((food) => food.id === foodId);

    if (item.quantity !== 1) {
      item.quantity--;
    } else {
      newCart = removeProductFromCart(newCart, item);
    }

    props.setCartHandler(newCart);
  };

  const removeProductFromCart = (cart, product) => {
    return cart.filter((food) => food.id !== product.id);
  };

  return (
    <div>
      {props.cart &&
        props.cart.map((item) => (
          <DropdownItem
            toggle={false}
            key={item.id}
            data-key={item.id}
            style={{
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
            }}
          >
            {props.getFoodById(item.id).foodName}
            <div className="ml-2">
              <Badge color="danger" onClick={decreaseQuantityOfProduct}>
                -
              </Badge>
              <Badge color="info">{item.quantity}</Badge>
              <Badge color="success" onClick={increaseQuantity}>
                +
              </Badge>
            </div>
          </DropdownItem>
        ))}
      <DropdownItem divider />
      <DropdownItem toggle={false} onClick={() => props.setCartHandler([])}>Sıfırla</DropdownItem>
    </div>
  );
}
