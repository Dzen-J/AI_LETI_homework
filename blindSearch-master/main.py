from tabulate import tabulate

from search_strategies import search


if __name__ == '__main__':
    repeat = 'Y'
    while repeat == 'Y':
        mode = input(tabulate(
                         [["1", "DFS"], ["2", "DLS"]],
                         headers=["№", "Стратегия"],
                         tablefmt="grid")
                     + '\n> ')

        match mode:
            case '1':
                debug_flag = input("\nРежим поэтапного вывода (Y/N):\n> ") == 'Y'
                table = list(map(int, input('\nВведите начальную таблицу, пробелами обозначая переход на новую строку или введите 0\n>').split(' ')))
                search(debug_flag, table=table)
            case '2':
                debug_flag = input("\nРежим поэтапного вывода (Y/N):\n> ") == 'Y'
                depth_limit = int(input("Введите ограничение на глубину:\n> "))
                table = list(map(int, input('\nВведите начальную таблицу, пробелами обозначая переход на новую строку или введите 0\n>').split(' ')))
                search(debug_flag, depth_limit=depth_limit)
            case _:
                print("Некорректный ввод")
        repeat = input("\nПерезапуск? (Y/N)\n > ")
