
import simpleHT

class LinearProbedHashTable(simpleHT.SimpleHashTable):

    def Insert(self, item):
        while(True):
            try:
                index = self.HashFunction(item)
                while(self.Table[index] != None):
                    index += 1
                self.Table[index] = item
                break
            except:
                self.Table.append(None)

    def Search(self, item):
        try:
            index = self.HashFunction(item)
            while(True):
                if self.Table[index] == item :
                    return index
                index += 1
        except:
            return -1

    def isEmpty(self):
        if len(self.Table) == 0:
            return True
        else:
            return False 
    
    def Refresh(self):
        while(not self.isEmpty()):
            item = self.Table.pop()
            if item != None:
                self.Table.append(item)
                break

    def Delete(self, item):
        try:
            index = self.HashFunction(item)
            while(True):
                if self.Table[index] == item :
                    self.Table[index] = None
                    self.Refresh()
                    break
                index += 1
        except:
            pass


