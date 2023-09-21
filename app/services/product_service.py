# app/services/product_service.py

import httpx
import asyncio
from fastapi import HTTPException
import os
import requests

def get_product(product_code: str):
    try:
        print("priting product service url ", os.getenv('PRODUCT_SERVICE_URL'))
        # response = await client.get(f"http://product_service-1:8081/products/{product_code}", timeout=5.0)  # Adjust the timeout value as needed
        response = requests.get(f"{os.getenv('PRODUCT_SERVICE_URL')}/products/{product_code}")  # Adjust the timeout value as needed
        response.raise_for_status()
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)
    except asyncio.TimeoutError:
        raise HTTPException(status_code=504, detail="Request to product service timed out")
    except httpx.TimeoutException:
        raise HTTPException(status_code=504, detail="Request to product service timed out")
    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail=f"Error connecting to product service: {str(e)}")


