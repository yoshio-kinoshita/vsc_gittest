
from decimal import Decimal

name = "Fred"

print(f"He said his name is {name}")

width = 10
precision = 4
value = Decimal("12.34567")

print(f"Result:{value:{width}.{precision}}")