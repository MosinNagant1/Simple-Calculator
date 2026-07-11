#Список разрешённых символов

available = set("01234567890+-*/() ")

while True:

    try:
        example = input(">> ")
        clear = ''.join(c for c in example if c in available)




        if clear != example:

            print("Используйте только числа или знаки, доступны 01234567890+-*/()")
            continue


        if clear:
            try:
                result = eval(clear)
                print(f"= {result}")
            except:
                print("Ошибка в примере, проверьте скобки и правильность написания")
                print("Введите ваш пример")

        else:
            print("Пустой ввод")


    except:
        break











