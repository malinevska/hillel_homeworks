import unittest
from homework_12_1 import find_longest_word, find_substring, has_unique_chars

class TestHomeworks(unittest.TestCase):

    # Тести для find_longest_word (Task 1)
    def test_longest_word_positive(self):
        """Позитивний тест: звичайний список"""
        self.assertEqual(find_longest_word(["apple", "banana", "kiwi"]), "banana")

    def test_longest_word_empty_list(self):
        """Граничне значення: порожній список"""
        self.assertEqual(find_longest_word([]), "")

    def test_longest_word_same_length(self):
        """Специфічний випадок: слова однакової довжини (має повернути перше)"""
        self.assertEqual(find_longest_word(["cat", "dog", "bat"]), "cat")

    # Тести для find_substring (Task 2)
    def test_find_substring_exists(self):
        """Позитивний тест: підрядок існує"""
        self.assertEqual(find_substring("Hello world", "world"), 6)

    def test_find_substring_not_exists(self):
        """Негативний тест: підрядок відсутній"""
        self.assertEqual(find_substring("Hello world", "python"), -1)

    def test_find_substring_start(self):
        """Позитивний тест: підрядок на самому початку"""
        self.assertEqual(find_substring("Hello", "H"), 0)

    def test_find_substring_empty_sub(self):
        """Граничне значення: порожній підрядок (find повертає 0)"""
        self.assertEqual(find_substring("Hello", ""), 0)

    # Тести для has_unique_chars (Task 3)
    def test_unique_chars_true(self):
        """Позитивний тест: більше 10 унікальних символів"""
        self.assertTrue(has_unique_chars("abcdefghijk")) # 11 символів

    def test_unique_chars_false(self):
        """Позитивний тест: рівно 10 унікальних символів (має бути False)"""
        self.assertFalse(has_unique_chars("abcdefghij"))

    def test_unique_chars_short(self):
        """Позитивний тест: коротка строка"""
        self.assertFalse(has_unique_chars("abc"))

if __name__ == '__main__':
    unittest.main()
