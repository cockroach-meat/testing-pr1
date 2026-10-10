from gilded_rose import Item, GildedRose

def update_item(name: str, quality: int, sell_in: int) -> Item:
    item = Item(name, sell_in, quality)

    shop = GildedRose([item])
    shop.update_quality()

    return item


def check_item(item: Item, quality: int, sell_in: int) -> bool:
    return item.quality == quality and item.sell_in == sell_in


def test_normal_item_with_positive_sell_in():
    item = update_item('Колбаса', 5, 5)
    assert check_item(item, 4, 4)


def test_normal_item_with_negative_sell_in():
    item = update_item('Колбаса', 5, -5)
    assert check_item(item, 3, -6)


def test_normal_item_with_sell_in_1():
    item = update_item('Колбаса', 5, 1)
    assert check_item(item, 4, 0)


def test_normal_item_with_sell_in_0():
    item = update_item('Колбаса', 5, 0)
    assert check_item(item, 3, -1)


def test_aged_brie_with_positive_sell_in():
    item = update_item('Aged Brie', 5, 5)
    assert check_item(item, 6, 4)


