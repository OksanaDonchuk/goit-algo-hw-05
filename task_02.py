from typing import List, Tuple, Optional

def binary_search(arr: List[float], target: float) -> Tuple[int, Optional[float]]:
    """
    Реалізує двійковий пошук у відсортованому масиві дробових чисел.
    
    Args:
        arr (List[float]): Відсортований масив дробових чисел.
        target (float): Число, яке потрібно знайти.

    Returns:
        Tuple[int, Optional[float]]: Кортеж, де:
            - Перший елемент — кількість ітерацій, потрібних для знаходження елемента.
            - Другий елемент — "верхня межа" (найменший елемент, який є більшим або рівним заданому значенню).
    """
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_limit: Optional[float] = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if arr[mid] == target:
            return (iterations, arr[mid])  # Якщо знайшли точний елемент, повертаємо його як upper_limit

        elif arr[mid] < target:
            left = mid + 1
        else:
            upper_limit = arr[mid]  # Запам'ятовуємо найменше більше або рівне число
            right = mid - 1

    # Якщо target більший за всі елементи, upper_limit має залишитись None
    if left < len(arr):
        upper_limit = arr[left]  # Найменше число, більше за target

    return (iterations, upper_limit)

# Тестуємо функцію:
arr = [2.6, 3.8, 4.6, 6.3, 8.2, 9.1]

# Цільове число є в масиві
print(binary_search(arr, 4.6))

# Цільове число між елементами
print(binary_search(arr, 5))

# Цільове число більше всіх елементів
print(binary_search(arr, 10))

# Цільове число менше всіх елементів
print(binary_search(arr, 2))