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
        pass

    #Time complexity: O(n) - linear time in size of list
    def __str__(self): # Bjarmi
        # TODO: remove 'pass' and implement functionality
        return ', '.join(self.array)

    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index): # Bjarmi
        # TODO: remove 'pass' and implement functionality
        if (len(self.array) - 1) < index:
            raise IndexOutOfBounds()    
        return self.array.insert(index, value)

    #Time complexity: O(1) - constant time
    def append(self, value):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(1) - constant time
    def set_at(self, value, index): # Bjarmi
        # TODO: remove 'pass' and implement functionality
        if (len(self.array) - 1) < index:
            raise IndexOutOfBounds()    
        self.array.pop(index, value)
        return self.array.insert(index, value)

    #Time complexity: O(1) - constant time
    def get_first(self):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(1) - constant time
    def get_at(self, index): # Bjarmi
        # TODO: remove 'pass' and implement functionality
        if (len(self.array) - 1) < index:
            raise IndexOutOfBounds()
        return self.array[index]

    #Time complexity: O(1) - constant time
    def get_last(self):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    def resize(self): # Bjarmi
        # TODO: remove 'pass' and implement functionality
        self.array.extend(array2)
        self.array += array2

    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(1) - constant time
    def clear(self): # Bjarmi
        # TODO: remove 'pass' and implement functionality
        return self.array.clear()

    #Time complexity: O(n) - linear time in size of list
    def insert_ordered(self, value):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def find(self, value): # Bjarmi
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    def remove_value(self, value):
        # TODO: remove 'pass' and implement functionality
        pass


if __name__ == "__main__":
    pass
    # add your tests here or in a different file.
    # Do not add them outside this if statement
    # and make sure they are at this indent level

    arr_lis = ArrayList()
    print(str(arr_lis))