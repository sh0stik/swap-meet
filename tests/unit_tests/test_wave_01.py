# The following line imports the Vendor class from the module vendor inside the swap_meet package.
import pytest
from swap_meet.vendor import Vendor


def test_vendor_has_inventory():
    vendor = Vendor()
    assert len(vendor.inventory) == 0


def test_vendor_takes_optional_inventory():
    inventory = ["a", "b", "c"]
    vendor = Vendor(inventory=inventory)
    assert len(vendor.inventory) == 3
    assert "a" in vendor.inventory
    assert "b" in vendor.inventory
    assert "c" in vendor.inventory


def test_adding_to_inventory():
    vendor = Vendor()
    item = "new item"

    result = vendor.add(item)

    assert len(vendor.inventory) == 1
    assert item in vendor.inventory
    assert result == item


def test_removing_from_inventory_returns_item():
    item = "item to remove"
    vendor = Vendor(
        inventory=["a", "b", "c", item]
    )

    result = vendor.remove(item)

    assert len(vendor.inventory) == 3
    assert item not in vendor.inventory
    assert result == item


def test_removing_not_found_is_none():
    item = "item to remove"
    vendor = Vendor(
        inventory=["a", "b", "c"]
    )

    result = vendor.remove(item)

    # *********************************************************************
    # ****** Complete Assert Portion of this test **********
    # *********************************************************************
    assert result is None

    # *********************************************************************
    # ****** Addidtional tests **********
    # *********************************************************************

# test_remove_from_empty_inventory_is_none
def test_vendor_default_inventories_are_not_shared():
    vendor_a = Vendor()
    vendor_b = Vendor()

    vendor_a.add("item")

    assert vendor_a.inventory is not vendor_b.inventory
    assert vendor_a.inventory == ["item"]
    assert vendor_b.inventory == []

def test_remove_duplicate_removes_only_one():
        item = "item to remove"
        vendor = Vendor(
            inventory=["a", "b", "c", item, item]
        )
    
        result = vendor.remove(item)
    
        assert result == item
        assert len(vendor.inventory) == 4
        assert item in vendor.inventory

def test_remove_from_empty_inventory_is_none():
    item = "item to remove"
    vendor = Vendor()

    result = vendor.remove(item)

    assert result is None