def equation(a, b, c):
    D = b ** 2 - 4 * a * c
    x1 = (-b - D ** 0.5) / 2 * a
    x2 = (-b + D ** 0.5) / 2 * a
    return x1, x2

print('Корни уравнения: ', equation(4, 5, 1))
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
