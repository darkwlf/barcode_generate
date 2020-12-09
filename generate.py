from barcode import Code39
from barcode.writer import ImageWriter
import random

price = input("Price:")
f = open(f'Barcode - {random.randint(1, 100000)}.png', 'ab+')
Code39(price, writer=ImageWriter()).write(f)
f.close()
