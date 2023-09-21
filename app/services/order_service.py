from sqlalchemy.orm import Session
from models.order import OrderCreate, Order, OrderResponse
from utils.message_publisher import publish_created_order
from services.user_service import get_user
from services.product_service import get_product
from database import SessionLocal


async def create_order(order: OrderCreate) -> OrderResponse:
    # Get a database session
    db = SessionLocal()

    try:
        user_info = get_user(order.user_id)
        product_info = get_product(order.product_code)

        db_order = Order(
            user_id=order.user_id,
            product_code=order.product_code,
            customer_fullname=f"{user_info['firstName']} {user_info['lastName']}",
            product_name=product_info['name'],
            total_amount=product_info['price']
        )

        # Save the order and return the created order
        db.add(db_order)
        db.commit()

        created_order = OrderResponse(
            id=db_order.id,
            user_id=db_order.user_id,
            product_code=db_order.product_code,
            customer_fullname=db_order.customer_fullname,
            product_name=db_order.product_name,
            total_amount=db_order.total_amount
        )

        publish_created_order(created_order)
        return created_order
    finally:
        db.close()  # Close the database session
