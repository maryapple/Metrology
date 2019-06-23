from math import sqrt, erfc
from scipy.stats import norm

def func(filename):
    result = []
    with open(r"C:\Users\Asus\Documents\MIEM\Metrology\hw2\Chvn_v31_b.txt", 'r') as f:
        for row in f:
            s = row[0] + '.' + row[2:]
            result.append((float(s)))
    return result

def Average(lst):
    return sum(lst) / len(lst)

def Deviation(lst):
    av = Average(lst)
    s = 0
    for i in lst:
        s += (i - av) ** 2
    return sqrt(s / (len(lst) - 1))

def integral_fun(x):
    # интегральная функция стандартного нормального распределения
    return norm.cdf(x, loc=0, scale=1)

def Chauvenet_criteria(lst, out, outliers = []):
    # список со значениями без промахов
    results = []

    av = Average(lst)
    dev = Deviation(lst)

    # Проверяемые значения
    cur = []
    for i in lst:
        cur.append((abs(i - av) / dev))

    # значения интегральной функции для каждого элемента
    integral_list = []
    for i in cur:
        integral_list.append(integral_fun(i))

    # вероятности получения результата, превышающего модуль сомнительного элемента
    probabilities = []
    for i in integral_list:
        probabilities.append((1 - i) * 2)

    # ожидаемое число результатов
    expct = []
    for i in probabilities:
        expct.append(i * len(lst))


    checking = []
    for i in expct:
        if i < 0.5:
            checking.append('Выброс')
        else:
            checking.append('Не выброс')

    # формируем списки промахов, значений без промахов
    for i in range(len(checking)):
        if checking[i] == 'Не выброс':
            results.append(lst[i])
        else:
            out.append(expct[i])
            outliers.append(lst[i])
    return results