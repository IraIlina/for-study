#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class List_Iterator:
    def __init__(self, list):
        self._list = list
        self._index = -1
        self._len = len(list)

    def __next__(self):
        self._index += 1
        if self._index < self._len - 1:
            return self._list[self._index]
        else:
            raise StopIteration


class Node:
    def __init__(self, value,
                 prev_pointer = None, next_pointer = None):
        self.set_value(value)
        self.set_prev(prev_pointer)
        self.set_next(next_pointer)

    def get_value(self):
        return self._value

    def get_next(self):
        return self._next_pointer

    def get_prev(self):
        return self._prev_pointer

    def set_value(self, value):
        self._value = value

    def set_prev(self, prev_pointer):
        self._prev_pointer = prev_pointer

    def set_next(self, next_pointer):
        self._next_pointer = next_pointer

    def __str__(self):
        return str(self.get_value())
    

class List:
    def __init__(self, collection = None):
        self._start_pointer = None
        self._finish_pointer = None
        self._length = 0

        if isinstance(collection, list):
            for i in collection:
                self.append(i)

        if isinstance(collection, int):
            self.append(collection)

    def __len__(self):
        return self._length
    
    def append(self, value):
        if self._length == 0:
            self._start_pointer = Node(value)
            self._finish_pointer = self._start_pointer
            self._length = 1
        else:
            self._finish_pointer.set_next(Node(value,
                                               self._finish_pointer))
            self._finish_pointer = self._finish_pointer.get_next()
            self._length += 1

            
    def __getitem__(self, i):
        if i < 0 or i >= self._length:
            return False

        if i < self._length / 2:
            curr_pointer = self._start_pointer
            for j in range(i):
                curr_pointer = curr_pointer.get_next()

        elif i > self._length / 2:
            curr_pointer = self._finish_pointer
            for j in range(self._length - i - 1):
                curr_pointer = curr_pointer.get_prev()

        return curr_pointer.get_value()
    
    
    def __str__(self):
        arr = []
        for i in range(self._length):
            arr.append(str(self[i]))
        return "[" + ", ".join(arr) + "]"

    def __add__(self, other):
        for i in range(other._length):
            self.append(other[i])
        return self

    def __radd__(self, other):
        for i in range(self._length):
            other.append(self[i])
        return other
  

    def pop(self, i):
        m = List()
        a = self[i]
        for j in range(self._length - 1):
            if j < i:
                m.append(self[j])
            else:
                m.append(self[j + 1])
        self = m
        return a
    
    def __iter__(self):
        return List_Iterator(self)
    
    def _save_ (self, name="Date.bin"):
        with open (name, mode="wb") as f:
            pickle.dump(self, f)
    
    def _open_(self):
        try:
            name = input()
            with open(name, mode = 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            print ('Файла не существует!')
    
      
A = List()
for i in range(5):
    A.append(i)
for element in A:
    print(element)
print(A)

A._save_()
print(A.open_bin('Date.bin'))

