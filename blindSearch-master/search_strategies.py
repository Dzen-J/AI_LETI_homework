import sys
from time import process_time

from node import Node
from basic_operations import print_info, check_final, state_hash, \
    get_followers, print_state, print_node, print_path, get_initial_state, MOVES

sys.setrecursionlimit(1000000)  # Предел рекурсии
DEBUG = False


def search(debug_flag: int, table=[0], depth_limit: int = None):
    """
    Поиск в глубину.
    :param debug_flag: Выбор пользователя относительно пошагового вывода поиска.
    :param depth_limit: Ограничение для поиска с ограничением глубины.
    """
    global DEBUG
    DEBUG = debug_flag

    # Выводим сообщение о начале алгоритма DLS
    if depth_limit:
        print("ПОИСК В ГЛУБИНУ С ОГРАНИЧЕНИЕМ DLS — Deep-Limited Search.")
    else:
        print("ПОИСК СНАЧАЛА В ГЛУБИНУ DFS — Depth-first Search.")
    start_node = Node(get_initial_state(table), None, None, 0, 0)  # Начальный узел
    visited_states = set()  # Множество посещенных состояний
    stack = [start_node]  # стек для хранения узлов
    result_node = None  # Переменная для хранения результата
    iterations = 0  # Счетчик итераций
    defining_sequences.limit_reached = False  # Ограничитель на рекурсию

    START_TIME = process_time()
    # Основной цикл алгоритма
    while stack:
        result_node, iterations = defining_sequences(stack.pop(), visited_states, stack, iterations, depth_limit)
        if result_node is not None:
            break

    if result_node is not None:
        TIME_STOP = process_time()
        print("\n---Конечное состояние достигнуто!---")
        print_path(result_node)
        print("Информация о поиске:")
        print_info(iterations=iterations, time=TIME_STOP - START_TIME, visited_states=len(visited_states),
                   path_cost=result_node.path_cost)
    else:
        print("\nПуть к конечному состоянию не найден.")


def defining_sequences(current_node: "Node", visited_states: set,
                       stack: list, iterations: int, depth_limit: int = None):
    """
    Рекурсивная часть алгоритма поиска в глубину.
    :param current_node: Текущий обрабатываемый узел.
    :param visited_states: Список посещённых состояний.
    :param stack: Стек узлов .
    :param iterations: Количество прошедших итераций.
    :param depth_limit: Ограничение в глубину для поиска с ограничением.
    :return: Найденное конечное состояние и затраченное для этого количество итераций.
    """
    iterations += 1  # Увеличиваем счетчик итераций

    # Проверяем, достигнуто ли конечное состояние
    if check_final(current_node.current_state):
        return current_node, iterations

    # Хэшируем текущее состояние для проверки посещенных состояний
    state_hash_value = state_hash(current_node.current_state)

    visited_states.add(state_hash_value)  # Добавляем текущее состояние в множество посещенных

    # Проверка для ограниченного по глубине поиска
    if depth_limit is not None and current_node.depth >= depth_limit:
        if not defining_sequences.limit_reached:
            print("\nДостигнуто ограничение глубины!")
            stack.clear()  # Очищаем стек
            defining_sequences.limit_reached = True  # Меняем флаг достижения глубины
        return None, iterations

    new_states_dict = get_followers(current_node.current_state)  # Получаем новые состояния из текущего узла

    # Отладочный вывод текущего узла и всех его потомков по шагам
    if DEBUG:
        print(f"----------------Шаг {iterations}.---------------- \n")
        print("Текущий узел:", end=' ')
        if iterations == 1:
            print("Корень дерева")
        print_node(current_node)
        print("Потомки:")

    # Исследуем каждого потомка
    for child_action, child_state in new_states_dict.items():
        # Хэшируем состояние и инициализируем как узел
        child_hash_value = state_hash(child_state)
        if child_hash_value not in visited_states:
            child_node = Node(child_state, current_node, child_action, current_node.path_cost + 1,
                              current_node.depth + 1)
            if DEBUG:
                print_node(child_node)
            stack.append(child_node)  # Помещаем узел в стек
        elif DEBUG:
            print(f"Повторное состояние: \nAction = {MOVES[child_action]}, \nState: ")
            print_state(child_state)
    if DEBUG:
        input("Нажмите 'Enter' для продолжения...")

    # Рекурсивно переходим к обработке полученных потомков, удаляя их постепенно из очереди
    while stack:
        result_node, iterations = defining_sequences(stack.pop(), visited_states, stack, iterations, depth_limit)
        if result_node is not None:
            return result_node, iterations

    return None, iterations
