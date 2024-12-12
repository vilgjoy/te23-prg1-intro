# adult = 18
# user_age = input("Whats your age?: ")

# while True:
#     try:
#         if int(user_age) >= adult:
#             print("Ok your age is:", user_age)
#             break
#         else:
#             print("You are below the age limit")
#             break
#     except ValueError:
#         print("Your answer must be a numeric value, for example 19.")

def user_int():
    while True:
        try:
            user_input = int(input("Provide an integer: "))
            print("Your integer is", user_input)
            return user_input

        except ValueError:
            print("Your answer must be a numeric value, for example 19.")