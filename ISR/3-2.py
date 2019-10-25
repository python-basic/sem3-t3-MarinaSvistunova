# 3.2. Разработка сценария с реализацией операции поиска подстроки в тексте. 

def main():
  input_str = input("Введите строку для поиска: ")

  searchable_str = input("Введите строку, в которой мы ищем: ")
    
  choice = None
  while choice != '4':

    print('1 - поиск первого вхождения подстроки')
    print('2 - замена первой подстроки')
    print('3 - найти все вхождения подстроки' )
    print('4 - для выхода')
    choice = input("Сделайте  выбор (1..4) ")
        
    if choice == '1':
      search_str(input_str, searchable_str)

    if choice == '2':
      rep_str = input('Строка для замены: ')
      print(searchable_str.replace(input_str, rep_str))

    if choice == '3':
      search_n_replace_str(input_str,  len(searchable_str), searchable_str)

def search_str(what="", where=""):
  # 1 - поиск первого вхождения подстроки
  print("Номер первого вхождение строки: " + str(where.find(what)))

def search_n_replace_str(what="",  to_what="", where=""):
  # 3 - найти все вхождения подстроки
  print("Количество вхождений: " + str(where.count(what, 0, to_what)))

main()
