import re
import argparse

PATTERN_FLOAT_NUMBERS = r'^\d+\.?\d*$'

def format_price(price):
    str_price = str(price)
    if not re.search(PATTERN_FLOAT_NUMBERS, str_price):
        raise ValueError
    float_price = float(str_price)
    if float_price.is_integer():
        formatted_price = '{:,.0f}'.format(float_price).replace(',',' ')
    else:
        formatted_price = '{:,.2f}'.format(float_price).replace(',',' ')
    return formatted_price    


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
    	description='Convert price into clear view'
    )
    parser.add_argument(
    	'input',
    	help='price that converts in readable format'
    )
    args = parser.parse_args()
    print(format_price(args.input))