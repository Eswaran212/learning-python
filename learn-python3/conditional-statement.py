def register(f_name, l_name, e_age):
    print("\n\n******** Registration Starting *****")
    if int(e_age) < 30:
        print(f"Hello Mr/Mrs {f_name} {l_name}..\n your age is {e_age}\n You are Eligible")
    else:
        print(f"Hello Mr/Mrs {f_name} {l_name}..\n your age is {e_age}\n Sorry... You are not Eligible")
    print("******** Registration completed *****")


def get_details():
    first_name = input("\n\nEnter your first name\n\r")
    last_name = input("Enter your last name \n\r")
    age = input("Enter your Age \n\r")
    register(first_name, last_name, age)


get_details()
