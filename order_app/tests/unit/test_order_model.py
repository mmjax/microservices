import pytest
from uuid import uuid4
from pydantic import ValidationError
from app.models.order import Order, OrderStatuses


@pytest.fixture()
def any_cart_uuid():
    return uuid4()


def test_order_creation(any_cart_uuid):
    order_data = {
        "cart": str(any_cart_uuid),
        "status": OrderStatuses.DONE.value,
        "discount": 0.1,
        "price": 100.0,
    }

    order = Order(**order_data)

    assert order.cart == any_cart_uuid
    assert order.status == OrderStatuses.DONE
    assert order.discount == 0.1
    assert order.price == 100.0


# def test_order_default_values(any_cart_uuid):
#     order_data = {
#         "cart": str(any_cart_uuid),
#         "status": OrderStatuses.DONE,
#         "price": 100.0,
#     }

#     order = Order(**order_data)



def test_order_invalid_status(any_cart_uuid):
    order_data = {
        "cart": str(any_cart_uuid),
        "status": "invalid_status",
        "price": 100.0,
    }

    with pytest.raises(ValueError):
        Order(**order_data)


def test_order_invalid_discount(any_cart_uuid):
    order_data = {
        "cart": str(any_cart_uuid),
        "status": OrderStatuses.DONE,
        "discount": "invalid_discount",
        "price": 100.0,
    }

    with pytest.raises(ValueError):
        Order(**order_data)


def test_order_negative_price(any_cart_uuid):
    order_data = {
        "cart": str(any_cart_uuid),
        "status": OrderStatuses.DONE.value,
        "price": -100.0,
    }

    with pytest.raises(ValueError):
        Order(**order_data)