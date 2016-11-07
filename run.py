import sys
from valib import create, display, solve

x = create('equations/00.txt')
display(x)
y = solve(x)
if y:
    print()
    display(y)
