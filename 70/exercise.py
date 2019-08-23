from random import choice

COLORS = 'red blue green yellow brown purple'.split()


class EggCreator:

    '''Iterator that generates a <limit> number of eggs of random colours'''

    def __init__(self, limit=1):
        self.num = limit
        self.count = 0
        self.eggs = [choice(COLORS) + ' egg' for x in range(limit)]

    def __iter__(self):
        return self

    def __next__(self):
        count = self.count
        if count in range(self.num):
            self.count += 1
            return self.eggs[count]
        else:
            raise StopIteration
