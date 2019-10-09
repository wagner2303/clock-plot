import math

def printPixel(a):
    for linha in a:
        for item in linha:
            print(item, end='')
        print('')

angle = lambda i, count: i * math.pi * 2 / count
x = lambda i, d, count, center: int(round(math.sin(angle(i, count)) * d, 0) + center)
y = lambda i, d, count, center: int(round(-1 * math.cos(angle(i, count)) * d) + center)

def markers(a, d = 16):
    center = int((len(a)-1)/2)
    for i in range(12):
        a[x(i, 16, 12, center)][y(i, 16, 12, center)] = 'O'
    a[center][center] = 'O'
    return a

def point(a, i, d, count):
    center = int((len(a)-1)/2)
    a[x(i, d, count, center)][y(i, d, count, center)] = str(int('0')+(i%5))
    return a

def hand(a, min, size):
    center = int((len(a)-1)/2)
    plotLine(a, center, center, x(min, size, 60, center), y(min, size, 60, center))

def plot(a, x, y):
    a[x][y] = 'X'

def plotLineLow(a, x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    yi = 1
    if dy < 0:
        yi = -1
        dy = -dy
    D = 2 * dy - dx
    y = y0
    for x in range(x0, x1):
        plot(a, x, y)
        if D > 0:
            y += yi
            D -= 2 * dx
        D += 2 * dy

def plotLineHigh(a, x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    xi = 1
    if dx < 0:
        xi = -1
        dx = -dx
    D = 2 * dx - dy
    x = x0
    for y in range(y0, y1):
        plot(a, x, y)
        if D > 0:
            x += xi
            D -= 2 * dy
        D += 2 * dx

def plotLine(a, x0, y0, x1, y1):
    if abs(y1 - y0) < abs(x1 - x0):
        if x0 > x1:
            plotLineLow(a, x1, y1, x0, y0)
        else:
            plotLineLow(a, x0, y0, x1, y1)
    else:
        if y0 > y1:
            plotLineHigh(a, x1, y1, x0, y0)
        else:
            plotLineHigh(a, x0, y0, x1, y1)

size = 32
a = [[' ' for j in range(size + 1)] for i in range(size + 1)]
a = markers(a)

hand(a, 40, 16)
hand(a, 3, 14)
hand(a, 25, 8)
printPixel(a)
