# class UserModel:
#     def __init__(self):
#         self.users=[]

#     def add_users(self,user_name):
#         """Add User"""
#         self.users.append(user_name)

#     def delete_users(self,username):
#         """Delete User"""
#         if username in self.users:
#             self.users.remove(username)
#         else:
#             print("User Not found")

#     def get_all_user(self):
#         """Return all users"""
#         return self.users
    


# class UserView:
#     def display_user(self,users):
#         """Display Users"""
#         if not users:
#             print("No users")
#         else:
#             print("Users List:")
#             for user in users:
#                 print(user)


#     def get_user_input(self):
#         """Get input from user"""
#         print("Options: ")
#         print("1: Adduser ")
#         print("2: Delete User ")
#         print("3: Show User ")
#         print("4: Exit ")
#         return input("Choose Option: ")


# class UserController:
#     def __init__(self, model, view):
#         self.model = model
#         self.view = view
#     def run(self):
#         while True:
#             choice = self.view.get_user_input()

#             if choice =="1":
#                 user_name = input("Enter User name: ")
#                 self.model.add_users(user_name)

#             elif choice =="2":
#                 user_name = input("Enter User name: ")
#                 self.model.delete_users(user_name)

#             elif choice =="3":
#                 users = self.model.get_all_user()
#                 self.view.display_user(users)

#             else:
#                 print("Invalid Option")




# model = UserModel()
# view = UserView()
# controller=UserController(model, view)

# controller.run()













# class UserModelLib:
#     def __init__(self):
#         self.books=[]

#     def add_users(self,book):
#         """Add User"""
#         self.books.append(book)

#     def delete_users(self, book):
#         """Delete User"""
#         if book in self.books:
#             self.users.remove(book)
#         else:
#             print("User Not found")

#     def get_all_book(self):
#         """Return all users"""
#         return self.books
    
# class UserModelStd:
#     def __init__(self, model):
#         self.model=model
#     def get_all_books(self):
#         """Return all users"""
#         return self.model.get_all_book()
#     def search(self):
#         searchbook = input("Search Book")
#         if searchbook in self.model.books:
#             return searchbook
#         else:
#             print("Not found")



# class UserLibView:
#     def display_user(self,users):
#         """Display Users"""
#         if not users:
#             print("No users")
#         else:
#             print("Users List:")
#             for user in users:
#                 print(user)


#     def get_user_input(self):
#         """Get input from user"""
#         print("Options: ")
#         print("1: Add Book ")
#         print("2: Delete Book ")
#         print("3: Show Book ")
#         print("4: Exit ")
#         return input("Choose Option: ")

# class UserStdView:
#     def display_user(self,users):
#         """Display Users"""
#         if not users:
#             print("No users")
#         else:
#             print("Users List:")
#             for user in users:
#                 print(user)





# class UserController:
#     def __init__(self, model, view):
#         self.model = model
#         self.view = view
#     def run(self):
#         while True:
#             choice = self.view.get_user_input()

#             if choice =="1":
#                 user_name = input("Enter User name: ")
#                 self.model.add_users(user_name)

#             elif choice =="2":
#                 user_name = input("Enter User name: ")
#                 self.model.delete_users(user_name)

#             elif choice =="3":
#                 users = self.model.get_all_user()
#                 self.view.display_user(users)

#             else:
#                 print("Invalid Option")




# Libmodel = UserModelLib()
# stdmodel = UserModelStd()

# Libview = UserLibView()
# stdview = UserStdView()

# controller=UserController(model, view)

# controller.run()





















class LibraryModel:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, isbn):
        book = {"title": title, "author": author, "isbn": isbn}
        self.books.append(book)

    def delete_book(self, title):
        for book in self.books:
            if book["title"] == title:
                self.books.remove(book)
                print("Book removed successfully")
                return
        print("Book not found")

    def get_all_books(self):
        return self.books

    def search_book(self, keyword):
        results = []
        for book in self.books:
            if keyword.lower() in book["title"].lower() or keyword.lower() in book["author"].lower():
                results.append(book)
        return results



class LibrarianView:

    def menu(self):
        print("\n--- Librarian Menu ---")
        print("1 Add Book")
        print("2 Remove Book")
        print("3 View Books")
        print("4 Exit")

        return input("Choose option: ")

    def display_books(self, books):

        if not books:
            print("No books available")

        else:
            print("\nAvailable Books:")
            for book in books:
                print(book["title"], "-", book["author"], "-", book["isbn"])


class StudentView:

    def menu(self):
        print("\n--- Student Menu ---")
        print("1 View Books")
        print("2 Search Book")
        print("3 Exit")

        return input("Choose option: ")

    def display_books(self, books):

        if not books:
            print("No books available")

        else:
            for book in books:
                print(book["title"], "-", book["author"], "-", book["isbn"])

class LibrarianController:

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):

        while True:

            choice = self.view.menu()

            if choice == "1":

                title = input("Enter Title: ")
                author = input("Enter Author: ")
                isbn = input("Enter ISBN: ")

                self.model.add_book(title, author, isbn)

            elif choice == "2":

                title = input("Enter Book Title to Remove: ")
                self.model.delete_book(title)

            elif choice == "3":

                books = self.model.get_all_books()
                self.view.display_books(books)

            elif choice == "4":
                break

            else:
                print("Invalid Option")


class StudentController:

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):

        while True:

            choice = self.view.menu()

            if choice == "1":

                books = self.model.get_all_books()
                self.view.display_books(books)

            elif choice == "2":

                keyword = input("Enter Title or Author: ")
                results = self.model.search_book(keyword)

                self.view.display_books(results)

            elif choice == "3":
                break

            else:
                print("Invalid Option")



model = LibraryModel()

lib_view = LibrarianView()
std_view = StudentView()

while True:

    print("\n1 Librarian")
    print("2 Student")
    print("3 Exit")

    role = input("Select role: ")

    if role == "1":
        controller = LibrarianController(model, lib_view)
        controller.run()

    elif role == "2":
        controller = StudentController(model, std_view)
        controller.run()

    elif role == "3":
        break

    else:
        print("Invalid choice")