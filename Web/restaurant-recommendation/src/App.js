import React, { useState, useEffect } from "react";
import RecommendationBar from "./RecommendationBar";
import { Row, Col } from "reactstrap";
import Foods from "./Foods";
import Navi from "./Navi";
import Popularity from "./Popularity";
import { Switch, Route } from "react-router-dom";

function App() {
  const [foods, setFoods] = useState();
  const [categories, setCategories] = useState();
  const [cart, setCart] = useState([]);
  const [collabs, setCollabs] = useState([]);

  useEffect(() => {
    getFoods().then((data) => setFoods(data));
    getCategories().then((data) => setCategories(data));
  }, []);

  const getFoods = () =>
    fetch("http://192.168.1.185:5000/foods").then((res) => res.json());

  const getCategories = () =>
    fetch("http://192.168.1.185:5000/categories").then((res) => res.json());

  const setCartHandler = (newCart) => {
    if (cart.length !== newCart) {
      let foodNames;
      foodNames = (newCart.map((item) => getFoodNameById(item.id)) + ",")
        .toString()
        .slice(0, -1);
      setCollabsHandler({ foodNames });
    }

    setCart([...newCart]);
  };

  const getFoodNameById = (id) => {
    return foods && foods.find((food) => food.id === id).foodName;
  };

  const setCollabsHandler = (params) => {
    let url = new URL("http://192.168.1.185:5000/collaborative");
    url.search = new URLSearchParams(params).toString();

    return fetch(url)
      .then((res) => res.json())
      .then((data) => {
        if (data.success === false) {
          setCollabs([]);
        } else {
          setCollabs(data);
        }
      });
  };

  const getFoodById = (id) => {
    return foods.find((food) => food.id === id);
  };

  const getFoodByName = (name) => {
    return foods.find((food) => food.foodName === name);
  };

  return (
    <div
      className="App hide-scroll"
      style={{ background: "#24282c", minHeight: "100vh" }}
    >
      <Navi
        cart={cart}
        getFoodById={getFoodById}
        setCartHandler={setCartHandler}
      />

      <Switch>
        <Route path="/popularity" render={props => (
          <Popularity {...props} getFoodByName={getFoodByName} />
        )}></Route>
        <Route
          path="/"
          render={(props) => (
            <Row style={{ margin: "3vh", marginBottom: "0" }} {...props}>
              <Col xs="1" />
              <Col xs="8">
                <Foods
                  foods={foods}
                  categories={categories}
                  cart={cart}
                  setCartHandler={setCartHandler}
                />
              </Col>
              <Col xs="3">
                <RecommendationBar
                  collabs={collabs.length > 0 ? collabs : null}
                  getFoodByName={getFoodByName}
                  setCartHandler={setCartHandler}
                  cart={cart}
                />
              </Col>
            </Row>
          )}
        />
      </Switch>
    </div>
  );
}

export default App;
