import uuid

consumer_config = {
                'metadata.broker.list': '192.168.8.254:9092',
                'client.id': str(uuid.uuid4()),
                'auto.offset.reset': 'earliest'
        }

producer_config = {
                'metadata.broker.list': '192.168.8.254:9092',
                'client.id': str(uuid.uuid4())
        }