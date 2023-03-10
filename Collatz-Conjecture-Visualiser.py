import matplotlib.pyplot as plt

for i in range(1, 61):
    x = i
    y = [x]
    while x != 1:
        if x%2 == 1:
            x = 3*x + 1
        else:
            x = x // 2
        y.append(x)
    y.append(1)
    plt.plot(y)

plt.show()