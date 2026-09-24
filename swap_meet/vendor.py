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

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False

        self.remove(my_item)
        other_vendor.add(my_item)

        other_vendor.remove(their_item)
        self.add(their_item)

        return True

    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False

        my_first = self.inventory[0]
        their_first = other_vendor.inventory[0]

        return self.swap_items(other_vendor, my_first, their_first)

    def get_by_category(self, category):
        items = self.vendor_filter(lambda item: item.get_category() == category, self.inventory)

        return items
    
    def get_best_by_category(self, category):
        category_items = self.get_by_category(category)
        if not category_items:
            return None
        
        best_item = self.vendor_max(category_items, key=lambda item: item.condition)

        return best_item

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        best_item_for_them = self.get_best_by_category(their_priority)
        best_item_for_me = other_vendor.get_best_by_category(my_priority)

        return self.swap_items(other_vendor, best_item_for_them, best_item_for_me)

    def swap_by_newest(self, other_vendor):
        my_newest = self.vendor_max(self.inventory, key=lambda item: -item.age)
        their_newest = self.vendor_max(other_vendor.inventory, key=lambda item: -item.age)

        return self.swap_items(other_vendor, my_newest, their_newest)

    def vendor_filter(self, key, collection):
        if not collection :
            return None
        output = []
        for item in collection:
            if key(item):
                output.append(item)

        return output

    def vendor_max(self, collection, key):
        if not collection:
            return None
    
        cur_max = collection[0]
        max_val = key(cur_max)
        for item in collection:
            cur_val = key(item)

            if cur_val > max_val:
                cur_max = item
                max_val = cur_val
        
        return cur_max