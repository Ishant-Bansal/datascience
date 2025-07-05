def new_acc():
    acc_no = acc_no_gen()
    name = input("Enter Account Holder Name : ")
    mob = input("Enter Your Phone Number : ")
    pin = int(input("Enter your 4 digit Account Privacy Pin : "))
    balance = 0
    user_data = [acc_no, name, mob, pin, balance]
    
    with open("C://Users//ishan//OneDrive//Desktop//upflair//projects//account.txt", "a") as file:
        file.write(str(user_data) + "\n")  # List ko string me convert karke save kiya
    
    print("Account Created Successfully!")
    print(f"Your Account Number is: {acc_no}")

def view_acc():
    acc_no_input = input("Enter your Account Number : ").strip()
    pin_input = input("Enter your 4 digit pin : ").strip()
    found = False

    with open("C://Users//ishan//OneDrive//Desktop//upflair//projects//account.txt", "r") as file:
        for line in file:
            line = line.strip().replace('[','').replace(']','')
            parts = line.split(',')

            acc_no = parts[0].strip().strip("'")
            name   = parts[1].strip().strip("'")
            mob    = parts[2].strip().strip("'")
            pin    = parts[3].strip()
            balance = float(parts[4].strip())

            if acc_no_input == acc_no and pin_input == pin:
                print("\n--- YOUR ACCOUNT DETAIL ---")
                print(f" Account Holder Name : {name}")
                print(f" Phone Number        : {mob}")
                print(f" Account Number      : {acc_no}")
                print(f" Privacy Pin         : {pin}")
                print(f" Balance             : ₹{balance}")
                found = True
                break

    if not found:
        print("Invalid Account Number Or PIN")

def deposit():
    acc_no_input = input("Enter your Account Number : ").strip()
    pin_input = input("Enter your 4 digit pin : ").strip()
    found = False
    updated_lines = []

    with open("C://Users//ishan//OneDrive//Desktop//upflair//projects//account.txt", "r") as file:
        for line in file:
            line = line.strip().replace('[','').replace(']','')
            parts = line.split(',')

            acc_no = parts[0].strip().strip("'")
            name   = parts[1].strip().strip("'")
            mob    = parts[2].strip().strip("'")
            pin    = parts[3].strip()
            balance = float(parts[4].strip())

            if acc_no_input == acc_no and pin_input == pin:
                print("Your Current Balance : ",balance)
                dep = float(input("How Much Money Do You Want Deposit :  "))
                new_balance = balance+dep

                print("Money Deposit Successfully...")
                new_data = f"['{acc_no}', '{name}', '{mob}', {pin}, {new_balance}]"      
                found = True
            else:
                new_data = line  # Keep unchanged

            updated_lines.append(new_data)
    if found:
        # Overwrite entire file with updated data
        with open("C://Users//ishan//OneDrive//Desktop//upflair//projects//account.txt", "w") as file:
            for line in updated_lines:
                file.write(line + "\n")
    else:
        print("Invalid Account Number Or PIN")
def withdraw():
    acc_no_input = input("Enter your Account Number : ").strip()
    pin_input = input("Enter your 4 digit pin : ").strip()
    found = False
    updated_lines = []

    with open("C://Users//ishan//OneDrive//Desktop//upflair//projects//account.txt", "r") as file:
        for line in file:
            line = line.strip().replace('[','').replace(']','')
            parts = line.split(',')

            acc_no = parts[0].strip().strip("'")
            name   = parts[1].strip().strip("'")
            mob    = parts[2].strip().strip("'")
            pin    = parts[3].strip()
            balance = float(parts[4].strip())

            if acc_no_input == acc_no and pin_input == pin:
                print("Your Current Balance : ",balance)
                if balance<0:
                    print("Insufficient balance!!!...")
                else:
                    wid = float(input("How Much Money Do You Want Withdraw :  "))
                    if wid<=balance: 
                        new_balance = balance-wid
                        print("Money withdraw Successfully...")
                        print(f"Remain balance : {new_balance}")
                        new_data = f"['{acc_no}', '{name}', '{mob}', {pin}, {new_balance}]"  
                    else:
                        ("Insufficient balance!!!...")    
                    found = True
            else:
                new_data = line  # Keep unchanged

            updated_lines.append(new_data)
    if found:
        # Overwrite entire file with updated data
        with open("C://Users//ishan//OneDrive//Desktop//upflair//projects//account.txt", "w") as file:
            for line in updated_lines:
                file.write(line + "\n")
    else:
        print("Invalid Account Number Or PIN")
def transaction():
    d = 0
    
def acc_no_gen():
    try:
        with open("C://Users//ishan//OneDrive//Desktop//upflair//projects//account.txt", "r") as file:
            lines = file.readlines()
            if not lines:
                return "1001"  # First account
            last_line = lines[-1].strip()  # Last line
            last_line = last_line.replace('[', '').replace(']', '')
            parts = last_line.split(',')
            last_acc_no = int(parts[0].strip().strip("'"))  # Extract and clean acc no
            return str(last_acc_no + 1) 
    except FileNotFoundError:
        return "1001"  # If file doesn't exist, start from 1001


def main():
    x= 0
    while x==0:
        print("--------ATM INTERFACE--------")
        print("Open New Account press 1 : ")
        print("View Account Detail press 2 : ")
        print("Deposit money press 3 : ")
        print("Withdraw Money press 4 : ")
        choice = int(input("Enter your choice (1 to 4) : "))
        if choice == 1:
            new_acc()
        elif choice == 2:
            view_acc()
        elif choice == 3:
            deposit()
        elif choice == 5:
            transaction()
        elif choice == 4:
            withdraw()
        else:
            print("invalid choice!!!...")
        x=0
main()
