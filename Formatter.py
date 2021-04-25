class StringFormatter:
    def __init__(self, string, spliter=' '):
        self.__string = string
        self.__split_let = spliter

    @property
    def string(self):
        return self.__string

    def split_str(self):
        return self.__string.split(self.__split_let)

    def __str__(self):
        return self.__string

    def del_less(self, n):
        res=''
        for i, word in enumerate(self.split_str()):
            if len(word) < n:
                continue
            res += word+' '
        self.__string = res

    def change_num(self):
        for i, sym in enumerate(self.__string):
            if sym.isdigit():
                self.__string = self.__string.replace(self.__string[i], '*')

    def set_spaces(self):
        string = ''.join(self.split_str())
        self.__string = ' '.join(string)

    def sort_by_len(self):
        self.__string = ' '.join(sorted(self.split_str(),key=lambda x: len(x)))

    def sort_by_alph(self):
        self.__string = ' '.join(sorted(self.split_str(),key=lambda x: (str.lower(x),x)))


string = StringFormatter('There are people who are fond of repairing things')
string.del_less(4)
print(string)
string2 = StringFormatter('There are 456644 who are fond of 7888999 things')
string2.change_num()
print(string2)
string.set_spaces()
print(string)
string3 = StringFormatter('There are people who are fond of repairing things')
string3.sort_by_len()
print(string3)
string3.sort_by_alph()
print(string3)