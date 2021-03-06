class IndexOutOfBounds(Exception):
    pass

class NotFound(Exception):
    pass

class Empty(Exception):
    pass

class NotOrdered(Exception):
    pass

class ArrayList:
    def __init__(self):
        # TODO: remove 'pass' and implement functionality
        self.cap = 4
        self.size = 0
        self.arr = [0] * self.cap



    #Time complexity: O(n) - linear time in size of list
    def __str__(self): # Bjarmi
        # TODO: remove 'pass' and implement functionality
        str_val = ""
        for i in range(self.size):
            str_val += str(self.arr[i])
        return str_val

#     #Time complexity: O(n) - linear time in size of list
#     def prepend(self, value):
#         # TODO: remove 'pass' and implement functionality
#         pass

    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index): # Bjarmi
        # TODO: remove 'pass' and implement functionality
        if index + 1 > self.cap:
            raise IndexOutOfBounds()
        self.arr[index] = value
        return self.arr

#     #Time complexity: O(1) - constant time
#     def append(self, value):
#         # TODO: remove 'pass' and implement functionality
#         pass

    #Time complexity: O(1) - constant time
    def set_at(self, value, index): # Bjarmi
        # TODO: remove 'pass' and implement functionality
        if ((self.cap) - 1) < index:
            raise IndexOutOfBounds()    
        self.arr.pop(index)
        return self.arr.insert(index, value)

#     #Time complexity: O(1) - constant time
#     def get_first(self):
#         # TODO: remove 'pass' and implement functionality
#         pass

    #Time complexity: O(1) - constant time
    def get_at(self, index): # Bjarmi
        # TODO: remove 'pass' and implement functionality
        if ((self.cap) - 1) < index:
            raise IndexOutOfBounds()
        return self.arr[index]

#     #Time complexity: O(1) - constant time
#     def get_last(self):
#         # TODO: remove 'pass' and implement functionality
#         pass

    #Time complexity: O(n) - linear time in size of list
    def resize(self): # Bjarmi
        # TODO: remove 'pass' and implement functionality
        if ((self.cap)-1) < self.size:
            new_arr = self.arr * 2
            for i in range(self.size):
                new_arr[i] = self.arr[i]
            self.arr = new_arr
            return new_arr
        return self.arr

    #Time complexity: O(n) - linear time in size of list
#     def remove_at(self, index):
#         # TODO: remove 'pass' and implement functionality
#         pass

    #Time complexity: O(1) - constant time
    def clear(self): # Bjarmi
        # TODO: remove 'pass' and implement functionality
        self.size = 0
        return self.size

#     #Time complexity: O(n) - linear time in size of list
#     def insert_ordered(self, value):
#         # TODO: remove 'pass' and implement functionality
#         pass

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def find(self, value): # Bjarmi
        # TODO: remove 'pass' and implement functionality

        return self.arr.index(value)
#        for i in range(self.size):
#           return self.arr[i]

#     #Time complexity: O(n) - linear time in size of list
#     def remove_value(self, value):
#         # TODO: remove 'pass' and implement functionality
#         pass


if __name__ == "__main__":
    pass
    # add your tests here or in a different file.
    # Do not add them outside this if statement
    # and make sure they are at this indent level

    arr_lis = ArrayList()
    print(str(arr_lis))
