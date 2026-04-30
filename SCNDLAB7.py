import pytest
# def multiply(a, b):  
#     return a * b 

# def addition(a,b):
#     return a+b

# def divide(a,b):
#     return a/b

# def negative_multiplication(a,b):
#     return a * b

# def test_negativemultiply():  
#     assert negative_multiplication(-4, 5) == -20   
#     print("Negative Multiplication tests passed!")

# def test_addition():
#     assert addition(10,10)==20
#     print("Addition test passed")

# def test_multiply():  
#     assert multiply(2, 3) == 6   
#     print("Addition Multiplication tests passed!")

# def test_zerodivision():
#     assert pytest.raises(ZeroDivisionError)

# print( "Multiply: ",multiply(2,3))
# test_multiply()
# print("Addition:", addition(10,10))
# test_addition()
# print("Negative Multiplication:",negative_multiplication(-4,5))
# test_negativemultiply()
# print("Zero Division",divide(5,0))
# test_zerodivision()





#Q3
# def userage(age):
#     age = int(age)
#     return 18 if age >= 18 else age

# def test_age18():
#     assert userage(18)==18
# def test_age17():
#     assert userage(17)==17

# def test_age19():
#     assert userage(19)==19
    


# age1=input("Enter Your age: ")
# print("Test Passed: ",userage(age1))
# try:
#     test_age18()
#     print("Assertion Passed")
# except AssertionError:
#     print("Assertion Failed")

# age2=input("Enter Your age: ")
# print("Test Failed: ",userage(age2))
# try:
#     test_age17()
#     print("Assertion Passed")
# except AssertionError:
#     print("Assertion Failed")

# age3=input("Enter Your age: ")
# print("Test Passed: ",userage(age3))
# # try:
# #     test_age19()
# #     print("Assertion Passed")
# # except AssertionError:
# #     print("Assertion Failed")
















#Q2


# def string_length(s):
#     return len(s)


# def test_regular_string():
#     assert string_length("hello") == 5

# def test_empty_string():
#     assert string_length("") == 0

# def test_string_with_spaces_and_special_characters():
#     assert string_length("hello @world!") == 13


# print("string_length('hello') =", string_length("hello"))
# test_regular_string()
# print("test_regular_string: Passed")


# print("string_length('') =", string_length(""))
# test_empty_string()
# print("test_empty_string: Passed")


# #     print("test_empty_string: Failed")

# print("string_length('hello @world!') =", string_length("hello @world!"))
# test_string_with_spaces_and_special_characters()
# print("test_string_with_spaces_and_special_characters: Passed")


# print()



def sort_list(numbers):
    return sorted(numbers)

# Tests for Task 4
def test_random_numbers():
    assert sort_list([7, 2, 9, 1, 5]) == [7, 2, 9, 1, 5]

def test_already_sorted_list():
    assert sort_list([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_mixed_negative_and_positive_numbers():
    assert sort_list([3, -1, 4, -5, 0]) == [-5, -1, 0, 3, 4]


print("Test Passed")
print(sort_list([1,2,5,7,9]))
test_already_sorted_list()
print("")
print("Test Passed")
print(sort_list([7, 2, 9, 1, 5]))
test_random_numbers()
print("")
print(sort_list([7, 2, 9, 1, 5]))
test_random_numbers([])

