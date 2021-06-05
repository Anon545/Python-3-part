#списки
"""
#arr = [1, 6, 'g', 'word', [1, 5 , 'g'], True, len(s), -98, 0.00112]
#print(arr)
"""
""" #сложение списков
#arr1 = [1, 2, 4, 6]
arr1 = ['1', '2', '4', '6']
arr2 = ['a', 'b', 'c', 'd']
arr3 = arr1 + arr2
print(arr3)
# #stroka ='0'.join(arr3) #вставка символа в строку arr3 после кажд.символа
# #print(stroka)
"""
""" #замена символов
#arr2[0] ='z' #замена нулевого символа в списке arr2
print (arr3[1:7:2])
arr3[1:7:2] = ['A', 'A', 'A']
print (arr3)
"""
#копирование списка
arr1 = ['1', '2', '4', '6']
arr2 = ['a', 'b', 'c', 'd']
arr3 = arr1 + arr2
arr4 = arr3.copy()
print(arr3)
print(arr4)
