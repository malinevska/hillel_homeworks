def find_longest_word(word_list):
    """Повертає найдовше слово у списку."""
    if not word_list:
        return ""
    longest_word = ""
    for word in word_list:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word


def find_substring(str1, str2):
    """Повертає індекс першого входження другого рядка у перший."""
    return str1.find(str2)


def has_unique_chars(text):
    """Повертає True, якщо унікальних символів більше 10."""
    unique_chars = set(text)
    return len(unique_chars) > 10
