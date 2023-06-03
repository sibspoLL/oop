import time # импортируем модуль времени
class Time:
    'СОЗДАТЬ КЛАСС С УКАЗАННЫМИ ДВУМЯ АТРИБУТАМИ (ПОЛЕ 1, ПОЛЕ 2) И ТРЕМЯ МЕТОДАМИ :'
    #'- КОНСТРУКТОР ДЛЯ ИНИЦИАЛИЗАЦИИ ОБЪЕКТА'
    #'- ФУНКЦИЯ ФОРМИРОВАНИЯ СТРОКИ С ИНЦОРМАЦИЕЙ ОБ ОБЪЕКТЕ'
    #'- задача по варианту

    'В ОСНОВНОЙ ПРОГРАММЕ ВВОДИТЬ ЗНАЧЕНИЯ ПОЛЕЙ КАЖДОГО ОБЪЕКТА ИЗ КОМПОНЕНТОВ EDIT И ВЫВОДИТЬ РЕЗУЛЬТАТЫ'
    'В КОМПОНЕНТ MEMO'

    def __init__(self,hour, minute ,second ): # конструктор для иницилизации объекта
        self.hour = hour    # =
        self.minute= minute # =        # self - ссылка на объект
        self.second = second  #
        print("Инициализатор сработал")

    def __del__(self):
        print('Объект уничтожен')


# НАДО СОЗДАТЬ КЛАСС ПОТОМОК ДЛЯ КЛАССА Time

class Times(Time): # новый класс наследуется от Time
        def __init__(self, train_number,departure,departure_time):
            # Father.__init__(self, name, lastname) ????????????    ????????????    ?????????    ???????
            self.train_number=train_number
            self.departure=departure
            self.departure_time=departure_time

        def kol_vo__min(self,spisok_otpravlenie): # функция-метод класс потомка
            print("внутри функции kol_vo__min")
            print(spisok_otpravlenie)
            print(spisok_time_now)


# kvm=Times()

# номер поезда - train_number
# направление - departure
# время отправления - departure_time

#СПРАШИВАЕМ У ПОЛЬЗОВАТЕЛЯ ИНФОРМАЦИЮ ПО РАСПИСАНИЮ ДВИЖЕНИЯ ПОЕЗДОв
print(f"Введите номер поезда:")
x1=str(input("  Номер поезда = "))
print(f"Введите направление поезда")
x2=str(input("  нап равление поезда = "))
# время отправления - сделать списком
print(f"Введите время отправления")
print(f"    Введите часы")
h1=int(input("  h = "))
print(f"    Введите минуты")
min1=int(input("min = "))
print(f"    Введите секунды")
sec1=int(input("sec = "))
print()

# еще раз реализую всё что со временем
n_t = time.localtime()
t_s = time.strftime("%H:%M:%S",n_t)
r_t = time.strptime(t_s, "%H:%M:%S")

h_h=r_t[3]
m_m=r_t[4]  # взял из массива time.struct_time 3,4,5 - элементы и поместил в переменные
c_c=r_t[5]






spisok_otpravlenie=[h1,min1,sec1] # часы минуты секунды ВРЕМЕНИ ОТПРАВЛЕНИЯ
spisok_time_now=[h_h,m_m,c_c]  # часы минуты секунды  ТЕКУЩЕГО ВРЕМЕНИ
# КОЛ-ВО_МИНУТ =  ВРЕМЕНИ ОТПРАВЛЕНИЯ - ТЕКУЩЕГО ВРЕМЕНИ

kol_min=(h1-h_h)*60+(min1-m_m)*1+(sec1-c_c)//60
print(f"Кол-во минут до отправления поезда: {kol_min}")
if(kol_min<0):
    print("Вы опаздали на поезд")
print()








print(f"Список ВРЕМЕНИ ОТПРАВЛЕНИЯ: {spisok_otpravlenie}")
print(f"Список ТЕКУЩЕГО ВРЕМЕНИ: {spisok_time_now}")

object2 = Times(x1,x2,spisok_otpravlenie)

print(".............................................")
print(f"Получена от вас следующая информация:")
print(f"    номер поезда: {object2.train_number}")
print(f"    направление поезда: {object2.departure}")
print(f"    время отправления: {object2.departure_time} [часы, минуты, секунды]")
print()

def info_of_object(self): # выводит информацию об объекте
    print(repr(self))

# Здесь реализую всё что со временем

named_tuple = time.localtime()
time_string = time.strftime("%H:%M:%S", named_tuple)

print(f"Время сейчас : {time_string}")

result = time.strptime(time_string, "%H:%M:%S")

#print(result) # большой вывод time
# time.struct_time(tm_year=1900, tm_mon=1, tm_mday=1, tm_hour=15, tm_min=24, tm_sec=47, tm_wday=0, tm_yday=1, tm_isdst=-1)
# из кортежа отбираю нужные эл-ты соответсвующие часам минутам секундам
#print(f"    h={result[3]}")
#print(f"    min={result[4]}")   # ТЕКУЩЕЕ ВРЕМЯ !!!!!!!!!!!!!!!!!!!!!!!!
#print(f"    sec={result[5]}")

h=result[3]
m=result[4]  # взял из массива time.struct_time 3,4,5 - элементы и поместил в переменные
c=result[5]

# print(h,m,c)


print(".............................................")



del object2








#Любой конструктор __init__ является методом перегрузки.
#в питоне нет понятия конструктор, в питоне нет перегрузки как таковой
# def __init__ - инициализатор
# в питоне нету перегрузки,
# деструктора нет потому что python сам память подчищает за собой
# Этим сборщик мусора занимается
# А про деструкторы — временем жизни объекта управляет сам интерпретатор и
# мы не можем гарантировать, когда он умрёт.
