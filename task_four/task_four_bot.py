def add_contact(contacts, name, phone):
    contacts[name] = phone
    return "Contact added."

def change_contact(contacts, name, new_phone):
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    return "Contact not found."

def show_phone(contacts, name):
    if name in contacts:
        return contacts[name]
    return "Contact not found."

def show_all(contacts):
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    return "No contacts found."

def parse_input(user_input):
    parts = user_input.strip().split(maxsplit=2)
    command = parts[0].lower()
    args = parts[1:]
    return command, args

def main():
    contacts = {}
    while True:
        user_input = input("Enter command: ")
        command, args = parse_input(user_input)

        if command == "hello":
            print("How can I help you?")
        elif command == "add":
            if len(args) == 2:
                name, phone = args
                print(add_contact(contacts, name, phone))
            else:
                print("Invalid command format. Use: add [name] [phone]")
        elif command == "change":
            if len(args) == 2:
                name, new_phone = args
                print(change_contact(contacts, name, new_phone))
            else:
                print("Invalid command format. Use: change [name] [new_phone]")
        elif command == "phone":
            if len(args) == 1:
                name = args[0]
                print(show_phone(contacts, name))
            else:
                print("Invalid command format. Use: phone [name]")
        elif command == "all":
            print(show_all(contacts))
        elif command in ("exit", "close"):
            print("Good bye!")
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

