
#%%1
for i in range(11): 
    print(i)



# %%
list = ["Akash", "Daniel", "Bob", "Joe" ]

for i in range(len(list)):
    print(list[i])
# %%
list = {1,2,3,4,5,6,7}
count = 0

for i in range(len(list)): 
    count = count + i

print(count)
# %%

word = "python"
reversed = ""

for char in word: 
    reversed = char + reversed
print(reversed)
# %%
word = "banana"

letterCount = {}

for char in word: 

    if char in letterCount: 
        letterCount[char] +=1

    else: 
        letterCount[char]  =1

for char, count in letterCount.items(): 
    print (f"{char}: {count}")
# %%

students = {
    'student1': {
        "Name": "Akash", 
        "Grade" : 68
    }, 
    'student2': {
        "Name": "Daniel",
        "Grade": 92
    }, 
    'student': {
        "Name": "Bob", 
        "Grade": 58
    } 
 }

for i in students : 
    if students[i]["Grade"] >= 60 :
        print(students[i]["Name"])
        print(students[i]["Grade"])
# %%

num = 5

for i in range(1,11): 
    print(f"{num} x {i} = {num * (i)}")
# %%
i = 1
while i < 11: 
    print (i)
    i+= 1 

# %%
name = ""
while name.lower() != "quit":
    name = input("Enter a name (or 'quit' to stop): ")
    
    if name.lower() != "quit":
        print(f"Hello, {name}!")
# %%

num = int(input("Enter a number"))
if (num % 2 == 0) : 
    print("The number is even.")
else: 
    print("The number is odd.")
# %%
import random
list = []

for i in range(10): 
    list.append(random.randint(1, 100))
print (list)

small = 101
large = 0

length = len(list) - 1
for i in range(length): 
    if list[i] < small : 
        small = list[i]
    if list[i] > large:
        large = list[i]

print(f"Largest is {large}.")
print(f"Smallest is {small}.")
# %%

fruits = {
    'fruit1': {
        "Name": "apple", 
        "Price": 3
    }, 
    'fruit2' : {
        "Name": "banana", 
        "Price": 4,
    }, 
    'fruit3' : {
        "Name": "orange", 
        "Price": 2,
    }
}

exist = False
findPrice = input("Enter the name of the fruit").lower()
for i in fruits :
    if fruits[i]["Name"] == findPrice: 
        num2 = fruits[i]["Price"]
        print(f"The price of {findPrice} is {num2}.")
        exist = True

if exist == False :  
    print("Sorry, we don't have that fruit.")

    


# %%
