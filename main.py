# Программа-шагомер для фитнес-трекера

import datetime as dt

FORMAT = '%H:%M:%S'  # Формат полученного времени.
WEIGHT = 75  # Вес.
HEIGHT = 175  # Рост.
K_1 = 0.035  # Коэффициент для подсчета калорий.
K_2 = 0.029  # Коэффициент для подсчета калорий.
STEP_M = 0.65  # Длина шага в метрах.

storage_data = {}  # Словарь для хранения полученных данных.


def check_correct_data(data):
    """Проверка корректности полученного пакета."""
    if len(data) != 2 or (None in data):
        return False
    # Если длина пакета отлична от 2
    # или один из элементов пакета имеет пустое значение -
    # функция вернет False, иначе - True.


def check_correct_time(time):
    """Проверка корректности параметра времени."""
    if storage_data is not None:
        for time_check in storage_data.keys():
            if dt.datetime.strptime(time_check, FORMAT).time() >= time:
                return False
    # Если словарь для хранения не пустой
    # и значение времени, полученное в аргументе,
    # меньше самого большого ключа в словаре,
    # функция вернет False.
    # Иначе - True


def get_step_day(steps):
    """Получить количество пройденных шагов за этот день."""
    all_day_steps = sum(storage_data.values()) + steps
    return all_day_steps
    # Все шаги, записанные в словарь storage_data.


def get_distance(steps):
    """Получить дистанцию пройденного пути в км."""
    distance = (steps * STEP_M) / 1000
    return distance
    # Дистанция в километрах,
    # исходя из количества шагов и длины шага.


def get_spent_calories(dist, current_time):
    """Получить значения потраченных калорий."""
    hours = current_time.hour + current_time.minute / 60
    mean_speed = dist / hours
    minutes = current_time.hour * 60 + current_time.minute
    spent_calories = (K_1 * WEIGHT + (mean_speed ** 2 / HEIGHT) * K_2 * WEIGHT) * minutes
    return spent_calories

def get_achievement(dist):
    """Получить поздравления за пройденную дистанцию."""
    if dist >= 6.5:
        return 'Отличный результат! Цель достигнута.'
    elif dist >= 3.9:
        return 'Неплохо! День был продуктивным.'
    elif dist >= 2:
        return 'Маловато, но завтра наверстаем!'
    else:
        return 'Лежать тоже полезно. Главное — участие, а не победа!'
    # Поздравление (достижение) пользователя.


def show_massage(time, steps, dist, calories, achievement):
    return (f"""
Время: {time}.
Количество шагов за сегодня: {steps}.
Дистанция составила {dist:.2f} км.
Вы сожгли {calories:.2f} ккал.
{achievement}
""")
# Показ сообщения в зависимости от результата.

def accept_package(data):
    """Обработать пакет данных."""

    if check_correct_data(data) is False:  # Если функция проверки пакета вернет False
        return 'Некорректный пакет'

    time, steps = data
    pack_time = dt.datetime.strptime(time, FORMAT).time()  # Преобразование времени в объект типа time.

    if check_correct_time(pack_time) is False:  # Если функция проверки значения времени вернет False
        return 'Некорректное значение времени'

    day_steps = get_step_day(steps)  # Результат подсчёта пройденных шагов.

    dist = get_distance(steps) + get_distance(
        sum(storage_data.values()))  # Результат расчёта пройденной дистанции.

    spent_calories = get_spent_calories(dist, pack_time)  # Результат расчёта сожжённых калорий.

    achievement = get_achievement(dist)  # Мотивирующее сообщение.

    print(show_massage(pack_time, day_steps, dist, spent_calories, achievement))  # Демонтрация пользователю.

    storage_data.update({data})  # Добавить новый элемент в словарь storage_data.

    return storage_data  # Возвращаем словарь storage_data.


# Данные с фитнес-трекера
package_0 = ('2:00:01', 505)
package_1 = (None, 3211)
package_2 = ('9:36:02', 15000)
package_3 = ('9:36:02', 9000)
package_4 = ('8:01:02', 7600)

# Вызов функции
accept_package(package_0)
accept_package(package_1)
accept_package(package_2)
accept_package(package_3)
accept_package(package_4)