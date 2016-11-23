vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print([num for elem in vec for num in elem])

from math import pi

[str(round(pi, i)) for i in range(1, 6)]
