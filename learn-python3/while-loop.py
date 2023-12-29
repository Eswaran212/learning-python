def get_input(runner):
    while runner == "Y":
        start_index = int(input("enter the sequence start point : "))
        end_point = int(input("Enter the sequence end point : "))
        while start_index < end_point:
            print(f" current sequence {start_index}")
            start_index = start_index + 1
        runner = input("Do you want continue Y/N : ")


get_input("Y")
