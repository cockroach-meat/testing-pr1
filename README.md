# Практическая работа 1

## Бизнес-правила

1. Товары имеют качество (`quality`) и крайний срок реализации (`sell_in`)
2. `quality` не может быть больше 50
3. Для обычных товаров, если `sell_in > 0`, каждый день `quality` уменьшается на 1
4. Для обычных товаров, если `sell_in <= 0`, каждый день `quality` уменьшается на 2
5. Для товара "Aged Brie" каждый день `quality` увеличивается на 1
6. Для товара "Backstage passes" каждый день `quality` увеличивается на 1 при `sell_in > 10`, на 2 при `sell_in <= 10` и на 3 при `sell_in <= 5`
7. Для товара "Backstage passes" `quality = 0` при `sell_in <= 0`
8. Для товара "Sulfuras" `quality` не меняется

| Правило | Начальное состояние                                    | После одного обновления ожидается | Почему выбраны данные                        | Имя теста/результат |
| ------- | ------------------------------------------------------ | --------------------------------- | -------------------------------------------- | ------------------- |
| BR3     | `name = "Колбаса", quality = 5, sell_in = 5`           | `quality = 4, sell_in = 4`        | Представитель класса "до истечения срока"    | `test_normal_item_with_positive_sell_in`, успех                    |
| BR4     | `name = "Колбаса", quality = 5, sell_in = -5`          | `quality = 3, sell_in = -6`       | Представитель класса "после истечения срока" |  `test_normal_item_with_negative_sell_in`, успех                    |
| BR3     | `name = "Колбаса", quality = 5, sell_in = 1`           | `quality = 4, sell_in = 0`        | Граничный случай: нижняя граница срока       |  `test_normal_item_with_sell_in_1`, успех                    |
| BR4     | `name = "Колбаса", quality = 5, sell_in = 0`           | `quality = 3, sell_in = -1`       | Граничный случай: нижняя граница срока       |   `test_normal_item_with_sell_in_0`, успех                   |
| BR5     | `name = "Aged Brie", quality = 5, sell_in = 5`         | `quality = 6, sell_in = 4`        | Специальный товар                            |   `test_aged_brie_with_positive_sell_in`, успех                   |
| BR5     | `name = "Aged Brie", quality = 5, sell_in = -5`        | `quality = 6, sell_in = -6`       | Специальный товар                            |                     |
| BR2     | `name = "Aged Brie", quality = 49, sell_in = 5`        | `quality = 50, sell_in = 4`       | Граничный случай: верхняя граница качества   |                     |
| BR2     | `name = "Aged Brie", quality = 50, sell_in = 5`        | `quality = 50, sell_in = 4`       | Граничный случай: верхняя граница качества   |                     |
| BR6     | `name = "Backstage passes", quality = 5, sell_in = 11` | `quality = 6, sell_in = 10`       | Граничный случай: перед переходом            |                     |
| BR6     | `name = "Backstage passes", quality = 5, sell_in = 10` | `quality = 7, sell_in = 9`        | Граничный случай: после перехода             |                     |
| BR6     | `name = "Backstage passes", quality = 5, sell_in = 6`  | `quality = 7, sell_in = 5`        | Граничный случай: перед переходом            |                     |
| BR6     | `name = "Backstage passes", quality = 5, sell_in = 5`  | `quality = 8, sell_in = 4`        | Граничный случай: после перехода             |                     |
| BR7     | `name = "Backstage passes", quality = 5, sell_in = 1`  | `quality = 8, sell_in = 0`        | Граничный случай: перед обнулением           |                     |
| BR7     | `name = "Backstage passes", quality = 5, sell_in = 0`  | `quality = 0, sell_in = -1`       | Граничный случай: после обнуления            |                     |
| BR8     | `name = "Sulfuras", quality = 5, sell_in = 5`          | `quality = 5, sell_in = 4`        | Специальный товар                            |                     |
