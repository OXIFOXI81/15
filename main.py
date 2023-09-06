 # Итератор
class FlatIterator:

    def __init__(self):
         pass

    def __iter__(self):
        print('начали цикл')
        self.main_index = 0  # курсор основного списка
        self.nexted_index = 0  # курсор списка вложенного в основной список
        self.numbers=[]
        return self

    def __next__(self):
        if self.nexted_index >= len(self.numbers):
            if self.main_index>=len(some_list):
                raise StopIteration()
            self.numbers = some_list[self.main_index]
            self.main_index =self.main_index+ 1
            self.nexted_index=0
        self.nexted_index= self.nexted_index+1
        return self.numbers[self.nexted_index-1]

def flat_generator(some_list):
  for elem in some_list:
     for el in elem:
        yield el

if __name__ == '__main__':
  my_set=[]
  some_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

  for item in FlatIterator():
      my_set.append(item)
  print(f"Итератор  {my_set}")

  my_set = []

#  Генератор

  for item in flat_generator(some_list):
         my_set.append(item)
  print(f"Генератор {my_set}")
