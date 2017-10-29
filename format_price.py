def format_price(price):
    try:
        if not isinstance(price, int) and not isinstance(price, float):
            price = float(price)
        return "{:,.2f}".format(price).rstrip('0').rstrip('.,').replace(',', ' ')
    except (ValueError, TypeError):
        return 'Incorrect value'


if __name__ == '__main__':
    while True:
        price = input('Input price for formatting: ')
        print(format_price(price))
