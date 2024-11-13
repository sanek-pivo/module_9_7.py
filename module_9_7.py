def is_prime(function): # Функция декоратор
    def wrapper(*args, **kwargs): #аргументы декорируемой функции передаются функции-обёртке
        Null = function(*args, **kwargs)
        for i in range(2,Null):
            if Null % i == 0:
                print('Составное') # если составное число
                break
        else: # иначе печатает другое
            print('Простое') # если простое число

        return Null # возвращает функцию Null
    return wrapper #  is_prime должна возвращает wrapper


@is_prime
def sum_three(a, b, c):
    summa = a + b + c # Функция которая складывает 3 числа
    return summa


result = sum_three(2, 3, 6)
print(result)