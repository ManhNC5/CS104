phonebook = {}

def add_contact(name, phone_number):
  # Add a new contact to the phonebook
  phonebook[name] = phone_number

def delete_contact(name):
  # Delete a contact from the phonebook
  if name in phonebook:
    del phonebook[name]
  else:
    print(f"{name} is not in the phonebook.")

def update_contact(name, phone_number):
  # Update a contact's phone number
  if name in phonebook:
    phonebook[name] = phone_number
  else:
    print(f"{name} is not in the phonebook.")
