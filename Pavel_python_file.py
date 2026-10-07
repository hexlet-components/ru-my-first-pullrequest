def print_check(honey_position: object) -> None:
    total = 0
    print()
    print('000 Медовый спас\n')

    for honey in honey_position:
        name = honey[0]
        amount = honey[1]
        price = honey[2]

        item_total = amount * price

        print(f'{name} ({amount} шт.) - {price} руб.')
        print(f'Сумма: {item_total:.2f}\n')
        print('-' * 30)

        total += item_total

    print('-' * 30)
    print(f'\nИтого: {total:.2f} руб.')
    print('-' * 22)
    print('Спасибо за покупку!')


def get_amount():
    while True:
        try:
            amount = int(input('Amount:'))

            if amount <= 0:
                print('Количество должно быть больше 0.')
                continue

            return amount

        except ValueError:
            print('Ошибка: введите целое число')


def get_price():
    while True:
        try:
            price = float(input('Price:'))

            if price <= 0:
                print('Цена должны быть больше 0')
                continue

            return price

        except ValueError:
            print('Ошибка: введите число. Например: 500 или 499.50')


honey_position = []

while True:
    name = input('Name (для завершения введите "enter"): ').strip()

    if name.lower() == "enter":
        break

    if not name:
        print('Ошибка: наименование товара не может быть пустым')
        continue

    amount = get_amount()
    price = get_price()

    honey_position.append((name, amount, price))

    print('Товар добавлен!')


if honey_position:
    print_check(honey_position)

else:
    print('Чек пуст, товары не добавлены!')