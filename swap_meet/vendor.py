class Vendor:
    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        try:
            self.inventory.remove(item)
        except ValueError:
            return None
        return item

    def get_by_id(self, item_id):
        for item in self.inventory:
            if item.id == item_id:
                return item
        return None