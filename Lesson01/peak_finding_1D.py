import matplotlib.pyplot as plt

if __name__ == '__main__':
    a = [1, 3, 5, 2, 6, 9]

    if a[0] >= a[1]:
        print("The Peak is ", a[0])
    for i in range(0, len(a) - 2):
        if a[i + 1] >= a[i]:
            if i + 1 == len(a) - 2:
                if a[i + 2] >= a[i + 1]:
                    print("The Peak is ", a[i + 2])
            elif a[i + 1] >= a[i + 2]:
                print("The Peak is ", a[i + 1])

    x = list(range(0, 6))
    y = list(a)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    fig.suptitle('Photo')
    plt.show()
