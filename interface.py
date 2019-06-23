from tkinter import *
from metrology_0_2 import *
import matplotlib.pyplot as plt
from pandas import DataFrame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = Tk()

def graph_initial(lst):
    av = Average(lst)
    dev = Deviation(lst)

    fig = plt.figure()   # Создание объекта Figure
    print(fig.axes)   # Список текущих областей рисования пуст
    print(type(fig))   # тип объекта Figure

    for tmp in lst:
        p = erfc(abs(tmp - av)/dev)
        plt.scatter(tmp, p)   # scatter - метод для нанесения маркера в точке (1.0, 1.0)

    # После нанесения графического элемента в виде маркера
    # список текущих областей состоит из одной области
    print(fig.axes)

    plt.title('Начальная выборка')
    plt.ylabel('Критерий')
    plt.xlabel('Значения выборки')

    plt.show()

def graph_corrected(lst):
    av = Average(lst)
    dev = Deviation(lst)

    fig = plt.figure()  # Создание объекта Figure
    print(fig.axes)  # Список текущих областей рисования пуст
    print(type(fig))  # тип объекта Figure

    for tmp in lst:
        p = erfc(abs(tmp - av) / dev)
        plt.scatter(tmp, p)  # scatter - метод для нанесения маркера в точке (1.0, 1.0)

    # После нанесения графического элемента в виде маркера
    # список текущих областей состоит из одной области
    print(fig.axes)
    plt.title('График наличия выбросов')
    plt.ylabel('Критерий')
    plt.xlabel('Значения выборки')

    plt.show()

def start():
    # Начальная выборка
    outliners = []
    expct = []
    a = func(EntryFileName.get())
    print("initial list:", a)
    print("Average of initial list: %f" % Average(a))
    print("Deviation of initial list: %f" % Deviation(a))
    graph_initial(a)

    # Исправленная выборка
    b = a
    corrected_lst = Chauvenet_criteria(b, expct, outliners)

    text = f"Выброс(-ы): {outliners}\nпоскольку {expct} < 0.5"
    label = Label(text=text, justify=LEFT, font='Arial 10')
    label.place(relx=.0, rely=.1)
    
    print("Corrected list:", corrected_lst)
    print("Average of new list: %f" % Average(corrected_lst))
    print("Deviation of new list: %f" % Deviation(corrected_lst))

    graph_corrected(corrected_lst)

# создаем панель на которой расположены все элементы

root.title("Проверка выборки на наличие промахов по критерию Шовене и их исключение")
root.geometry("1000x500")

# лейбл поля ввода названия
name0 = "Введите название файла:"
label0 = Label(text=name0, justify=LEFT, font='Arial 10')
label0.place(relx=.05, rely=.1)

# поле ввода названия
EntryFileName = Entry(root, width=20, font='Arial 10') #, message = filename)
EntryFileName.insert(0, "Chvn_v31_a.txt")
EntryFileName.place(relx=.05, rely=.2)

# лейбл вывода НАЧАЛЬНОГО среднего значения
name11 = "Среднее начальное значение:"
label1 = Label(text=name11, justify=LEFT, font='Arial 10')
label1.place(relx=.05, rely=.3)

# вывод начального среднего значения
EntryFirstAverage = Entry(root, width=10, font='Arial 10')
EntryFirstAverage.place(relx=.05, rely=.4)

# лейбл вывода НАЧАЛЬНОГО отклонения
name12 = "Отклонение:"
label2 = Label(text=name12, justify=LEFT, font='Arial 10')
label2.place(relx=.05, rely=.5)

# вывод начального отклонения
Entry12 = Entry(root,  width=10, font='Arial 10')
Entry12.place(relx=.05, rely=.6)

# лейбл вывода КОНЕЧНОГО среднего значения
name21 = "Среднее значение:"
label21 = Label(text=name21, justify=LEFT, font='Arial 10')
label21.place(relx=.25, rely=.3)

# вывод конечного среднего значения
EntrySecondAverage = Entry(root, width=10, font='Arial 10')
EntrySecondAverage.place(relx=.25, rely=.4)

# лейбл вывода КОНЕЧНОГО отклонения
name22 = "Отклонение:"
label22 = Label(text=name22, justify=LEFT, font='Arial 10')
label22.place(relx=.25, rely=.5)

# вывод конечного отклонения
Entry22 = Entry(root, width=10, font='Arial 10')
Entry22.place(relx=.25, rely=.6)

# кнопка запуска
btn = Button(text="Запуск", background="#ffc0cb", foreground="#000000",
	padx="16", pady="5", font='Arial 13', command = lambda: start())
btn.place(relx=.05, rely=.75)

root.mainloop()