class MyList():
    a = list

    def __init__(self):
        self.a = self.a()

    def get_list(self):
        return self.a.copy()


b = MyList()

print(b.a)

c = b.get_list()
c.append(1)

print(b.a)