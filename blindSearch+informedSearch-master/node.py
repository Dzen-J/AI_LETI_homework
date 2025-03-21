class Node:
    """
    Класс представления узла.
    """
    current_state: list = None  # Текущее состояние
    parent_node: "Node" = None  # Указатель на родительский узел
    previous_action: tuple = None  # Действие, применённое к родительскому узлу
    path_cost: int = 0  # Стоимость пути от начального узла к данному
    depth: int = 0  # Глубина узла
    node_id: int = 0  # ID узла (его индекс в общем массиве узлов)
    heuristic: int = 0  # Эвристическая оценка

    nodes_count = 0  # Общее количество представителей класса

    def __init__(self, state: list, parent: "Node", action: tuple, cost: int, depth: int, heuristic: int = 0):
        """
        Конструктор класса.
        :param state: Текущее состояние.
        :param parent: Родительский узел.
        :param action: Действие, применённое к родительскому узлу.
        :param cost: Стоимость.
        :param depth: Глубина.
        :param heuristic: Эвристическая оценка.
        """
        self.current_state = state
        self.parent_node = parent
        self.previous_action = action
        self.path_cost = cost
        self.depth = depth
        self.heuristic = heuristic
        self.node_id = Node.nodes_count

        Node.nodes_count += 1

    def __lt__(self, other: "Node"):
        """
        Оператор сравнения для приоритетной очереди.
        :param other: Другой узел.
        :return: True, если текущий узел меньше другого.
        """
        return (self.path_cost + self.heuristic) < (other.path_cost + other.heuristic)

    @classmethod
    def get_nodes_count(cls) -> int:
        """
        Геттер количества узлов.
        :return: Количество узлов.
        """
        return cls.nodes_count