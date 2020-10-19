# #### 1ST PART ####

# products_dict = {}

# with open("items.txt") as products_list:
#     for item in products_list:
#         (key, val) = item.strip().split("-")
#         products_dict[key] = val

# isFinshed = False
# products_sum = 0
# purchases_history = open("purchases.txt","a")
# while not isFinshed :

#     user_choice = input("Please enter a product : \n")
#     print("For ending please type `end`")

#     if user_choice == "end":
#         isFinshed=True
#     elif user_choice in products_dict:
#         products_sum+=int(products_dict[user_choice])
#         purchases_history.write(f"{user_choice} \n")
#     else:
#         print("Sorry but your product is not in our list")
     

# print(f"Your total purchases is {products_sum} $")
# purchases_history.write(f"total : {products_sum} \n")
# purchases_history.write("******************")
# purchases_history.close()




# user_review =  input("Please type `rev` to give a feedback for our supermarket so that we can improve our service next time \n")

# if user_review == "rev":

#     review_action = input("Please choose one of the actions : 1) Propose new items 2) Submit a comment 3) Rate the supermarket out of 5 \n" )

#     reviews = open("reviews.txt","a")
    
#     if review_action == "1":
#        user_propose = input("Please propose new items so that we can add it to our list \n")
#        reviews.write(f"Our user want to add {user_propose} to the list \n")

#     elif review_action == "2":
#         user_comment = input("Please leave us a comment \n")
#         reviews.write(f"Following comment has been made by the user : {user_comment} \n")
#     elif review_action =="3":
#         user_rate = input("Please rate our supermarket out of 5 \n")
#         reviews.write(f"Our user left a rate of {user_rate} out of 5 \n")

#     reviews.close()
#     print("Thank you for your time . Have a wonderful Day !")



#### 2ND PART ####
