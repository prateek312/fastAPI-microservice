from sqlalchemy import Column, String, Float
from pydantic import BaseModel
from database import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid

class OrderCreate(BaseModel):
    user_id: str
    product_code: str

class Order(Base):
    __tablename__ = "orders"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(String, index=True)
    product_code = Column(String, index=True)
    customer_fullname = Column(String)
    product_name = Column(String)
    total_amount = Column(Float)
    
class OrderResponse(BaseModel):
    id: uuid.UUID
    user_id: str
    product_code: str
    customer_fullname: str
    product_name: str
    total_amount: float
