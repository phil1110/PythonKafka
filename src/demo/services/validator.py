# 2) validator.py — Consumer → Producer (stream step)
# Consumes orders.incoming
# Validates schema + basic business rules
# On success → produce to orders.validated
# On failure → produce to orders.dlq (include reason + original payload)
# Implements:
# Manual commits
# At-least-once semantics
# Retry policy (small local retry loop) + DLQ after N tries

import asyncio, json
from confluent_kafka import Consumer, Producer
from demo.common import consumer_config, producer_config, Item, Order

def get_consumer() -> Consumer:
    conf = consumer_config
    
    conf["group.id"] = "validator"
    
    return Consumer(conf)



async def validate(json_msg: str) -> bool:
    try:
        order = Order.from_dict(json.loads(json_msg))
        
        if (order.id
            and order.items
            and order.time):
            return True
    except:
        print("VALIDATION ERROR")
    
    return False



async def produce(key, value, topic):
    with Producer(producer_config) as producer:
        producer.produce(topic=topic, value=value, key=key)
        


async def dlq_converter(value):
    order_dict = json.loads(value)
    
    dlq_dict = {
        "reason" : "Generic Validation Error",
        "order" : order_dict
    }
    
    return json.dumps(dlq_dict)



async def run_validator():
    running: bool = True
    
    with get_consumer() as consumer:
        consumer.subscribe(["orders.incoming"])
        print("SUBSCRIBED!")
        
        while True:
            print("WAITING ...")
            msg = consumer.poll(1)
            
            if msg is None: continue
            
            if msg.error():
                print("MSG ERROR")
            else:
                key = msg.key().decode("ASCII")
                value = msg.value().decode("ASCII")
                
                print("MSG CAUGHT: " + value)
                
                result = await validate(value)
                
                if result:
                    print("MSG " + key + " SENT TO VALIDATED")
                    await produce(key=key, value=value, topic="orders.validated")
                else:
                    print("MSG " + key + " SENT TO DLQ")
                    await produce(key=key, value=(await dlq_converter(value)), topic="orders.dlq")
                    
                consumer.commit(asynchronous=True)



asyncio.run(run_validator())