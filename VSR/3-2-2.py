# 3.4. Реализовать программу шифрующую строку, задаваемую пользователем, с помощью алгоритма шифрования, использующего
#      сдвиг на определенное количество знаков (шифр Цезаря). Сдвиг задается пользователем.


def rot_n(str, n_for_rot):
    new_str = ""
    for letter in str:
        lr = ord(letter)
        eng_alphabet = 28
        rus_alphabet = 32
        if_rot_eng = eng_alphabet % n_for_rot
        if_rot_rus = rus_alphabet % n_for_rot
        if (65 <= lr <= 90) or (97 <= lr <= 122):
            if (if_rot_eng == 0):
                new_str += chr(lr + n_for_rot)
            else:
                new_str += chr(lr + if_rot_eng)
        elif (1040 <= lr <= 1071) or (1072 <= lr <= 1103):
            if (if_rot_rus == 0):
                new_str += chr(lr + n_for_rot)
            else:
                new_str += chr(lr + if_rot_rus)
        else:
            new_str += letter
    print(new_str)

if __name__ == "__main__":
    user_text = input("Введите строку: ")
    user_rot_n = int(input("Введите длину сдвига: "))
    rot_n(user_text, user_rot_n)
