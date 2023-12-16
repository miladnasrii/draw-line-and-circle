from matplotlib import pyplot as plt

def draw_line(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    x = x0
    y = y0
    p = 2 * dy - dx
    while x < x1:
        if p >= 0:
            y = y + 1
            p = p + 2 * dy - 2 * dx
        else:
            p = p + 2 * dy
        x = x + 1

x0, y0 = map(int, input("Enter x0 and y0 : ").split())
x1, y1 = map(int, input("Enter x1 and y1 : ").split())

plt.plot([x0, x1], [y0, y1], marker = 'o')
draw_line(x0, y0, x1, y1)
plt.show()