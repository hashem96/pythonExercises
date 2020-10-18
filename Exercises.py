### Strings ###

#Ask the user for his name, 
# and then print a greeting message


user_name = input("Please enter your name:\n")

print(f"Welcome back {user_name}")

#Ask two users for their names, and then tell 
# them who got the longest name.

first_user = input("1st user , please enter your name:\n")
second_user = input("2nd user , please enter your name:\n")

if len(first_user) > len(second_user):
    print("1st User's name is longer")
else :
    print("2nd User's name is longer")


#Ask a user for his name, and if it starts with a vowel, 
# # greet him

user_name = input("Please enter your name:\n")

vowel = ["a","e","i","o","u"]

if user_name[0].lower() in vowel:

    print(f"Weclome Back {user_name}")
else:
    print("Welcome Back")


#Ask the user for his name, and tell him if 
# the last letter is a vowel or a consonant

user_name = input("Please enter your name:\n")


if user_name[-1].lower() in vowel :
    print("Your last letter in your name is a vowel")

else :
        print("Your last letter in your name is a consonant")


Ask the user for two numbers (one after the other) 
and then print their sum


first_num = input("Please enter your 1st number:\n")

second_num = input("Please enter your 2nd number:\n")

print("Your sum is" , int(first_num)+int(second_num))


Challenge the user to print the longest sentence without any “A”, 
if he achieves it, tell him how many letters
he wrote, else, print a fail message.

longest_sen  = input("Please enter your longest sentence:\n")

if "A" in longest_sen:
    print(f"You failed , you have {len(longest_sen)} letters in your sentence")
else:
    print("Congratulations , you did it")



Ask the user for his full name (example: “John Doe”), and check the validity of his answer:

The name should contain only letters.
The name should contain only one space.
The first letter of each name should be upper cased.



full_name = input("Please enter your full number:\n")


if full_name.isalpha():
    break
    print ("invalid name")



#Ask the user for a sentence, and then tell him how many words are in it.

user_sentence = input("Please enter your sentence:\n")

print(f"Your sentence contains {len(user_sentence.split())} words")






## For Loops ###


#Write a program that counts the number of element for a list, without the len function.

name=['Alex','Mike','Dylan','Yossi']
count=0

for element in name:
    count+=1

print(f"You have {count} names in your list")


#Write a program that print every name that starts by ‘a’
name = ['Alex','Mike','Dylan','Yossi']

for element in name:
    if element[0].lower() == "a":
        print (element)


#Write a Python program that prints all the numbers from 0 to 10 except 3 and 6.


for i in range(11):
    if (i == 3) or  (i== 6) :
        pass
    else:
        print (i)


#Use a for loop to print the numbers from 1 to 20, inclusive.

for i in range(1,21):
    print (i)


#Write a program that returns the index of the first occurrence of an item in a list.

random = ["A","C" , "B", "C" ,"B","A"]

print(random.index("B"))


#Write a little program that concatenate two lists together without using the + sign.
 
test_list1 = [1, 4, 5, 6, 5] 
test_list2 = [3, 5, 7, 2, 5] 

for i in test_list2 : 
    test_list1.append(i) 


print(test_list1)


Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.

multiples = []

for i in range(3, 31):
    # if equal to zero it is a multiple of 3
    if i % 3 == 0:  
        multiples.append(i)   

print(multiples)


#Write a program that insert an item at a defined index.


test_list = [1,2,3,5,6,8]
test_list.insert(2,"Hello")

print(test_list)


#You have two lists, current_players and new_players, use a while loop to transfer every player from new_players to current_players.

current_players = ['Mario', 'Luigi', 'Peach']
new_players = ['Blue Toad', 'Red Toad', 'Green Toad']

for i in new_players : 
    current_players.append(i) 

print(current_players)

#What is the output of the following?¶
x = ['ab', 'cd']
for i in x:
    i.upper()
    print(x)

# => Nothing will change as we print x without saving the effect of uppercase on i

#What is the output of the following?¶


x = ['ab', 'cd']
for i in x:
    x.append(i.upper())
    print(x)

