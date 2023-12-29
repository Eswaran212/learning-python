def validate_input(e_age):
    print("\n\n******** Validation Starting *****")
    if e_age < 30:  # this will fail, if we receive not integer number
        print(f" your input is {e_age}\n You are validated")
    else:
        print(f"\n your input is {e_age}\n Sorry... Unable to validate")
    print("******** Validation completed *****")


def get_details():
    try:

        age = input("Enter your input \n\r")
        validate_input(int(age))

    except ValueError:
        print("Sorry... Incorrect input.. ")

get_details()