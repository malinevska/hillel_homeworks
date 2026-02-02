default_text = "Monica is a cute Yorkiepoo, about 4 years old. She has a beautiful coat without any white markings."
user_string = input("Enter text (or press Enter for default): ") or default_text
unique_chars = set(user_string)
count = len(unique_chars)

print(f"Text: {user_string}")
print(f"Number of unique characters: {count}")
print(count > 10)
