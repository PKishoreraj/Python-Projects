class parent():
    def __init__(self):
        print("This is a parent class")
    def companies(companies):
        if companies=="medical":
            print("brindavin or oneplus")
        elif companies=="IT ":
            print("Inforces or LNT")
        elif companies=="chemecal":
            print("Bio chem or CPL")
        else:
            print("Enter a valid compane")
    def final(companies):
        if companies=="medical":
            print("You can join either brindavin or oneplus")
        elif companies=="IT ":
            print("You can join either Inforces or LNT")
        elif companies=="chemecal":
            print("You can join either Bio chem or CPL")
class child1(parent):
    def __init__(self,companies):
        self.new_dish=dish
    def get_menu(self):
        parent.menu(self.new_dish)
class child2(parent):
    def __init__(self,companies):
        self.add_ons=add_ons
    def get_final_amount(self):
        parent.final_amount(self.new_dish,self.add_ons)
child1_object=child1("burger")
child1_object.get_menu
child2_object=child2("iced_amercano")
child2_object.get_final_amount