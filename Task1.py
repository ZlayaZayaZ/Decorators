import datetime
import re


def log_decor(old_function):
    def new_function(*args, **kwargs):
        datetime_function = datetime.datetime.now()
        result = old_function(*args, **kwargs)
        print(f'Дата и время вызова функции: {datetime_function.strftime("%Y-%m-%d-%H.%M.%S")}')
        print(f'Имя функции - {old_function.__name__}')
        print(f'*args - {args}, **kwargs - {kwargs}')
        print(f'Возвращаемое функцией значение{result}')
        with open('log_list.txt', 'a', encoding='utf-8') as file:
            file.write(f'Дата и время вызова функции: {datetime_function.strftime("%Y-%m-%d-%H.%M.%S")}\n')
            file.write(f'Имя функции - {old_function.__name__}\n')
            file.write(f'*args - {args}, **kwargs - {kwargs}\n')
            file.write(f'Возвращаемое функцией значение{result}\n')
            file.write(f'\n')
        return result
    return new_function


@log_decor
def converting_a_string_into_a_set(string):
    string_list = re.findall("\w+", string)
    set_string = set(string_l.lower() for string_l in string_list)
    return set_string


string_1 = 'Здесь должна быть ваша реклама.'
string_2 = 'Программирование - особый вид искусства.'

if __name__ == '__main__':
    converting_a_string_into_a_set(string_1)
    print('-' * 9)
    converting_a_string_into_a_set(string_2)
    print('-' * 9)


