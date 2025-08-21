from datetime import date
import re
class Product:
    'Python OOPs applied'
    def __init__(self,productid=None,productname=None,unitprice=None,categoryid=None,manufacturedate=None,is_active='Y'):
        self.__product_id = productid
        self.__productname = None #vlidating productname
        self.__unitprice = unitprice
        self.__category_id = categoryid
        self.__manufacture_date = manufacturedate if manufacturedate else date.today()
        self.__is_active = is_active
        # -------
        # getter and setters
        # ----------
    def get_productid(self):
        return self.__product_id 
    def set_product_id(self,productid):
        self.__product_id = productid

    def get_productname(self):
        return self.__productname
    def set_product_name(self,productname):
        'validate product name before setting (2-30 alphabet/underscore)'
        pattern = re.compile(r"[A-Za-z_]{2,30}$")

        while True:
            if pattern.match(productname):
                self.__productname = productname
                break
            else:
                print("\t\t Invalid product name, must have only alphabets &_!!!!")
                produntname = input('\t\tEnter Product Name again: ')
    def get_unitprice(self):
        return self.__unitprice
    def set_unitprice(self,unitprice):
        self.__unitprice = unitprice

    def get_categoryid(self):
        return self.__category_id
    def set_categoryid(self,categoryid):
        self.__category_id = categoryid

    def get_manufacture_date(self):
        return self.__manufacture_date
    def set_manufacture_date(self,manufacturedate):
        if isinstance(manufacturedate,date):
            self.__manufacture_date = manufacturedate
        else:
            raise ValueError("manufacture date must be date object")

    def get_is_active(self):
        return self.__is_active
    def set_is_active(self,is_active):
        self.__is_active = is_active

    # override __str__
    def __str__(self):
        return f'Produnt ID :{self.__product_id:<10},  Category ID :{self.__category_id:<10}, Unit price :{self.__unitprice:<10}, Manufacture Date :{self.__manufacture_date}, Is Active :{self.__is_active}'
    
product = Product(1,'laptop',45.5,1)
print(product.__category_id)