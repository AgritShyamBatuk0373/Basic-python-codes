# String operattions
a= "ab1cd2ef3gh4"
print(a[1:50])

print(a[5:6])

print(a[-1:-2])

print(a[4:10])

print(a[11:11])

print(a[15:-12:-1])

print(a[0:-11])

print(a[-12:11:5])

print(a[0:13:2])

print(a[-4:-10:-2])

print(a[0:12:11])

print(a[10:11]*3)

print(a[2:3]+a[-7:-6]+a[9:10]+a[2:3]*2)

print('abra' + 'ca' + 'dabra')

print( "ra" in "abra")

print("rasp' + 'berry")
print('db' in'123dabra')
print(a[6:10:1])
''' print[10;12;1]
    1) h6
    2) h4
    3) 4
    4) ''
    5) SyntaxError '''

print(a[-2:-6])
'''
    1- ef3g
    2- g3fe
    3- ''
    4- SyntaxError
    5- hg3
'''
print(a[-7:-12:-1])
'''
    1- 2dc1b
    2-  2dc1
    3- 1cd2
    4- 2dc1ba
    5- None of these
    '''
'''
print(a[8:11:0])
1- ''
2- 3gh
3- 3g
4- 3
5- valueerror
'''

# List operation

L=["is",'life','even','fun']
L.insert(1,"college")
print(L)

L=['why','only', 'me', 'you', '?',4,5,6]
L.remove(4)
print(L)
'''
1-[]
2-['why','only', 'me', 'you', '?',4,5,6]
3- ['why','only', 'me', 'you', '?',5,6]
4- ['why','only', 'me', 'you',4,5,6]
5- ['why','only', 'me', '?',4,5,6]
'''

#print([3,4,5] + 'ghhh')

# Dictionary Operation
D={ "name":"Dinesh","age":18,"class":'CSE-303', "Status": "single", "Studying":['CSE','EEE','Phy']}
#print(D["Studying"]['1'])
'''
1-['CSE','EEE','Phy']
2-['CSE']
3- ['EEE']
4- Error
'''
print(D['age'])

'''
1- Error
2-m18
3-'18'
4-'age'
'''

