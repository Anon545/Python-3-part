#методы списков

# append - добавление в конец  списка
res=[]
print(res)
res.append('oleg')
print(res)
res.append('danil')
print(res)
res.append('artem')
print(res)

# extend - добавление содержимого списка
tr = [12,35,55]
res.extend(tr)
#res.append(tr)
print(res)

# insert - вставка в список со сдвигом
res.insert(2, 'Alex')
print(res)
# pop - вырезать элемент из списка
print(res.pop(3))
print(res)

# remove - удаление
res.remove('oleg')
print(res)

# index - 
print(res.index('danil'))