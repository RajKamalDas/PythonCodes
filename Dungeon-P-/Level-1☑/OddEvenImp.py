n = input("Please Enter A Number To Be Checked: ")

try:
    n = float(n)
    if not n.is_integer():

        x = input(
            f"The Entered Value Is →NOT← A Whole Number. Do You Want To Continue With {int(n)}? (Y/N):"
        )
        if x.lower() != "y":
            raise Exception("You chose not to continue.")
            
    n = int(n)
    if not n % 2:
        print(f"{n} Is Even.")
    else:
        print(f"{n} Is Odd.")

except ValueError:
    print("Unfortunately The Entered Value Is →NOT← A Number.")

except Exception as e:
    print(e)  # This will print the custom message if the user chooses not to continue.
