# 3.4. Реализовать программу шифрующую строку, задаваемую пользователем, с помощью алгоритма шифрования ROT13. 
#      Формирование отчета по выполнению задания и размещение его в портфолио, персональном репозитории.

def rot13(str):
    new_str = ""
    for letter in str:
        lr = ord(letter)
        if (65 <= lr <= 77) or (97 <= lr <= 109) or (1040 <= lr <= 1055) or (1072 <= lr <= 1087):
           new_str += chr(lr + 13)
        elif (78 <= lr <= 90) or (110 <= lr <= 122) or (1056 <= lr <= 1071) or (1088 <= lr <= 1103):
           new_str += chr(lr - 13)
        else:
            new_str += letter
    print(new_str)

if __name__ == "__main__":
    user_text = input("Введите строку: ")
    rot13(user_text)
