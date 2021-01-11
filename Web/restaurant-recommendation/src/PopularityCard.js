import React from 'react'
import {Card, CardBody, CardImg, CardTitle, Badge} from 'reactstrap';

export default function PopularityCard(props) {
    return (
        <div>
            <Card data-key={props.data_key} style={{width: "80%", marginBottom: "40px", background: "#2e3439"}}>
                <CardImg top src={'/images/' + props.food.imagePath} />
                <CardBody style={{alignItems: "center", textAlign: "center"}}>
                    <CardTitle tag="h5" style={{color: "whitesmoke", height: "10vh"}}>{props.food.foodName}</CardTitle>
                    <div style={{display: 'flex', justifyContent:"space-around", alignItems: "center", marginTop: "10px"}}>
                        <Badge color="info" style={{fontSize: "1em", padding: ".7em 20%"}}>{'%' + props.score}</Badge>
                    </div>
                </CardBody>
            </Card>
        </div>
    )
}
