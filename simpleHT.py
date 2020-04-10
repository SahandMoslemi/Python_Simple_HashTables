
class SimpleHashTable():

    _slots_ = 'Table', 'HashFunction'

    def __init__(self, HashFunc):
        self.HashFunction = HashFunc
        self.Table = list()

    def Insert(self, item):
        while(True):
            try:
                self.Table[self.HashFunction(item)] = item
                break
            except:
                self.Table.append(None)

    def Search(self, item):
        try:
            if self.Table[self.HashFunction(item)] == item:
                return self.HashFunction(item)
            return -1
        except:
            return -1
                
    def Delete(self, item):
        try:
            self.Table[self.HashFunction(item)] = None
        except:
            pass

    def getTable(self):
        return self.Table

    def isEmpty(self):
        if len(self.Table) == 0:
            return True
        else:
            return False 