# => We will uppercase every element of X and add it to the list itself  However this will go infinitely (Wont STOP)


#Given a list of integers and strings, put all the integers in one list, and all the strings in another one.


test_list = [1,2,"Hello", 3 , 4 ,"Hi"]
int_list = []
str_list = []


for i in test_list:

    if type(i) == int:
        int_list.append(i)
    elif type(i) == str:
        str_list.append(i)


print(int_list)
print(str_list)


##   While Loops    ###

Write a loop that prompts the user to enter a series of pizza toppings until they enter a ‘quit’ value.
As they enter each topping, print a message saying you’ll add that topping to their pizza .

pizza_topping = ""

while (pizza_topping != "quit") :
    pizza_topping = input("Please enter your topping:\n")
    print("This will be added on top of your pizza")
print("Thank you , your pizza will be ready in few minutes")


#Given a list, use a while loop to print out every elements from the end to the beginning.

my_list = ["a","b","c","d"]
count = 0

while count < len(my_list):
    print (my_list[count])
    count+=1


#Use a while loop to print every number from 5 to 100

count= 5

while count <101:
    print(count)
    count+=1


#Given a list, use a while loop to print out every element which his index is even. 

my_list = ["a","b","c","d"]

print(my_list[1::2])


#Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700.

final_list = []
count= 1500

while count < 2701:
    if (count  % 7 == 0) and (count % 5== 0):
        final_list.append(count)
        count+=1
print (final_list)


Count the number of spaces in a string.

count = 0

my_str = "Hello World , How are you ?"

for i in my_str:
  if (i==" "):
       count+=1

       
print(f"You have {count} spaces in your sentence")



#Count the number of words in a string. 



my_str = "Hello World , How are you ?"

strlength = len(my_str.split())

print(f"You have {strlength} words in your sentence")




## Dictionnaries ###


#Create a dict with your friends ages


my_dict= {"Ahmed" : 20 , "Mohmmad":21, "Adham" :22}



# Transform this dict:

# {0: 10, 1: 20}
# into this:

# {0: 10, 1: 20, 2: 30}



my_dict = {0: 10, 1: 20}

my_dict[2] = 30

print(my_dict)

#Write a Python program to get the maximum and minimum value in a dictionary.


a_dictionary = {"a": 1, "b": 2, "c": 3}

all_values = a_dictionary.values()
min_value=min(all_values)
max_value = max(all_values)


#Print every key and value of this dictionary using for loop, and then using while loop: 

products = {
"SMART WATCH": 550,
"PHONE" : 1000,
"PLAYSTATION": 500,
"LAPTOP" : 1550,
"MUSIC PLAYER" : 600,
"TABLET": 400
}


for key, value in products.items():
    print(key, value)



Write a Python program to remove duplicates values from Dictionary.



products = {
"SMART WATCH": 550,
"PHONE" : 1000,
"PLAYSTATION": 500,
"LAPTOP" : 1550,
"MUSIC PLAYER" : 600,
"TABLET": 400,
"TABLET": 600,
}

result = {}

for key,value in products.items():
    if value not in result.values():
        result[key] = value

print(result)


#Write a Python script to check if a given key already exists in a dictionary.


products = {
"SMART WATCH": 550,
"PHONE" : 1000,
"PLAYSTATION": 500,
"LAPTOP" : 1550,
"MUSIC PLAYER" : 600,
"TABLET": 400,
}


def is_key_present(x):
    if x in products:
        print('Key is present in the dictionary')
    else:
        print('Key is not present in the dictionary')

is_key_present("SMART WATCH")
is_key_present("IWATCH")


#Write a Python script to concatenate following dictionaries to create a new one.

dic1={1:10, 2:20} 
dic2={3:30, 4:40} 
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4)


#Use python to convert those two lists:


list1 = ['Rick', 'Donald', 'Mickey' , 'Mario']
list2 = ['Sanchez', 'Duck', 'Mouse', 'Kart']

res = {} 
for key in list1: 
    for value in list2: 
        res[key] = value 
        list2.remove(value) 
        break  
print(res)






