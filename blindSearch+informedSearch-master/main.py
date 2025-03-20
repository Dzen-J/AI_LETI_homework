from tabulate import tabulate
from search_strategies import search, greedy_best_first_search, a_star_search
from basic_operations import get_initial_state, get_finish_state, h1, h2
from node import Node


if __name__ == '__main__':
    repeat = 'Y'
    while repeat == 'Y':
        mode = input(tabulate(
                         [["1", "DFS"], ["2", "DLS"], ["3", "Greedy h1"], ["4", "Greedy h2"], ["5", "A* h1"], ["6", "A* h2"]],
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
            case '3':
                table = list(map(int, input('\nВведите начальную таблицу, пробелами обозначая переход на новую строку или введите 0\n>').split(' ')))
                start_node = Node(get_initial_state(table), None, None, 0, 0)
                result_node, iterations = greedy_best_first_search(start_node, get_finish_state(), h1)
            case '4':
                table = list(map(int, input('\nВведите начальную таблицу, пробелами обозначая переход на новую строку или введите 0\n>').split(' ')))
                start_node = Node(get_initial_state(table), None, None, 0, 0)
                result_node, iterations = greedy_best_first_search(start_node, get_finish_state(), h2)
            case '5':
                table = list(map(int, input('\nВведите начальную таблицу, пробелами обозначая переход на новую строку или введите 0\n>').split(' ')))
                start_node = Node(get_initial_state(table), None, None, 0, 0)
                result_node, iterations = a_star_search(start_node, get_finish_state(), h1)
            case '6':
                table = list(map(int, input('\nВведите начальную таблицу, пробелами обозначая переход на новую строку или введите 0\n>').split(' ')))
                start_node = Node(get_initial_state(table), None, None, 0, 0)
                result_node, iterations = a_star_search(start_node, get_finish_state(), h2)
            case _:
                print("Некорректный ввод")
        repeat = input("\nПерезапуск? (Y/N)\n > ")
