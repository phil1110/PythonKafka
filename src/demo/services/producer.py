import random, time, json, uuid
from datetime import datetime
from confluent_kafka import Producer, Message
from demo.common import producer_config, Item, Order

items = [
    Item(1, "T-Shirt"),
    Item(2, "Shoe"),
    Item(3, "Jeans")
]

@staticmethod
def create_order() -> Order:
    order_items = []
    item_amount = random.randint(0,3)
    
    for i in range(0, item_amount):
        item = items[i]
        order_items.append(items[i])
    
    return Order(str(uuid.uuid4()), order_items, datetime.now())

def acked(err, msg: Message):
    if err is None:
        print("MSG: " + str(msg.value()))
    else:
        print("!!!ERROR!!!\nERR MSG: " + str(err) + "\nMSG: " + str(msg.value()))

def run_producer():
    while True:
        orders = []
    
        for i in range(1, random.randint(2, 4)):
            time.sleep(0.01)
            orders.append(
                    create_order()
                    .to_dict())
            
        
        with Producer(producer_config) as producer:
            for order in orders:
                producer.produce(topic="orders.incoming", value=json.dumps(order), key=order["id"], callback=acked)
                producer.poll(0)
        
        time.sleep(1)
        


run_producer()