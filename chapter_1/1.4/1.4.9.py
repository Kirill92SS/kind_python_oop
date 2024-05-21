import sys


lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')
    a = {}
    def insert(self, data):
        for _ in range(len(data)):
            self.lst_data.append({k: v for k, v in zip(self.FIELDS, data[_].split(' '))})
        self.a.setdefault()

    def select(self, a, b):
        return self.lst_data[a:b+1]


db = DataBase()
db.lst_data.set
db.insert(lst_in)
