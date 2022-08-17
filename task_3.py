"""
Задание 3.

Для этой задачи
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""
dict1 = {'name1': 134, 'name2': 12345, 'name3': 1234, 'name4': 12346, 'name5': 1234, 'name6': 3456}
cntmax = 3

def key_max(dict_in): # O(n)
# возвращает ключ наибольшего
    value_max = dict_in[list(dict_in.keys())[0]] # O(1)
    for key in dict_in.keys(): # O(n)
        value = dict_in[key] # O(1)
        if value > value_max: # O(1)
            res = key # O(1)
            value_max = value # O(1
    return res # O(1)

def list_1(dict_in): # O(n)
# проверка исходных данных
    if len(dict_in) <= cntmax: # O(1)
        print(f'В хранилище не более {cntmax} компаний!') # O(1)
        return # O(1)
# cntmax раз сделать:
# найти наибольший, исключить его
    dict_ = dict_in.copy() # O(n)
    for i in range(cntmax): # O(n)
        res = key_max(dict_) # O(n)
        print(i + 1, res) # O(1)
        dict_[res] = -111111111 # O(1)

list_1(dict1)

##########################

dict2 = {'name1': [1234, 0], 'name2': [134, 0], 'name3': [234, 0], 'name4': [1234, 0], 'name5': [1234, 0], 'name6': [3456, 0]}
cntmax = 3

def list_2(dict_in): # O(n**2)
    if len(dict_in) <= cntmax: # O(1)
        print(f'В хранилище не более {cntmax} компаний!')
        return
# для каждого посчитать количество превышающих его
    dict_ = dict_in.copy() # O(n)
    for key1 in dict_.keys(): # O(n)
        value = dict_[key1] # O(1)
        value[1] = 0 # O(1)
        for key2 in dict_.keys(): # O(n)
            if key2 == key1: # O(1)
                continue # O(1)
            if dict_[key2][0] > value[0]: # O(1)
                value[1] += 1 # O(1)
# найти cntmax первых в порядке убывания количества превышающих
    cnt = 0 # счётчик найденных  O(1)
    n = 0 # количество превышающих O(1)
    while cnt < cntmax: # O(1)
        for item in dict_.items(): # O(n)
            if item[1][1] == n: # O(1)
                cnt += 1 # O(1)
                print(cnt, item[0]) # O(1)
            if cnt == cntmax: # O(1)
                break
        n += 1 # O(1)

list_2(dict2)

# Функция list_1 имеет меньшую сложность (O(n) < O(n**2)), поэтому эффективнее
