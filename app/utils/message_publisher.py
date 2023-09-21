# app/utils/message_publisher.py

import pika
import json
from datetime import datetime
from retry import retry


@retry(exceptions=Exception, tries=5, delay=2, backoff=2)
def publish_created_order(order):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host='localhost',
            credentials=pika.PlainCredentials(username='hellofresh', password='food')
        )
    )
    channel = connection.channel()

    exchange_name = 'orders'
    routing_key = 'created_order'
    message = {
        "producer": "order_service",
        "sent_at": datetime.now().isoformat(),
        "type": "order_created",
        "payload": {
            "order": {
                "order_id": order.id,
                "customer_fullname": order.customer_fullname,
                "product_name": order.product_name,
                "total_amount": order.total_amount
            }
        }
    }

    channel.basic_publish(
        exchange=exchange_name,
        routing_key=routing_key,
        body=json.dumps(message),
        properties=pika.BasicProperties(
            delivery_mode=2,  # Make the message persistent
        )
    )

    connection.close()
