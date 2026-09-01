class PhoneBook:
    phone_directory = [] # stores contact information

    def __init__(self,name,phone_number):
        self.Name = name
        self.PhoneNo = phone_number
        PhoneBook.phone_directory.append(self) # self is nothing but an contact information
        
    def show_contact(self):
        return f"Name : {self.Name}, Phone Number : {self.PhoneNo}"
        # print(f"Name : {self.Name}, Phone Number : {self.PhoneNo}")

# if you want to get entire contact defails we need to use class method. It means it will show all the contacts. 

    @classmethod
    def show_all_contacts(cls):
        if len(cls.phone_directory) == 0:
            print("No contacts found in the phone book.")
        else:
            print("All the contacts from the phone book are : \n")
            for contact in cls.phone_directory:
                print(contact.show_contact())  
                
    @classmethod
    def search_contact(cls,search_name):
        for contact in cls.phone_directory:
            if contact.Name == search_name:  # can be changed to if contact.Name.lower() == search_name.lower(): to make it case insensitive
                return contact.PhoneNo
            
        return f"No contact found for {search_name}"
    
    @staticmethod
    def validate_phone_number(number):
        if len(number) >= 8 and number.isdigit():
            return True
        else:
            return False

n_contacts = int(input("How many contacts do you want to add in the phone book? : "))

for i in range(n_contacts):
    name = input("Enter the name of the contact " )
    phoneNo = input("Enter the phone number of the contact : ")
    if PhoneBook.validate_phone_number(phoneNo):
        PhoneBook(name,phoneNo)
    else:
        print(f"Invalid phone number for {name}. Phone number should be at least 8 digits long and can only contain digits. Contact not added.")
# For working of validate_phone_number() method, we need to pass the phone number as a string. Because isdigit() method is only applicable for string data type. like below :

phone1 = PhoneBook("Ayush","8460794821")
phone2 = PhoneBook("Karan","8456778891")
phone3 = PhoneBook("Thor","1234567890")

# print(PhoneBook.phone_directory) # it will print the list of contact information

print(phone1.show_contact()) # it will print the contact information of phone1  
print(phone2.show_contact()) # it will print the contact information of phone2

PhoneBook.show_all_contacts()

# search for contact by name:
# print(PhoneBook.search_contact("Ayush")) # if you write "ayush"(all lowercase), it will not find the contact because it is case sensitive. To solve thie problem, we can use Lowercase() method.

# print(PhoneBook.search_contact("Dragon"))