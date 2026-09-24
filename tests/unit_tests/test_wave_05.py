import pytest
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics
from swap_meet.item import Item

TEST_CUSTOM_ID = 12345

# ~~~~~ Clothing Tests ~~~~~


def test_clothing_has_default_uuid_length_id():
    clothing = Clothing()
    check_for_default_uuid_length_id(clothing)


def test_clothing_has_expected_category_and_custom_id():
    clothing = Clothing(id=TEST_CUSTOM_ID)
    check_category_and_custom_id(clothing, TEST_CUSTOM_ID, "Clothing")


def test_clothing_has_expected_default_to_str():
    clothing = Clothing(id=TEST_CUSTOM_ID)
    expected_str = (
        f"An object of type Clothing with id {TEST_CUSTOM_ID}. "
        "It is made from Unknown fabric."
    )
    assert str(clothing) == expected_str


def test_clothing_has_expected_to_str_with_custom_fabric():
    clothing = Clothing(id=TEST_CUSTOM_ID, fabric="Pinstriped")
    expected_str = (
        f"An object of type Clothing with id {TEST_CUSTOM_ID}. "
        "It is made from Pinstriped fabric."
    )
    assert str(clothing) == expected_str


# ~~~~~ Decor Tests ~~~~~


def test_decor_has_default_uuid_length_id():
    decor = Decor()
    check_for_default_uuid_length_id(decor)


def test_decor_has_expected_category_and_custom_id():
    decor = Decor(id=TEST_CUSTOM_ID)
    check_category_and_custom_id(decor, TEST_CUSTOM_ID, "Decor")


def test_decor_has_expected_default_to_str():
    decor = Decor(id=TEST_CUSTOM_ID)
    expected_str = (
        f"An object of type Decor with id {TEST_CUSTOM_ID}. "
        "It takes up a 0 by 0 sized space."
    )
    assert str(decor) == expected_str


def test_decor_has_expected_to_str_with_custom_size():
    decor = Decor(id=TEST_CUSTOM_ID, width=3, length=12)
    expected_str = (
        f"An object of type Decor with id {TEST_CUSTOM_ID}. "
        "It takes up a 3 by 12 sized space."
    )
    assert str(decor) == expected_str


# ~~~~~ Electronics Tests ~~~~~


def test_electronics_has_default_uuid_length_id():
    electronics = Electronics()
    check_for_default_uuid_length_id(electronics)


def test_electronics_has_expected_category_and_custom_id():
    electronics = Electronics(id=TEST_CUSTOM_ID)
    check_category_and_custom_id(electronics, TEST_CUSTOM_ID, "Electronics")


def test_electronics_has_expected_default_to_str():
    electronics = Electronics(id=TEST_CUSTOM_ID)
    expected_str = (
        f"An object of type Electronics with id {TEST_CUSTOM_ID}. "
        "This is a Unknown device."
    )
    assert str(electronics) == expected_str


def test_electronics_has_expected_to_str_with_custom_type():
    electronics = Electronics(id=TEST_CUSTOM_ID, type="Mobile Phone")
    expected_str = (
        f"An object of type Electronics with id {TEST_CUSTOM_ID}. "
        "This is a Mobile Phone device."
    )
    assert str(electronics) == expected_str


# ~~~~~ Item Tests ~~~~~


def test_items_have_condition_as_float():
    items = [Clothing(condition=3.5), Decor(condition=3.5), Electronics(condition=3.5)]
    for item in items:
        assert item.condition == pytest.approx(3.5)


def test_items_have_condition_descriptions_that_are_the_same_regardless_of_type():
    items = [Clothing(condition=5), Decor(condition=5), Electronics(condition=5)]
    five_condition_description = items[0].condition_description()
    assert isinstance(five_condition_description, str)
    for item in items:
        assert item.condition_description() == five_condition_description
    items[0].condition = 1
    one_condition_description = items[0].condition_description()
    assert isinstance(one_condition_description, str)
    for item in items:
        item.condition = 1
        assert item.condition_description() == one_condition_description

    assert one_condition_description != five_condition_description


# ~~~~~ Helper Functions ~~~~~


def check_for_default_uuid_length_id(to_check):
    assert isinstance(to_check.id, int)
    assert len(str(to_check.id)) >= 32


def check_category_and_custom_id(to_check, id, category):
    assert to_check.get_category() == category
    assert to_check.id == id

    # *********************************************************************
    # ****** Additional tests **********
    # *********************************************************************


def test_float_condition_uses_lower_description():
    items = [Clothing(condition=3.5)]
    result = items[0].condition_description()

    assert result == "Very Good"


def test_items_default_condition_is_zero():
    items = [Clothing()]
    result = items[0].condition

    assert result == 0


def test_condition_description_for_each_value_0_to_5():
    items = [
        Clothing(condition=0),
        Clothing(condition=1),
        Clothing(condition=2),
        Clothing(condition=3),
        Clothing(condition=4),
        Clothing(condition=5),
    ]

    assert items[0].condition_description() == "Poor"
    assert items[1].condition_description() == "Fair"
    assert items[2].condition_description() == "Good"
    assert items[3].condition_description() == "Very Good"
    assert items[4].condition_description() == "Excellent"
    assert items[5].condition_description() == "Brand New"


def test_subclasses_are_instances_of_item():
    items = [Clothing(), Decor(), Electronics()]

    for item in items:
        assert isinstance(item, Item)


def test_condition_description_out_of_range_returns_none():
    items = [Item(condition=6), Clothing(condition=-1), Decor(condition=-0.5)]

    for item in items:
        assert item.condition_description() is None
