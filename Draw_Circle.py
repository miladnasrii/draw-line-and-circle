import matplotlib.pyplot as plt

def eightWaySymmetricPlot(x_center, y_center, x, y):
    plt.scatter(x+x_center, y+y_center, color="black", s=20)
    plt.scatter(x+x_center, -y+y_center,color="black", s=20)
    plt.scatter(-x+x_center, -y+y_center, color="black", s=20)
    plt.scatter(-x+x_center, y+y_center, color="black", s=20)
    plt.scatter(y+x_center, x+y_center, color="black", s=20)
    plt.scatter(y+x_center, -x+y_center, color="black", s=20)
    plt.scatter(-y+x_center, -x+y_center, color="black", s=20)
    plt.scatter(-y+x_center, x+y_center, color="black", s=20)

def draw_Circle(x_center, y_center, r):
    x = 0
    y = r
    d = 3 - 2 * r
    eightWaySymmetricPlot(x_center, y_center, x, y)
    while x <= y:
        if d <= 0:
            d = d + (4 * x) + 6
        else:
            d = d + (4 * x) - (4 * y) + 10
            y = y - 1
        x = x + 1
        eightWaySymmetricPlot(x_center, y_center, x, y)

plt.figure(figsize=(6, 6))

xc, yc = map(int, input("Enter x and y (for center) : ").split())
r = int(input("Enter the value of radius: "))

draw_Circle(xc, yc, r)

plt.show()