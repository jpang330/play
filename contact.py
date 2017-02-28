

class Contact(object):
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.mobile_number = ""
        self.work_number = ""
        self.email = ""

    def send_text(self):
        if self.mobile_number == "":
            print "Please enter a mobile number!"
        else:
        
            print "To: %s - Hello! How are you?" % (self.mobile_number)

def main():


    number = 1
    contacts_list = []
    for i in range(3):
        first_name = raw_input("Enter your first name. ")
        last_name = raw_input("Enter your last name. ")        
        contact_object = Contact(first_name, last_name)
        contact_object.mobile_number = raw_input("What is your phone number? ")
        contact_object.work_number = raw_input("What is your work number? ")
        contact_object.email = raw_input("What is your email? ")
        contacts_list.append(contact_object)
        number += 1
    print contacts_list
    for contact_object in contacts_list:
        print contact_object.first_name, contact_object.last_name, contact_object.mobile_number, contact_object.work_number, contact_object.email
        contact_object.send_text()
main()

    
