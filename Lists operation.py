# operation on lists
a=[ 23, 45, 56, 234, " 23", "Shyam","Baishanav","Shri Hari","Narayan"]

 # indexing operations
print(a[5])
print(a[3])
print(a[-3])
print(a[-0])

# slicing operation
print(a[0:13])
print(a[-3:])
print(a[ -3: -10: -2])

# membership:
print("Shyam" in a)
print("Har" in a)
    

#Updating the list
print(a[4])
a[4]= "Rudra"
print(a)

# inserting operation
a.insert(0,"Bhairav")
print(a)

# Remoaving an element in list
a.remove(234)
print(a)


