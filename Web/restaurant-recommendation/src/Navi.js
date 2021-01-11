import React from "react";
import {
  Navbar,
  NavbarBrand,
  Nav,
  NavItem,
  UncontrolledDropdown,
  DropdownToggle,
  DropdownMenu,
} from "reactstrap";

import { Link } from "react-router-dom";

import Cart from "./Cart";

export default function Navi(props) {
  return (
    <div>
      <Navbar dark color="dark" light expand="md">
        <NavbarBrand href="/">Ana Menü</NavbarBrand>
        <Nav className="ml-auto" navbar>
          <NavItem>
            <Link to="/popularity" className="nav-link">
              Sipariş Tahmini
            </Link>
          </NavItem>
            <UncontrolledDropdown nav inNavbar>
              <DropdownToggle nav caret>
                Sepet
              </DropdownToggle>
              <DropdownMenu right>
                <Cart
                  cart={props.cart}
                  getFoodById={props.getFoodById}
                  setCartHandler={props.setCartHandler}
                />
              </DropdownMenu>
            </UncontrolledDropdown>
        </Nav>
      </Navbar>
    </div>
  );
}
