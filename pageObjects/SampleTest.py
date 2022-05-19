class Mydetails:
    __details = ''     #protected


    def __init__(self,details={}):  # constructor
        self.__details = details


    def set_details(self,details):        # function
        self.__details = details

    def get_details(self):
        return self.__details

    def toString(self):
        return 'Welcome {}'.format(self.__details)


new_details = ['xyz','klm','nop']
pdetails = Mydetails()
pdetails.set_details(new_details)
plist = pdetails.get_details()
print(type(plist))
