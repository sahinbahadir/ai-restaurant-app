import React from 'react'
import {ListGroup} from 'reactstrap';
import Recommendation from './Recommendation';

export default function RecommendationBar(props) {
    return (
        <div>
            <h3 style={{color:"whitesmoke"}}>Öneriler</h3>
            <ListGroup style={{borderRadius: "10px !important"}}>
                {
                    props.collabs && props.collabs.map(food => {
                        const foodDetails = props.getFoodByName(food[0])
                        return (
                            <Recommendation key={foodDetails.id} foodDetails={foodDetails} setCartHandler={props.setCartHandler} cart={props.cart} />
                        )
                    })
                }
            </ListGroup>
        </div>
    )
}
