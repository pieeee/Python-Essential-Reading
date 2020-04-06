#LIST FUNCTION AND ITS COMMON METHODS:


#***LIST.APPEND(OBJECT)***
list1 = ['Hermione', 'David', 'Cherry']
list2 = ['Eshan', 'Estes', 'Rojin']
list1.append(list2)
a = list1
print(a)
#result: ['Hermione', 'David', 'Cherry', ['Eshan', 'Estes', 'Rojin']]


#***LIST.EXTEND(OBJECT)***
list3 = ['Hermione', 'David', 'Cherry']
list4 = ['Eshan', 'Estes', 'Rojin']
list3.extend(list4)
b = list3
print(b)
#result: ['Hermione', 'David', 'Cherry', 'Eshan', 'Estes', 'Rojin']


#***LIST.POP(INDEX)***
list5 = ['Hermione', 'David', 'Cherry', 'Eshan', 'Estes', 'Rojin']
c = list5.pop(4)
print(c)
#result: Estes (Removed the 4th element of the container)


#***LIST.INDEX(OBJECT, RANGE)***
list6 = ['Hermione', 'David', 'Cherry', 'Eshan', 'Estes', 'Rojin']
d = list6.index('David')
print(d)
#e = list6.index('David', 3) print(e)
#result(d): 1 (Declaring "David" position; start from 0)
#result(e): e = list6.index('David', 3) ValueError: 'David' is not in list


#***LIST.__getitem__(index)***
list7 = ['Hermione', 'David', 'Cherry', 'Eshan', 'Estes', 'Rojin']
e = list7.__getitem__(3)
print(e)
#result: Eshan
#**Alternate to __getitem__ method
print(list7[3])
#result: Eshan


#***List Item Slicing
list7 = ['Hermione', 'David', 'Cherry', 'Eshan', 'Estes', 'Rojin']
print(list7[1:3])
#result: ['David', 'Cherry']
print(list7[0:3])
#result: ['Hermione', 'David', 'Cherry']
print(list7[:3])
#result: ['Hermione', 'David', 'Cherry']
print(list7[3:])
#result: ['Eshan', 'Estes', 'Rojin']


#***List Item Slicing






