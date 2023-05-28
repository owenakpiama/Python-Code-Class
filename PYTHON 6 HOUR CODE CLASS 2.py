numbers = [5,2,1,5,7,4]
numbers.sort()
numbers.reverse() #list methods 
print(numbers)

numbers = (1,2,3)
print(numbers[0]) #tuples

coordinates = [1,2,3]
x,y,z = coordinates #unpacking
print(x * y)

customer = {
    "name" : "John Smith",
    "age":30 ,
    "is_verified": True #dictoniares 
}
customer["birthdate"] = "Jan 1 1980"
print(customer["birthdate"])

 
 
def greet_user():
    print('Hi there !')
    print('Welcome aboard')


    print("start") #functions
    greet_user()
    print("Finish")


    def greet_user(first_name , last_name):
        print(f'Hi {first_name} {last_name}!') #parameters
        print('Welcome aboard')


    print("Start")
    greet_user("John ,Smith")
    print("Finish")

