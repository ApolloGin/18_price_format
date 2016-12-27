# 18_price_format

## Synopsis

Script help to convert input price in human readable format

## Quick start

Script has two interfaces.

First - programm interface
 - Import module format_price.py and use format_price(price) function.
 - Input: price which will be formatted
 - Output: string with formatted number. If input is incorrect that function raises ValueError exception

Second - comand-line interface
 - run format_price.py with one parameter, that represents price. For example: `python3.5 format_price.py 3245.000000`
 - Input: parameter must be number
 - Output: string with formatted number, otherwise exception.

## Tests

Module format_price.py has some test cases. If you plan to use this module in projects first of all run test.py for check. (`python3.5 tests.py`) Every tests must be completed.