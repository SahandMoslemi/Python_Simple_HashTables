
import simpleHT

class ChainedHashTable(simpleHT.SimpleHashTable):

    _slots_ = 'Table', 'HashFunction'

    def Insert(self, item):
        while(True):
            try:
                if item not in self.Table[self.HashFunction(item)]:
                    self.Table[self.HashFunction(item)].append(item)
                    break
            except:
                self.Table.append(list())
    
    def Search(self, item):
        if item not in self.Table[self.HashFunction(item)]:
            return -1
        else:
            return self.HashFunction(item)

    def isEmpty(self):
        if len(self.Table) == 0:
            return True
        else:
            return False 

    def Refresh(self):
        while(not self.isEmpty()):
            item = self.Table.pop()
            if len(item) != 0:
                self.Table.append(item)
                break

    def Delete(self, item):
        try:
            self.Table[self.HashFunction(item)].remove(item)
            self.Refresh()
        except:
            pass





