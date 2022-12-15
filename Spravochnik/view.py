import export
from datetime import datetime as dt
from tabulate import tabulate
def choise():
    try:
        i = int(input('Введите запрос 1 - ввод данных, 0 - считать данные: '))
        if type(i) == int:
            if i == 1:
                a = input('Введите имя фамилию номер локацию ')
                print(a)
                create_log('log_add.txt',a)
                return (a, 1)
            else:
                b = input("Веведите  фамилию ")
                create_log('log_output.txt',b,'запрос :')
                return (b, 0)
    except:
        print('Non correct date')
        create_log('crash.txt',Exception(),'Exeption : ')

def out_put(list_export : list):
       print(tabulate(list_export,headers=['Фимилия','Имя','Город','Телефон'],tablefmt='orgtbl'))

def create_log(log_name_file,data,send_message = 'Запрос :'):
    time = dt.now().strftime('%H:%M:%S')
    with open(log_name_file, "a", encoding= 'utf-8') as log:
        log.write('{} - время. {} : {};'.format(time,send_message,data)+ '\n')
        
