import uuid, datetime, random, json
from order.items import Item, items

class Order:    
    def __init__(self, id = str(uuid.uuid4()), items="", time = datetime.datetime.now()):
        self.id = id
        self.items = items
        self.time = time
        pass
    
    def to_dict(self):        
        return {
            "id" : self.id,
            "items" : [item.to_dict() for item in self.items],
            "time" : str(self.time)
        }
    
    @staticmethod
    def from_dict(data: dict[str, any]) -> Order:
        return Order(
            id = dict["id"],
            items = [Item.from_dict(item) for item in data["items"]],
            time = datetime.datetime.strptime(str(data["time"]), "%Y-%m-%d %H:%M:%S.%f")
        )
    
def create_order():
    order_items = []
    item_amount = random.randint(0,3)
    
    for i in range(0, item_amount):
        item = items[i]
        order_items.append(items[i])
    
    return Order(items=order_items)