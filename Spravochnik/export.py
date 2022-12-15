import csv
list_find_values = []


def exp(str_find):
   
    with open('db.csv', encoding='utf-8') as f:
        list_find_values = csv.reader(f)
        result_list = []
        for val in list_find_values:
            if find_val(str_find, val):
                result_list.append(val)
        some_list = []
        for i in result_list:
            if i not in some_list:
                some_list.append(i)

        if not some_list:
            print('Совподения не найдены')
        else : 
            return some_list

def find_val(str_val, list_val):
    count = 0
    string_lenght= len(str_val)
    for i in list_val:
        if i in str_val:
            count +=1
    if count == string_lenght:
        return True
    else : False