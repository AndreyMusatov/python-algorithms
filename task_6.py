"""
Задание 6. На закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте класс-структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
3) список решенных задач, куда задачи перемещаются из базовой очереди или
очереди на доработку

После реализации структуры, проверьте ее работу на различных сценариях

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

class TaskBoard:
    def __init__(self):
        self.elems = []

    def __str__(self):
        if not self.elems:
            return 'Все задания выполнены.'
        else:
            return f'Список дел: {self.elems}.'

    def is_empty(self):
        return self.elems == []

    def add_task(self, task):
        self.elems.insert(0, task)

    def del_task(self):
        if self.elems:
            task = self.elems.pop()
            print(f'Задание "{task}" выполнено.')
        else:
            print('Заданий больше нет, можешь ехать домой =)')

    def size(self):
        return len(self.elems)


if __name__ == '__main__':
    to_do_list = TaskBoard()
    to_do_list.add_task('Сдать работу')
    to_do_list.add_task('Зайти на встречу')
    print(to_do_list)
    to_do_list.del_task()
    to_do_list.add_task('Заказать домой еду')
    to_do_list.del_task()
    to_do_list.del_task()
    print(to_do_list)
    to_do_list.add_task('Пройти Обучения')
    print(to_do_list)
    to_do_list.del_task()
    to_do_list.del_task()
    print(to_do_list)