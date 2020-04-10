# Python_Simple_HashTables
some simple hash tables :P


#how to use 

#importing
import ChainedHashTable

#create a hash function
def myfunction(mychar):
    return ord(mychar)

#create a table
mytable = ChainedHashTable(myfunction)

#append an item
mytable.Insert('h')

#get the table
print(mytable.getTable())
