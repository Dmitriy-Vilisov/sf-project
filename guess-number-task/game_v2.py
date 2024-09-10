"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Функция подсчета попыток угадать число "number", с учетом информации о том что больше или меньше искомое число выбранного в каждой итерации числа
    Args:
        number (int, optional): Загаданное число. Defaults to 1.
    Returns:
        int: Число попыток
    """
    count = 0  # Счетчик количества попыток
    start = 1  # Нижний предел поиска
    finish = 101  # Верхний предел поиска
    
    while True:
        count += 1
        predict_number = np.random.randint(start, finish)  # Предполагаемое число выбираеся радномно, ограничиваясь верхним и нижним пределом
        
        if number == predict_number:
            break  # Выход из цикла если угадали число
        elif number > predict_number:
            start = predict_number  # Повышаем нижний предел поиска
        elif number < predict_number:
            finish = predict_number  # Понижаем верхний предел поиска
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм
    Args:
        random_predict ([int]): функция, результатом которой является количество попыток отгадать число "number"
    Returns:
        int: среднее количество попыток
    """
    np.random.seed(1)  # Фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # Загадали список чисел
    count_ls = []  # Инициализируем список с количеством попыток отгадать число в загаданном списке чисел

    for number in random_array:
        count = random_predict(number)  # Считаем количество попыток отгадать число 'number' в списке чисел
        count_ls.append(count)

    medium_score = int(np.mean(count_ls))  # Считаем среднее количество попыток
    print(f"Ваш алгоритм угадывает число в среднем за:{medium_score} попыток") 
    return medium_score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)

