from fastapi import APIRouter, HTTPException
from models.order import OrderCreate, OrderResponse
from services.order_service import create_order

router = APIRouter()

@router.get("/")
async def hello():
    return {"message": "Hello, there! To run the orders service append /orders/ and with post call and required body"}

@router.post("/orders/", response_model=OrderResponse)  # Use OrderResponse as response_model
async def createOrder(order: OrderCreate):
    try:
        created_order = await create_order(order)  # Await the coroutine
        return created_order
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
