# class DataAccessLayer:    
#      def __init__(self):       
#           self.students = []  # Simulating database with an array 

# def add_student(self, student):    
#     """Add a student record."""   
#     self.students.append(student) 

# def delete_student(self, student_name):       
#       """Delete a student by name."""      
#       self.students = [student for student in self.students if student['name'] != student_name]


# def get_all_students(self):       
#       """Return all student records."""     
#       return self.students 


# def update_student(self, student_name, updated_student):     
#         """Update student data."""     
#         for index, student in enumerate(self.students):        
#           if student['name'] == student_name: 
#                 self.students[index] = updated_student          
#                 return True      
#         return False 




# class ValidationLayer:  
#     @staticmethod   
#     def validate_age(age):    
#         """Validate if the age is a positive integer."""   
#         return isinstance(age, int) and age > 0

#     @staticmethod  
#     def validate_grade(grade):     
#             """Validate if the grade is a valid string (A, B, C, etc.)."""    
#             valid_grades = ['A', 'B', 'C', 'D', 'F']      
#             return grade in valid_grades 



#     @staticmethod   
#     def validate_student_data(name, age, grade):    
#         """Validate all student data before processing."""    
#         if not name:       
#                 return False, "Name cannot be empty!"     
#         if not ValidationLayer.validate_age(age):       
#                 return False, "Age must be a positive integer!"     
#         if not ValidationLayer.validate_grade(grade):       
#                 return False, "Invalid grade. Valid grades are A, B, C, D, F."     
#         return True, ""


# class BusinessLogicLayer:  
#        def __init__(self, data_access_layer, validation_layer):    
#             self.data_access_layer = data_access_layer    
#             self.validation_layer = validation_layer 



#        def add_student(self, name, age, grade):   
#             """Add a student after validating the data."""     
#             is_valid, error_message = self.validation_layer.validate_student_data(name, age, grade)     
#             if is_valid:         
#                  student = {'name': name, 'age': age, 'grade': grade}      
#                  self.data_access_layer.add_student(student)       
#                  return f"Student '{name}' added successfully!"    
#             else:        
#              return f"Error: {error_message}" 
            


#        def delete_student(self, name):   
#             """Delete a student from the records."""     
#             self.data_access_layer.delete_student(name)   
#             return f"Student '{name}' deleted."


#        def update_student(self, name, age, grade):    
#              """Update student data after validation."""     
#              is_valid, error_message = self.validation_layer.validate_student_data(name, age, grade)    
#              if is_valid:      
#                    updated_student = {'name': name, 'age': age, 'grade': grade}     
#                    success = self.data_access_layer.update_student(name, updated_student)     
#              if success:         
#                     return f"Student '{name}' updated successfully!"      
#              else:  
#                 return f"Error: Student '{name}' not found!"   
#             else:         
#                 return f"Error: {error_message}" 
 
#        def get_all_students(self):     
#             """Retrieve all students."""    
#             return self.data_access_layer.get_all_students() 
       



#        class PresentationLayer:     def __init__(self, business_logic_layer):         self.business_logic_layer = business_logic_layer 
 
#     def display_students(self, students):         """Display all student records."""         if not students:             print("No students found.")         else:             print("Student Records:")             for student in students:                 print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}") 
 
#     def get_user_input(self):         """Display options for the user to choose from."""         print("\nOptions:")         print("1. Add Student")         print("2. Delete Student")         print("3. Update Student")         print("4. Show All Students")         print("5. Exit")         return input("Choose an option: ") 
# Software Construction & Development  lab 
# Page | 28  
 
 
#     def run(self):         """Main method to interact with the user."""         while True:             choice = self.get_user_input()                          if choice == '1':                 name = input("Enter student name: ")                 age = int(input("Enter student age: "))                 grade = input("Enter student grade (A, B, C, D, F): ")                 result = self.business_logic_layer.add_student(name, age, grade)                 print(result) 
 
#             elif choice == '2':                 name = input("Enter student name to delete: ")                 result = self.business_logic_layer.delete_student(name)                 print(result) 
 
#             elif choice == '3':                 name = input("Enter student name to update: ")                 age = int(input("Enter new student age: "))                 grade = input("Enter new student grade (A, B, C, D, F): ")                 result = self.business_logic_layer.update_student(name, age, grade)                 print(result) 
 
