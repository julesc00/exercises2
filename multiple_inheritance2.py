
# Base class
class PanCard(object):
    def __init__(self):
        self.pan_num = "Pan000001"
        print("From PanCard class")


# Base class
class AdharCard(object):
    def __init__(self):
        self.adhar_num = "5000000000000001"
        print("From AdharCard class")


# Driver class
class BankAccountOpening(PanCard, AdharCard):
    def __init__(self):
        # Calling constructors of Base class1
        PanCard.__init__(self)
        # Calling constructors of Base class2
        AdharCard.__init__(self)
        print("From BankAccountOpening class")

    def customer_details(self):
        return f"Pan_number: {self.pan_num}\nAdhar_number: {self.adhar_num}"


bank_obj = BankAccountOpening()
print(bank_obj.customer_details())
