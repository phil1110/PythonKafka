import datetime

class Item:
    def __init__(self, id, desc):
        self.id = id
        self.desc = desc
        pass
    
    def to_dict(self):
        return {
            "id" : str(self.id),
            "desc" : str(self.desc)
        }
    
    @staticmethod
    def from_dict(data: dict[str, any]) -> Item:
        return Item(
            id = data["id"],
            desc = data["desc"]
        )
        
class Order:    
    def __init__(self, id, items, time):
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