import pytest

from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics
from swap_meet.item import Item
from swap_meet.vendor import Vendor


def test_swap_by_newest():
    item_a = Decor(condition=2.0, age=1)
    item_b = Electronics(condition=4.0, age=2)
    item_c = Decor(condition=4.0, age=3)
    tai = Vendor(inventory=[item_a, item_b, item_c])

    item_d = Clothing(condition=2.0, age=0)
    item_e = Decor(condition=4.0, age=1)
    item_f = Clothing(condition=4.0, age=1)
    jesse = Vendor(inventory=[item_d, item_e, item_f])

    tai_inventory = [item_b, item_c, item_d]
    jesse_inventory = [item_e, item_f, item_a]

    result = tai.swap_by_newest(jesse)

    assert result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    for item in tai_inventory:
        assert item in tai.inventory
    for item in jesse_inventory:
        assert item in jesse.inventory


def test_swap_by_newest_same_ages_returns_false():

    item_a = Decor(condition=2.0, age=5)
    item_b = Electronics(condition=4.0, age=5)
    item_c = Decor(condition=4.0, age=5)
    tai = Vendor(inventory=[item_a, item_b, item_c])

    item_d = Clothing(condition=2.0, age=5)
    item_e = Decor(condition=4.0, age=5)
    item_f = Clothing(condition=4.0, age=5)
    jesse = Vendor(inventory=[item_d, item_e, item_f])

    result = tai.swap_by_newest(other_vendor=jesse)
    tai_inventory = [item_a, item_b, item_c]
    jesse_inventory = [item_d, item_e, item_f]

    assert not result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    for item in tai_inventory:
        assert item in tai.inventory
    for item in jesse_inventory:
        assert item in jesse.inventory


def test_items_default_age_is_zero():
    items = [Clothing()]
    result = items[0].age

    assert result == 0


def test_items_use_custom_age_if_passed():
    items = [Clothing(age=1)]
    result = items[0].age

    assert result == 1


def test_swap_by_newest_empty_inventory_returns_false():
    tai = Vendor(inventory=[])

    item_a = Clothing(condition=2.0, age=1)
    item_b = Decor(condition=4.0, age=3)
    jesse = Vendor(inventory=[item_a, item_b])

    result = tai.swap_by_newest(jesse)
    jesse_inventory = [item_a, item_b]

    assert not result
    assert len(tai.inventory) == 0
    assert len(jesse.inventory) == 2
    for item in jesse_inventory:
        assert item in jesse.inventory


def test_swap_by_newest_other_empty_inventory_returns_false():
    item_a = Clothing(condition=2.0, age=1)
    item_b = Decor(condition=4.0, age=3)
    tai = Vendor(inventory=[item_a, item_b])

    jesse = Vendor(inventory=[])

    result = tai.swap_by_newest(jesse)
    tai_inventory = [item_a, item_b]

    assert not result
    assert len(tai.inventory) == 2
    assert len(jesse.inventory) == 0
    for item in tai_inventory:
        assert item in tai.inventory


def test_swap_by_newest_one_vendor_same_ages_returns_false():
    item_a = Decor(condition=2.0, age=2)
    item_b = Decor(condition=4.0, age=2)
    tai = Vendor(inventory=[item_a, item_b])

    item_c = Clothing(condition=2.0, age=4)
    item_d = Clothing(condition=4.0, age=1)
    jesse = Vendor(inventory=[item_c, item_d])

    result = tai.swap_by_newest(jesse)
    tai_inventory = [item_a, item_b]
    jesse_inventory = [item_c, item_d]

    assert not result
    assert len(tai.inventory) == 2
    assert len(jesse.inventory) == 2
    for item in tai_inventory:
        assert item in tai.inventory
    for item in jesse_inventory:
        assert item in jesse.inventory


def test_swap_by_newest_picks_first_on_tie():
    item_a = Decor(condition=2.0, age=3)
    item_b = Decor(condition=4.0, age=1)
    item_c = Decor(condition=4.0, age=1)
    tai = Vendor(inventory=[item_a, item_b, item_c])

    item_d = Clothing(condition=2.0, age=2)
    item_e = Clothing(condition=4.0, age=5)
    jesse = Vendor(inventory=[item_d, item_e])

    result = tai.swap_by_newest(jesse)
    tai_inventory = [item_a, item_c, item_d]
    jesse_inventory = [item_e, item_b]

    assert result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 2
    for item in tai_inventory:
        assert item in tai.inventory
    for item in jesse_inventory:
        assert item in jesse.inventory
