class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def modify(self, brand=None, model=None, price=None):
        if brand: self.brand = brand
        if model: self.model = model
        if price: self.price = price

    def __str__(self):
        return f"Brand: {self.brand}, Model: {self.model}, Price: {self.price}"


def create_phone(phone_list):
    phone_list.append(Phone(input("Brand: "), input("Model: "), input("Price: ")))
    print("Phone added!\n")


def modify_phone(phone_list):
    if not phone_list: return print("No phones to modify.\n")
    for i, phone in enumerate(phone_list): print(f"{i+1}: {phone}")
    try:
        phone = phone_list[int(input("Select phone number: "))-1]
        phone.modify(input("New Brand: ") or None, input("New Model: ") or None, input("New Price: ") or None)
        print("Phone modified!\n")
    except: print("Invalid input.\n")


def delete_phone(phone_list):
    if not phone_list: return print("No phones to delete.\n")
    for i, phone in enumerate(phone_list): print(f"{i+1}: {phone}")
    try:
        print(f"Deleted {phone_list.pop(int(input("Select phone number: "))-1)}\n")
    except: print("Invalid input.\n")


def main():
    phone_list = []
    while True:
        print("1. Add Phone\n2. Modify Phone\n3. Delete Phone\n4. View Phones\n5. Exit")
        choice = input("Select: ")
        if choice == '1': create_phone(phone_list)
        elif choice == '2': modify_phone(phone_list)
        elif choice == '3': delete_phone(phone_list)
        elif choice == '4': print(*phone_list, sep="\n", end="\n\n") if phone_list else print("No phones.\n")
        elif choice == '5': break
        else: print("Invalid choice.\n")


if __name__ == "__main__":
    main()
