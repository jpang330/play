from contact import Contact


class Phone(object):
    """A simple Phone class to keep track of contacts"""

    def __init__(self, number, name, contacts=None):
        self.number = number
        self.name = name
        if contacts:
            self.contacts = contacts
        else:
            self.contacts = {}

    # The __repr__ method gives the class a print format that is meaningful to
    # humans, in this case we chose first and last name
    def __repr__(self):

        return self.name

    def add_contact(self, first_name, last_name, number):
        """Creates new Contact instance and adds the instance to contacts"""
        #add something to the dictionary, make a contact instance to hold on to that info
        #store them
        self.contacts[self._get_contact_key(first_name, last_name)] = Contact(first_name, last_name, number)
       

    def call(self, first_name):
        """Call a contact."""

        pass

    def text(self, first_name, message):
        """Send a contact a message."""

        pass

    def del_contact(self, first_name):
        """Remove a contact from phone"""
        self.contacts[self._get_contact_key(first_name, last_name)] 
        


    def _get_contact_key(self, first_name, last_name):
        """This is a private method. It's meant to be used only from within
        this class. We notate private attributes and methods by prepending with
        an underscore.
        """
        return first_name.lower() + " " + last_name.lower()

