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
    
items = [
    Item(1, "T-Shirt"),
    Item(2, "Shoe"),
    Item(3, "Jeans")
]