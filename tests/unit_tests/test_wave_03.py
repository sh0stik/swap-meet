import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item

def test_item_overrides_to_string():
    test_id = 12345
    item = Item(id=test_id)

    item_as_string = str(item)

    expected_result = f"An object of type Item with id {test_id}."
    assert item_as_string == expected_result

def test_swap_items_returns_true():
    item_a = Item()
    item_b = Item()
    item_c = Item()
    fatimah = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Item()
    item_e = Item()
    jolie = Vendor(
        inventory=[item_d, item_e]
    )

    result = fatimah.swap_items(jolie, item_b, item_d)

    assert len(fatimah.inventory) == 3
    assert item_b not in fatimah.inventory
    assert item_a in fatimah.inventory
    assert item_c in fatimah.inventory
    assert item_d in fatimah.inventory
    assert len(jolie.inventory) == 2
    assert item_d not in jolie.inventory
    assert item_e in jolie.inventory
    assert item_b in jolie.inventory
    assert result

def test_swap_items_when_my_item_is_missing_returns_false():
    item_a = Item()
    item_b = Item()
    item_c = Item()
    fatimah = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Item()
    item_e = Item()
    jolie = Vendor(
        inventory=[item_d, item_e]
    )

    result = fatimah.swap_items(jolie, item_e, item_d)

    assert len(fatimah.inventory) == 3
    assert item_d not in fatimah.inventory
    assert item_a in fatimah.inventory
    assert item_b in fatimah.inventory
    assert item_c in fatimah.inventory
    assert len(jolie.inventory) == 2
    assert item_d in jolie.inventory
    assert item_e in jolie.inventory
    assert not result

def test_swap_items_when_their_item_is_missing_returns_false():
    item_a = Item()
    item_b = Item()
    item_c = Item()
    fatimah = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Item()
    item_e = Item()
    jolie = Vendor(
        inventory=[item_d, item_e]
    )

    result = fatimah.swap_items(jolie, item_b, item_c)

    assert len(fatimah.inventory) == 3
    assert item_d not in fatimah.inventory
    assert item_a in fatimah.inventory
    assert item_b in fatimah.inventory
    assert item_c in fatimah.inventory
    assert len(jolie.inventory) == 2
    assert item_d in jolie.inventory
    assert item_e in jolie.inventory
    assert not result

def test_swap_items_from_my_empty_returns_false():
    fatimah = Vendor(
        inventory=[]
    )

    item_d = Item()
    item_e = Item()
    jolie = Vendor(
        inventory=[item_d, item_e]
    )

    nobodys_item = Item()

    result = fatimah.swap_items(jolie, nobodys_item, item_d)

    assert len(fatimah.inventory) == 0
    assert len(jolie.inventory) == 2
    assert not result

def test_swap_items_from_their_empty_returns_false():
    item_a = Item()
    item_b = Item()
    item_c = Item()
    fatimah = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    jolie = Vendor(
        inventory=[]
    )

    nobodys_item = Item()

    result = fatimah.swap_items(jolie, item_b, nobodys_item)

    # raise Exception("Complete this test according to comments below.")
    # *********************************************************************
    # ****** Complete Assert Portion of this test **********
    # *********************************************************************

    assert len(fatimah.inventory) == 3
    assert item_a in fatimah.inventory
    assert item_b in fatimah.inventory
    assert item_c in fatimah.inventory
    
    assert len(jolie.inventory) == 0

    assert not result 

    # *********************************************************************
    # ****** Additional tests **********
    # *********************************************************************

def test_swap_items_both_missing_returns_false():
    fatimah = Vendor(
        inventory=[]
    )

    jolie = Vendor(
        inventory=[]
    )

    nobodys_item = Item()
    nobodys_item_2 = Item()

    result = fatimah.swap_items(jolie, nobodys_item, nobodys_item_2)

    assert len(fatimah.inventory) == 0
    assert len(jolie.inventory) == 0
    assert not result 

def test_swap_items_with_self():
    item_a = Item()
    item_b = Item()
    item_c = Item()
    fatimah = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    result = fatimah.swap_items(fatimah, item_a, item_b)

    assert not result
    

def test_swap_items_same_item_object_in_both_inventories():
    item_a = Item()
    item_b = Item()
    item_c = Item()
    fatimah = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Item()
    item_e = Item()
    jolie = Vendor(
        inventory=[item_a, item_d, item_e]
    )

    result = fatimah.swap_items(jolie, item_a, item_a)
    assert not result
    assert item_a in fatimah.inventory
    assert item_a in jolie.inventory
    assert len(fatimah.inventory) == 3
    assert len(jolie.inventory) == 3