import random
import array as arr



class Sorting:
    size = 0
    list = 0

    def __init__(self, size):
        self.size = size
        self.list = list()
        self.fill_List()
        self.bubble()

    def fill_List(self):
        for i in range(0, self.size-1):
            n = random.randint(0, 20)
            self.list.append(n)


    def bubble(self):
        n = len(self.list)

        # Traverse through all list elements
        for i in range(n - 1):
            # range(n) also work but outer loop will repeat one time more than needed.

            # Last i elements are already in place
            for j in range(0, n - i - 1):

                # traverse the list from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if self.list[j] > self.list[j + 1]:
                    self.list[j], self.list[j + 1] = self.list[j + 1], self.list[j]

        for x in self.list:
            print(x)
