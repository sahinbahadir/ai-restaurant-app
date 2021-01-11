import React from 'react';
import { Card, CardImg, CardBody
, CardTitle, Button, Badge } from 'reactstrap';

const FoodCard = props => {

    const addFood = (food) => {
        let item = getItemById(food.id);
        let qty = item ? item.quantity: 0;
        return (
            <Card data-key={props.data_key} style={{width: "80%", marginBottom: "40px", background: "#2e3439"}}>
                <CardImg top src={'/images/' + food.imagePath} onError={imgNotFoundHandler}/>
                <CardBody style={{alignItems: "center", textAlign: "center"}}>
                    <CardTitle tag="h5" style={{color: "whitesmoke", height: "10vh"}}>{food.foodName}</CardTitle>
                    <div style={{display: 'flex', justifyContent:"space-around", alignItems: "center", marginTop: "10px"}}>
                        <Button color="danger" onClick={decreaseQuantityOfProduct}>-</Button>
                        <Badge color="info" style={{fontSize: "1em", padding: ".7em 20%"}}>{qty}</Badge>
                        <Button color="success" onClick={addProductToCart}>+</Button>
                    </div>
                </CardBody>
            </Card>

        );
    }

    const imgNotFoundHandler = (e) => {
        e.target.onerror = null;
        e.target.src = '/images/resized_822.jpeg';
    }

    const addProductToCart = (evt) => {
        const foodId = Number(evt.target.parentElement.parentElement.parentElement.getAttribute('data-key'));
        const newCart = props.cart;
        let item = newCart.find(food => food.id === foodId);

        if(item) {
            item.quantity++;
        }

        else {
            newCart.push({
                id: foodId,
                quantity: 1
            });
        }

        props.setCartHandler(newCart);
    }

    const decreaseQuantityOfProduct = (evt) => {
        const foodId = Number(evt.target.parentElement.parentElement.parentElement.getAttribute('data-key'));
        let newCart = props.cart;
        const item = newCart.find(food => food.id === foodId);

        if(item) {
            if(item.quantity !== 1) {
              item.quantity--;
            }
    
            else {
                newCart = removeProductFromCart(newCart, item);
            }
    
            props.setCartHandler(newCart);
          }
    
          return;
    }

    const removeProductFromCart = (cart, product) => {
        return cart.filter(food => food.id !== product.id);
    }

    const getItemById = id => {
        return props.cart.find(food => food.id === id);
    }
    
    return (
        <div>
            {addFood(props.food)}
        </div>
    );
};

export default FoodCard;