#             elif choice == '4':                 students = self.business_logic_layer.get_all_students()                 self.display_students(students) 
 
#             elif choice == '5':                 print("Exiting the application.")                 break 
# Software Construction & Development  lab 
# Page | 29  
 
 
#             else:                 print("Invalid option. Please try again.") 
 
 
# # Instantiate the layers data_access_layer = DataAccessLayer()  # Data Access Layer validation_layer = ValidationLayer()  # Validation Layer business_logic_layer = BusinessLogicLayer(data_access_layer, validation_layer)  # Business Logic Layer presentation_layer = PresentationLayer(business_logic_layer)  # Presentation Layer 
 
# # Run the application presentation_layer.run() 





























# class DataAccessLayer:
#     def __init__(self):
#         self.students = [] 
#     def add_student(self, student):
#         self.students.append(student)

#     def delete_student(self, student_name):
#         self.students = [
#             student for student in self.students
#             if student['name'] != student_name
#         ]

#     def get_all_students(self):
#         return self.students

#     def update_student(self, student_name, updated_student):
#         for index, student in enumerate(self.students):
#             if student['name'] == student_name:
#                 self.students[index] = updated_student
#                 return True
#         return False

# class ValidationLayer:

#     @staticmethod
#     def validate_age(age):
#         return isinstance(age, int) and age > 0

#     @staticmethod
#     def validate_grade(grade):
#         valid_grades = ['A', 'B', 'C', 'D', 'F']
#         return grade in valid_grades

#     @staticmethod
#     def validate_student_data(name, age, grade):
#         if not name:
#             return False, "Name cannot be empty!"
#         if not ValidationLayer.validate_age(age):
#             return False, "Age must be a positive integer!"
#         if not ValidationLayer.validate_grade(grade):
#             return False, "Invalid grade (A, B, C, D, F only)."
#         return True, ""



# class BusinessLogicLayer:
#     def __init__(self, dal, validator):
#         self.dal = dal
#         self.validator = validator

#     def add_student(self, name, age, grade):
#         is_valid, error = self.validator.validate_student_data(name, age, grade)

#         if is_valid:
#             student = {'name': name, 'age': age, 'grade': grade}
#             self.dal.add_student(student)
#             return f"Student '{name}' added successfully!"
#         return f"Error: {error}"

#     def delete_student(self, name):
#         self.dal.delete_student(name)
#         return f"Student '{name}' deleted."

#     def update_student(self, name, age, grade):
#         is_valid, error = self.validator.validate_student_data(name, age, grade)

#         if is_valid:
#             updated_student = {'name': name, 'age': age, 'grade': grade}
#             success = self.dal.update_student(name, updated_student)

#             if success:
#                 return f"Student '{name}' updated successfully!"
#             else:
#                 return f"Error: Student '{name}' not found!"
#         return f"Error: {error}"

#     def get_all_students(self):
#         return self.dal.get_all_students()


# class PresentationLayer:
#     def __init__(self, bll):
#         self.bll = bll

#     def display_students(self, students):
#         if not students:
#             print("\nNo students found.")
#         else:
#             print("\n===== Student Records =====")
#             for student in students:
#                 print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

#     def menu(self):
#         print("\n===== MENU =====")
#         print("1. Add Student")
#         print("2. Delete Student")
#         print("3. Update Student")
#         print("4. Show All Students")
#         print("5. Exit")

#     def run(self):
#         while True:
#             self.menu()
#             choice = input("Enter choice: ")

#             if choice == '1':
#                 name = input("Enter name: ")
#                 try:
#                     age = int(input("Enter age: "))
#                 except:
#                     print("Invalid age input!")
#                     continue
#                 grade = input("Enter grade (A/B/C/D/F): ")

#                 print(self.bll.add_student(name, age, grade))

#             elif choice == '2':
#                 name = input("Enter name to delete: ")
#                 print(self.bll.delete_student(name))

#             elif choice == '3':
#                 name = input("Enter name to update: ")
#                 try:
#                     age = int(input("Enter new age: "))
#                 except:
#                     print("Invalid age input!")
#                     continue
#                 grade = input("Enter new grade: ")

