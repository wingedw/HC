mylist = ['a','b', '62', '66', 'b']
print(mylist[0]) # a

print(mylist[1:3]) # ['b',62]

print(mylist[:1]) # ['a']

print(mylist[:-1]) #['a', 'b', 62, 66]

print(len(mylist)) # 5

print(mylist.count('b')) # 2

mylist.sort()
print(mylist) # ['62', '66', 'a', 'b', 'b']

mylist.remove('a')
print(mylist) # ['62', '66', 'b', 'b']

mylist.append('c')
print(mylist) # ['62', '66', 'b', 'b', 'c']

mylist.pop() # Removes last item added
print(mylist) # ['62', '66', 'b', 'b']

mylist.pop(1) #Removes by index
print(mylist) # ['62', 'b', 'b']

print('b' in mylist) # True

