# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cadena = "R, R, R, R, R,\r\nR, C-a, C, C, R,\r\nR, C, C, C, R,\r\nR, R, R, C, R,\r\nR, M, C, C, R,\r\nR, C, C, C, R,\r\nR, R, R, R, R,"
    graph = {}
    # Eliminar los caracteres \r\n y dividir la cadena en una lista de strings
    lines = cadena.replace("\r\n", ".").split(".")

    list = [elemento.strip().split(', ') for elemento in lines]
    for i in range(len(list)):
        for j in range(len(list[i])):
            list[i][j] = list[i][j].replace(" ", "")
            list[i][j] = list[i][j].replace(",", "")
    for i in range(len(list)):
        for j in range(len(list[i])):
            graph[(i, j)] = list[i][j]

    print(graph)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
