# import math 

# try:
#     nums = input("Enter numbers sepreated  by spaces:") .split()
#     for n in nums:
#         number = float(n)
#         print("Square root of", number, "is", math.sqrt(number))

# except ValueError:
#     print("Invalid Input")




#Q#2
# name = input("Enter Name: ")

# try:
#     account_bal = int(input("Enter Account Balance: "))
#     withdrawal_amount = int(input("Enter Withdrawal Amount: "))
    
#     if withdrawal_amount > account_bal:
#         print("Invalid Amount: Insufficient funds.")
        
#     elif withdrawal_amount <= 0:
#         print("Invalid Amount: Please enter a value greater than zero.")
        
#     else:
#         account_bal -= withdrawal_amount
#         print("Transaction successful!")
#         print(account_bal)

# except ValueError:
#     print("Invalid Amount Type: Please enter numeric values only.")

# except Exception as e:
#     print(f"Unexpected error occurred: {e}")







# # Q#4




# class MissingUserIDError(Exception):
#     pass

# class BookNotFoundError(Exception):
#     pass

# class BorrowLimitExceededError(Exception):
#     pass

# class AccountSuspendedError(Exception):
#     pass

# class LibraryClosedError(Exception):
#     pass



# class DigitalLibrary:
#     def __init__(self):
        
#         self.available_books = ["Python", "Physics", "DP"]
        
#     def request_book(self, user_id, requested_book, books_borrowed, is_suspended, current_hour=None):
       
#         try:
            
#             if current_hour is None:
#                 current_hour = datetime.datetime.now().hour
                
            
#             if current_hour >= 8:
#                 raise LibraryClosedError("The digital library is closed for maintenance after 11:00 PM.")

            
#             if not user_id:
#                 raise MissingUserIDError("User ID cannot be missing or blank.")

#             if is_suspended:
#                 raise AccountSuspendedError("Access denied. Your account is currently suspended.")

#             if books_borrowed >= 5:
#                 raise BorrowLimitExceededError("You have reached the maximum limit of 5 borrowed books.")

#             if requested_book not in self.available_books:
#                 raise BookNotFoundError(f"The book '{requested_book}' is not in our database.")

#             print(f"Success! '{requested_book}' has been granted to User ID: {user_id}.")

#         except (MissingUserIDError, BookNotFoundError, BorrowLimitExceededError, 
#                 AccountSuspendedError, LibraryClosedError) as e:
#             print(f"[{type(e).__name__}] -> {e}")


# library = DigitalLibrary()



# library.request_book("", "Physics", 2, False)

# library.request_book("U123", "Harry Potter", 2, False)

# library.request_book("U124", "Physics", 5, False)

# library.request_book("U125", "DP", 1, True)

# library.request_book("U126", "Python ", 1, False, current_hour=23)

# library.request_book("U127", "Physics", 2, False, current_hour=14)



















try:
    file = open("marks.txt","r")
    content = file.read()

except FileNotFoundError:
    print("File not found")
finally:
    file.close() 