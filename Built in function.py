# Bulit in function uses
# Analyzing the list of Salary of Worker

# how to take a list value from user ( for mixed value type)    
# get a space-separted list of values from the user
input_salary = input("enter a list of salary values Separated by spaces :")

# split the input string into list of strings using space as the sperator.
input_list= input_salary.split()

# intiaalize an empty list to store the converted values
mixed_list =[]

 # iterate through the input_list and try to convert each elemnt to the appropriate data type
for item in input_list:
    if item.isdigit():
        # if the item is a digit convert it to an integer
        mixed_list.append(int(item))

    else:
        try:
             # try to convert the item to float
             mixed_list.append(float(item))
       

        except ValueError:
            # if conversion to float fails, consider it a string
            mixed_list.append(str(item))
        
   
    
    
    
        
#now , you have a list of integer of integer provided by the user
print(" user input as a list of integer:", mixed_list)

Salary_list = list(mixed_list)
# Basic Statistics
total_Salary = sum(Salary_list)
print(total_Salary)
Avarage_salary = total_Salary / len(Salary_list)
print(Avarage_salary)
highest_Salary = max(Salary_list)
print(highest_Salary)
lowest_Salary = min(Salary_list)
print(lowest_Salary)

# Sorting
sorted_Salary_list = sorted(Salary_list)
print(sorted_Salary_list)
sorted_Salary_list_descending = sorted(Salary_list, reverse=True)
print(sorted_Salary_list_descending)



# List Length
number_of_Salary = len(Salary_list)
print(number_of_Salary)

# Removing Duplicates (not applicable in this case)

# indexing (first and last Salary)
first_Salary_list = Salary_list[0]
print(first_Salary_list)
last_Salary_list = Salary_list[-1]
print(last_Salary_list)

#round off the avaerage salary
avarage_salary_Rounded = round(Avarage_salary)
print(Avarage_salary)

# Ranging of salary
for i in range(Salary_list[0],Salary_list[4]):
    print(i)
    print(bin(i))
#enumerate(): Adds counter to an iterable and returns it in a form of enumerate object
enumerate_list= list(enumerate(Salary_list))
print(enumerate_list)

# types
print(type(Salary_list))

#print no of bytes 
print(bytes(11))

#print(Character) equivalent to given ascii value as salary
print(chr(1111))

#print the complex form of an salary vallues
print(complex(1232))
#print a frozen set of salary_list 

frozenset_salary_list= frozenset(salary_list)

#print memory view of specific salary 
x=memoryview(b'11')
print(x)





