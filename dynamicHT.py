
import simpleHT

class DynamicHashTable(simpleHT.SimpleHashTable):

    _slots_ = 'Table', 'HashFunction'

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
            self.Table[self.HashFunction(item)] = None
            self.Refresh()
        except:
            pass
        

