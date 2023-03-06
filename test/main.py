#1
def check_elements(tuple):
    element = tuple[0]
    check = True

    for i in tuple:
        if element != i:
            check = False
            break

    if (check == True):
        print("Equal")
    else:
        print("Not equal")


tuple = ['Boyan', 'Boyan', 'Boyan']
check_elements(tuple)
# 2
class Product:
    def __init__(self, supplement):
        self.supplement = supplement

    def show_my_drink(self):
        if(self.supplement == ""):
            print("Обикновена сода")
        else:
            print("Limonada and" + self.supplement)

