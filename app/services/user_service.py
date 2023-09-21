import httpx
import asyncio
from fastapi import HTTPException
import os
import requests

def get_user(user_id: str):
    try:
        # async with httpx.AsyncClient() as client:
        print("complete user service url, ", f"{os.getenv('USER_SERVICE_URL')}/users/{user_id}")
        # response = await client.get(f"{os.getenv('PRODUCT_USER_SERVICE_URL')}/users/{user_id}", timeout=5.0)  # Adjust the timeout value as needed
        response = requests.get(f"{os.getenv('USER_SERVICE_URL')}/users/{user_id}")  # Adjust the timeout value as needed
        response.raise_for_status()
        print("inside user_service after getting response ", response)
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)
    except asyncio.TimeoutError:
        raise HTTPException(status_code=504, detail="Request to user service timed out")
    except httpx.TimeoutException:
        raise HTTPException(status_code=504, detail="Request to user service timed out")
    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail=f"Error connecting to user service: {str(e)}")
