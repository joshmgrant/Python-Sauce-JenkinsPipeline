import pytest


def test_add_to_cart(driver):
    driver.get('https://localhost:3000/inventory.html')
    driver.find_element_by_class_name('btn_primary').click()

    assert driver.find_element_by_class_name('shopping_cart_badge').text == '1'

    driver.get('https://localhost:3000/cart.html')
    expected = driver.find_elements_by_class_name('inventory_item_name')
    assert len(expected) == 1

def test_add_two_to_cart(driver):
    driver.get('https://localhost:3000/inventory.html')
    driver.find_element_by_class_name('btn_primary').click()
    driver.find_element_by_class_name('btn_primary').click()

    assert driver.find_element_by_class_name('shopping_cart_badge').text == '2'

    driver.get('https://localhost:3000/cart.html')
    expected = driver.find_elements_by_class_name('inventory_item_name')
    assert len(expected) == 2
