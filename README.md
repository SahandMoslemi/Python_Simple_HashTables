# Python_Simple_HashTables


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
