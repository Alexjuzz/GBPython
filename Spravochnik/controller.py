import view 
import import_date
import export




def main():
    zapros = view.choise()
    test_list = list(zapros[0].split())
    if 1 == zapros[1]:
        

        if (len(test_list) == 4):
            import_date.write_date(test_list)
            view.create_log('log_request_import',view.export.exp(test_list),'Результат запроса')
        else:
            print('введены некорректные данные иди гуляй')

    else:
        view.out_put(export.exp(test_list))
        view.create_log('log_request_export',view.export.exp(test_list),'Результат запроса')