import uuid

CONDITION_DESCRIPTION = ( "Poor", "Fair", "Good", "Very Good", "Excellent", "Brand New" )

class Item:
    def __init__(self, id=None, condition=0) -> None:
        self.id = uuid.uuid4().int if id is None else id
        self.condition = condition

    def get_category(self):
        return self.__class__.__name__

    def __str__(self):
        return f"An object of type Item with id {self.id}."
    
    def condition_description(self): 
        """Return the description corresponding to the item's condition."""
        return CONDITION_DESCRIPTION[self.condition]