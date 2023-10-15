saved_passwords = ["12345", "abcde", "54321"]
user_password = input("Введіть пароль: ")

if user_password in saved_passwords:
    print("Ви маєте доступ. Пароль вірний.")
else:
    print("Вам відмовлено в доступі. Пароль не вірний.")
