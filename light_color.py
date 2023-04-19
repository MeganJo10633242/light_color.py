# Программа для определения цвета света
# на основе длины волны

def determine_color(wavelength):
    """
    Функция для определения цвета света
    на основе длины волны.

    Аргументы:
    wavelength -- длина волны (в нанометрах)

    Возвращает:
    color -- цвет света
    """
    if 380 <= wavelength < 450:
        color = "фиолетовый"
    elif 450 <= wavelength < 495:
        color = "синий"
    elif 495 <= wavelength < 570:
        color = "зеленый"
    elif 570 <= wavelength < 590:
        color = "желтый"
    elif 590 <= wavelength < 620:
        color = "оранжевый"
    elif 620 <= wavelength <= 750:
        color = "красный"
    else:
        color = "невидимый"
    return color


# Пример использования функции
wavelength = 500  # нм
color = determine_color(wavelength)
print(f"Свет с длиной волны {wavelength} нм -- это {color} свет")
