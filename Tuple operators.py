# operation on Tuple2sz
a=(23, 45, 56, 234, " 23", "Shyam","Baishanav","Shri Hari","Narayan", -234,243)

 # indexing operations
print(a[4])
print(a[-8])
print(a[-3])

# slicing operation
print(a[0:13])
print(a[-3:])
print(a[ -3: -10: -2])

# membership:
if "Hari" in a:
    print("\n yes Shyam")
else:
    print("\n No Krishna")
    
# concatenation in tuple
b=(235,21,"Krishna")

print(a+b)

# repetition on tuple
print((a+b)* (len(b)-1))

 # inserting operation
a.insert(0,"Bhairav")
print(a)  # output will be error from here because tupple is immutable

# Remoaving an element in tuple
a.remove(234)
print(a)  # output will be error from here because tupple is immutable

#Updating the tuple
print(a[4])
a[4]= "Rudra"
print(a) # output will be error from here because tupple is immutable



