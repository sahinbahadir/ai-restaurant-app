import React, { useState } from "react";
import { Row, Input, Button } from "reactstrap";
import moment from "moment";
import PopularityCard from "./PopularityCard";

export default function Popularity(props) {
  const [tmpTime, setTmpTime] = useState(moment());
  const [popularity, setPopularity] = useState([]);

  const getPopularity = () => {
    const url = new URL("http://192.168.1.185:5000/popularity");
    const params = { day: tmpTime.day(), hour: tmpTime.hours() };
    url.search = new URLSearchParams(params).toString();
    console.log(url.href);
    return fetch(url)
      .then((res) => res.json())
      .then((data) => setPopularity(data));
  };

  const changeTime = (val) => {
    const time = moment(tmpTime);
    time.add(val, "hours");
    setTmpTime(time);
  };

  const getShift = () => {
    return tmpTime.hour() + ":00 - " + (tmpTime.hour() + 1) + ":00";
  };

  const onChangeHandler = (value) => {
    setTmpTime(moment(value, "YYYY-MM-DDTkk:mm"));
  };

  return (
    <div>
      <Row
        style={{
          color: "whitesmoke",
          display: "flex",
          justifyContent: "center",
        }}
      >
        <div
          style={{
            color: "whitesmoke",
            border: "1px solid whitesmoke",
            padding: ".5rem",
            borderRadius: ".5rem",
            marginTop: "3vh",
          }}
        >
          <span>{getShift()}</span>
        </div>
      </Row>

      <Row
        style={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          marginTop: "3vh",
        }}
      >
        <Button
          color="danger"
          className="mr-3"
          onClick={() => changeTime(-1)}
          style={{ height: "6vh" }}
        >
          {"<<"}
        </Button>
        <div
          style={{
            color: "whitesmoke",
          }}
        >
          <Input
            type="datetime-local"
            name="date"
            id="date-input"
            value={tmpTime.format("YYYY-MM-DDTkk:mm")}
            style={{ backgroundColor: "whitesmoke", height: "6vh" }}
            onChange={(e) => onChangeHandler(e.target.value)}
          />
        </div>
        <Button
          color="success"
          className="ml-3"
          onClick={() => changeTime(1)}
          style={{ height: "6vh" }}
        >
          {">>"}
        </Button>
      </Row>
      <Row className="d-flex justify-content-center mt-3">
        <Button color="info" onClick={getPopularity}>
          Getir
        </Button>
      </Row>
      <div
        style={{
          display: "flex",
          flexWrap: "wrap",
          justifyContent: "left",
          marginTop: "5vh",
          marginLeft: "9vh",
        }}
      >
        {popularity &&
          popularity.map((item) => {
            const food = props.getFoodByName(item[1]);
            return (
              <PopularityCard
                key={food.id}
                data-key={food.id}
                food={food}
                score={item[0]}
              />
            );
          })}
      </div>
    </div>
  );
}
