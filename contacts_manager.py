from contact import Contact

def main():

    contacts_list = []
    first_name, last_name = new_contact.split(",")        
    contact_object = Contact(first_name, last_name)
    contact_object.mobile_number = raw_input("What is your phone number? ")
    contact_object.work_number = raw_input("What is your work number? ")
    contact_object.email = raw_input("What is your email? ")
    contacts_list.append(contact_object)

    print contacts_list

main()
