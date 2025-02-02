from tabulate import tabulate

class HashTable:
    """
    Реалізація хеш-таблиці з методом відкритої адресації (ланцюгове хешування).
    """
    
    def __init__(self, size: int) -> None:
        """
        Ініціалізує хеш-таблицю з певним розміром.

        Args:
            size (int): Розмір таблиці (кількість бакетів).
        """
        self.size = size
        self.table: list[list[tuple[str, int]]] = [[] for _ in range(self.size)]

    def hash_function(self, key: str) -> int:
        """
        Генерує хеш для ключа.

        Args:
            key (str): Ключ для хешування.

        Returns:
            int: Індекс у хеш-таблиці.
        """
        return hash(key) % self.size

    def insert(self, key: str, value: int) -> bool:
        """
        Додає нову пару ключ-значення в хеш-таблицю.

        Args:
            key (str): Ключ.
            value (int): Значення.

        Returns:
            bool: True, якщо вставка успішна.
        """
        key_hash = self.hash_function(key)

        for pair in self.table[key_hash]:
            if pair[0] == key:
                pair[1] = value  # Оновлюємо значення
                return True

        self.table[key_hash].append([key, value])
        return True

    def get(self, key: str) -> int | None:
        """
        Отримує значення за ключем.

        Args:
            key (str): Ключ для пошуку.

        Returns:
            int | None: Значення, якщо ключ знайдено, інакше None.
        """
        key_hash = self.hash_function(key)
        for pair in self.table[key_hash]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key: str) -> bool:
        """
        Видаляє пару ключ-значення з хеш-таблиці.

        Args:
            key (str): Ключ, який потрібно видалити.

        Returns:
            bool: True, якщо ключ знайдено і видалено, інакше False.
        """
        key_hash = self.hash_function(key)
        for i, (stored_key, _) in enumerate(self.table[key_hash]):
            if stored_key == key:
                del self.table[key_hash][i]
                return True
        return False

    def __contains__(self, key: str) -> bool:
        """
        Перевіряє, чи є ключ у хеш-таблиці.

        Args:
            key (str): Ключ для перевірки.

        Returns:
            bool: True, якщо ключ є, False, якщо немає.
        """
        return self.get(key) is not None

    def __str__(self) -> str:
        """
        Повертає табличне представлення хеш-таблиці.

        Returns:
            str: Вміст хеш-таблиці у вигляді відформатованої таблиці.
        """
        table_data = []
        for i, bucket in enumerate(self.table):
            if bucket:
                for key, value in bucket:
                    table_data.append([i, key, value])

        return tabulate(table_data, headers=["Bucket", "Key", "Value"], tablefmt="grid") if table_data else "Хеш-таблиця порожня"
    
# Тестуємо хеш-таблицю:
H = HashTable(5)
H.insert("apple", 10)
H.insert("orange", 20)
H.insert("banana", 30)

print("Вся таблиця до видалення елемента:\n", H)
print("Значення ключа 'apple':", H.get("apple"))  
print("Значення ключа 'orange':", H.get("orange"))  
print("Значення ключа 'banana':", H.get("banana"))  

H.delete("orange")  

print("\n Вся таблиця після видалення 'orange':\n", H)