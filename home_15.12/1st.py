from datetime import datetime, timedelta
import calendar

input_Date = input()
a = datetime.strptime(input_Date, '%d.%m.%Y')
# print(f"{a.strftime('%d')} {a.strftime('%B')} {a.strftime('%y')}")
# b = timedelta(days = 3)
# c = a + b
# print(str(f"{c.strftime('%d')} {c.strftime('%B')} {c.strftime('%y')}"))

brain = int(input())
count_week = int(input())
count_print = int(input())
list_start = [a, brain, count_week, count_print]


def print_date(list_date: list):
    list_else = []
    if (list_date[1] == 1):
        cou = 0
        to_exit = 0
        correct_date = timedelta(days=list_date[-2]*3)
        while to_exit < list_date[-1]:
                list_date[0] += correct_date   
                list_else.append(str(f"{list_date[0].strftime('%d')} {list_date[0].strftime('%B')} {list_date[0].strftime('%y')}"))             
                print(str(f"{list_date[0].strftime('%d')} {list_date[0].strftime('%B')} {list_date[0].strftime('%y')}"))
                to_exit +=1
    else : 
        to_exit = 0
        cou =0
        correct_date = timedelta(days = 1)
        while to_exit < list_date[-1]: 
            if list_date[0].strftime('%a') == 'Thu' and cou % list_date[-2] == 0:
                    print(str(f"{list_date[0].strftime('%d')} {list_date[0].strftime('%B')} {list_date[0].strftime('%y')}"))
                    list_else.append(str(f"{list_date[0].strftime('%d')} {list_date[0].strftime('%B')} {list_date[0].strftime('%y')}"))
                    list_date[0] += correct_date   
                    cou +=1
                    to_exit+=1

            else:
                 list_date[0] += correct_date 
                 cou +=1
    return list_else
# print(print_date(list_start))
print_date(list_start)
