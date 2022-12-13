import export
from tabulate import tabulate
def choise():
    try:
        i = int(input('Введите запрос 1 - ввод данных, 0 - считать данные: '))
        if type(i) == int:
            if i == 1:
                a = input('Введите имя фамилию номер локацию ')
                return (a, 1)
            else:
                b = input("Веведите  фамилию ")
                return (b, 0)

    except:
        print("Non correct")

def out_put(list_export : list):
       print(tabulate(list_export,headers=['Фимилия','Имя','Город','Телефон'],tablefmt='orgtbl'))