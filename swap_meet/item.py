import uuid

CONDITION_DESCRIPTION = ("Poor", "Fair", "Good", "Very Good", "Excellent", "Brand New")


class Item:
    def __init__(self, id=None, condition=0, age=0) -> None:
        self.id = uuid.uuid4().int if id is None else id
        self.condition = condition
        self.age = age

    def get_category(self):
        return self.__class__.__name__

    def __str__(self):
        return f"An object of type Item with id {self.id}."

    def condition_description(self):
        """Returns the description for the item's condition."""
        if self.condition < 0 or self.condition >= len(CONDITION_DESCRIPTION):
            return None
        return CONDITION_DESCRIPTION[int(self.condition)]
