class USResident(Person):
    """ 
    A Person who resides in the US.
    """
    def __init__(self, name, status):
        """ 
        Initializes a Person object. A USResident object inherits 
        from Person and has one additional attribute:
        status: a string, one of "citizen", "legal_resident", "illegal_resident"
        Raises a ValueError if status is not one of those 3 strings
        """       
        Person.__init__(self,name)
        
        self.name=name
        self.status=status
        self.getStatus()
                
    def getStatus(self):
        """
        Returns the status
        """
        if self.status == "citizen" or self.status == "legal_resident" or self.status == "illegal_resident":
            return self.status
        
        raise ValueError