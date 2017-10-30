import argparse

def format_price(price):
    try:
        if not isinstance(price, int) and not isinstance(price, float):
            price = float(price)
        return "{:,.2f}".format(round(price, 2)).replace('.00', '').replace(',', ' ')
    except (ValueError, TypeError):
        raise ValueError("Incoeect price format. Need integer or float")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Formatting prices.')
    parser.add_argument('price', type=float, help="Enter price for formatting")
    print(format_price(parser.parse_args().price))
