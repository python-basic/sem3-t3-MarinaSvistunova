# 3.3. Создание скрипта для считывания данных справочных логов из текстового файла и преобразования их в CSV-формат
#     с последующей записью в новый файл. Формирование отчета по выполнению задания и размещение его в портфолио,
#     персональном репозитории. 


# Логи: https://github.com/python-basic/sem3-t3-MarinaSvistunova/blob/master/ISR/data.txt
# CSV-файл: https://github.com/python-basic/sem3-t3-MarinaSvistunova/blob/master/ISR/data.csv


import csv

def txt_reader(log_for_csv):
    with open("data.csv", "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        for line in log_for_csv:
            writer.writerow(line.replace('"', '').replace('\n', '').split(','))

if __name__ == "__main__":
    with open("data.txt") as data_log:
        txt_reader(data_log)
