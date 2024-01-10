class MySimpleIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        else:
            i = self.data[self.index]
            self.index += 1
            return i


my_list = [1, 2, 3, 4, 5]
my_iterator = MySimpleIterator(my_list)

for i in my_iterator:
    print(i)
