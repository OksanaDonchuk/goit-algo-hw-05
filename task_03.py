import timeit
from typing import Callable, List, Tuple
from bm_search import boyer_moore_search
from kmp_search import kmp_search
from rk_search import rabin_karp_search

def measure_time(search_function: Callable[[str, str], int], text: str, pattern: str) -> float:
    """
    Вимірює час виконання пошукового алгоритму.

    Args:
        search_function (Callable[[str, str], int]): Функція пошуку.
        text (str): Основний текст.
        pattern (str): Підрядок для пошуку.

    Returns:
        float: Час виконання у секундах (округлений до 8 знаків після коми).
    """
    execution_time = timeit.timeit(lambda: search_function(text, pattern), number=1)
    return round(execution_time, 8)  # Округлюємо до 8 знаків

def compare_algorithms(text: str, pattern: str) -> List[Tuple[str, float]]:
    """
    Запускає всі три алгоритми пошуку та вимірює їх час виконання.

    Args:
        text (str): Основний текст.
        pattern (str): Підрядок для пошуку.

    Returns:
        List[Tuple[str, float]]: Список із назвами алгоритмів та їхнім часом виконання.
    """
    return [
        ("Boyer-Moore", measure_time(boyer_moore_search, text, pattern)),
        ("KMP", measure_time(kmp_search, text, pattern)),
        ("Rabin-Karp", measure_time(rabin_karp_search, text, pattern))
    ]

def print_results(title: str, results: List[Tuple[str, float]]) -> None:
    """
    Виводить результати у вигляді відформатованої таблиці.

    Args:
        title (str): Заголовок таблиці.
        results (List[Tuple[str, float]]): Дані для виводу.
    """
    print(f"\n {title}")
    print("=" * 40)
    print(f"{'Алгоритм':<15} | {'Час виконання, с':<15}")
    print("-" * 40)
    for algo, time in results:
        print(f"{algo:<15} | {time:<15.8f}")  # форматований час
    print("=" * 40)

# Завантажуємо тексти
with open("text_1.txt", "r", encoding='utf-8') as file:
    text1 = file.read()

with open("text_2.txt", "r", encoding='utf-8') as file:
    text2 = file.read()

# Вибираємо підрядки
existing_substring = "структури даних"  # підрядок, який є в тексті
non_existing_substring = "неіснуючий рядок"  # підрядок, якого немає в тексті

# Вимірюємо час виконання для кожного випадку
results_text1_existing = compare_algorithms(text1, existing_substring)
results_text1_non_existing = compare_algorithms(text1, non_existing_substring)
results_text2_existing = compare_algorithms(text2, existing_substring)
results_text2_non_existing = compare_algorithms(text2, non_existing_substring)

# Виводимо результати у вигляді таблиць (без tabulate)
print_results("Text 1 (існуючий підрядок)", results_text1_existing)
print_results("Text 1 (неіснуючий підрядок)", results_text1_non_existing)
print_results("Text 2 (існуючий підрядок)", results_text2_existing)
print_results("Text 2 (неіснуючий підрядок)", results_text2_non_existing)