#                 print(self.bll.update_student(name, age, grade))

#             elif choice == '4':
#                 students = self.bll.get_all_students()
#                 self.display_students(students)

#             elif choice == '5':
#                 print("Exiting system...")
#                 break

#             else:
#                 print("Invalid choice!")


# if __name__ == "__main__":
#     dal = DataAccessLayer()
#     validator = ValidationLayer()
#     bll = BusinessLogicLayer(dal, validator)
#     app = PresentationLayer(bll)

#     app.run()






















class DataAccessLayer:
    def __init__(self):
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def delete_patient(self, name):
        self.patients = [p for p in self.patients if p['name'] != name]

    def get_all_patients(self):
        return self.patients

    def find_patient(self, name):
        for p in self.patients:
            if p['name'] == name:
                return p
        return None

    def update_status(self, name, status):
        for p in self.patients:
            if p['name'] == name:
                p['status'] = status
                return True
        return False


class ValidationLayer:

    @staticmethod
    def validate_age(age):
        return isinstance(age, int) and age > 0

    @staticmethod
    def validate_patient(name, age, disease):
        if not name:
            return False, "Name required"
        if not ValidationLayer.validate_age(age):
            return False, "Invalid age"
        if not disease:
            return False, "Disease required"
        return True, ""



class BusinessLogicLayer:
    def __init__(self, dal, validator):
        self.dal = dal
        self.validator = validator

    # Receptionist
    def add_patient(self, name, age, disease):
        valid, msg = self.validator.validate_patient(name, age, disease)

        if valid:
            patient = {
                'name': name,
                'age': age,
                'disease': disease,
                'status': 'Under Treatment'
            }
            self.dal.add_patient(patient)
            return "Patient added successfully"
        return f"Error: {msg}"

    def remove_patient(self, name):
        self.dal.delete_patient(name)
        return "Patient removed"

    def view_all(self):
        return self.dal.get_all_patients()

    # Doctor
    def search_patient(self, name):
        return self.dal.find_patient(name)

    def update_status(self, name, status):
        success = self.dal.update_status(name, status)
        if success:
            return "Status updated"
        return "Patient not found"

    # Patient
    def view_record(self, name):
        return self.dal.find_patient(name)



class PresentationLayer:
    def __init__(self, bll):
        self.bll = bll

    def display(self, patients):
        if not patients:
            print("No records")
        else:
            for p in patients:
                print(f"{p['name']} | Age: {p['age']} | Disease: {p['disease']} | Status: {p['status']}")

    def run(self):
        while True:
            print("\n===== HOSPITAL SYSTEM =====")
            print("1. Receptionist")
            print("2. Doctor")
            print("3. Patient")
            print("4. Exit")

            role = input("Select role: ")

            # ================= Receptionist =================
            if role == '1':
                print("\n1. Add Patient\n2. Remove Patient\n3. View All")
                choice = input("Enter choice: ")

                if choice == '1':
                    name = input("Name: ")
                    age = int(input("Age: "))
                    disease = input("Disease: ")
                    print(self.bll.add_patient(name, age, disease))

                elif choice == '2':
                    name = input("Enter name: ")
                    print(self.bll.remove_patient(name))

                elif choice == '3':
                    self.display(self.bll.view_all())

            # ================= Doctor =================
            elif role == '2':
                print("\n1. Search Patient\n2. Update Status")
                choice = input("Enter choice: ")

                if choice == '1':
                    name = input("Enter name: ")
                    patient = self.bll.search_patient(name)
                    print(patient if patient else "Not found")

                elif choice == '2':
                    name = input("Enter name: ")
                    status = input("Enter status (Under Treatment/Recovered/Critical): ")
                    print(self.bll.update_status(name, status))

            # ================= Patient =================
            elif role == '3':
                name = input("Enter your name: ")
                patient = self.bll.view_record(name)

                if patient:
                    print("\nYour Record:")
                    print(patient)
                else:
                    print("Record not found")

            elif role == '4':
                print("Exiting...")
                break

            else:
                print("Invalid option")



if __name__ == "__main__":
    dal = DataAccessLayer()
    validator = ValidationLayer()
    bll = BusinessLogicLayer(dal, validator)
    app = PresentationLayer(bll)

    app.run()