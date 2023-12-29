import string


def validate_return_odd_number(input_data: str):
    data = input_data.split(",")
    output = []
    for record in data:
        if record.isdigit():
            if int(record) % 2 != 0:
                output.insert(0, record)

        else:
            print(f"Record {record} is not valid input")

    return output


def get_input():
    input_data = input("Enter inputs separated by Comma (,) :")
    print(validate_return_odd_number(input_data))


get_input()
