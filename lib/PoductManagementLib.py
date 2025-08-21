from dao.productDaolmple import PRoductDaoImplementation
from dao.AbstractProductDao import ProductDaoService
from models.product import Product
from datetime import datetime
class ProductManagementLib:
    'handle CRUD logic'
    dao_service: ProductDaoService = PRoductDaoImplementation()

    @staticmethod
    def display_all():
        products = ProductManagementLib.dao_service.display_all_products()
        for product in products:
            print(product)

    @staticmethod
    def add_product():
        product = Product()
        productname = input('Enter the product Name :')
        product.set_product_name(productname)
        unitprice = float(input('Enter the Unit price :'))
        product.set_unitprice(unitprice)
        categoryid = int(input('Enter the Category Id: '))
        product.set_categoryid(categoryid)
        m_date = input("Enter Manufacture Date(dd/MM/YYYY) : ")
        util_date = datetime.strptime(m_date, "%d/%m/%Y")
        conv_m_date = util_date.date()
        product.set_manufacture_date(conv_m_date)
        is_active = input('Product available ? (Y/N)')
        product.set_is_active(is_active)
        if ProductManagementLib.dao_service.insert_products(product):
            print('Inserted successfully...')
        else:
            print('something went wrong....')        
    
    @staticmethod
    def update_product():
        searchid = int(input('Enter the product ID: '))
        #create a method in DAO
        product = ProductManagementLib.dao_service.find_by_product_id(searchid)
        if not product:
            print('product not found')
            return
        print(product)
        confirm = input('Do you want to edit this data?(Y/N)')
        if confirm.lower() == 'y':
            product.set_product_name(input('Enter new product Name: '))
            product.set_unitprice(input('Enter New Unit Price: '))
            #pass the object to dao update
            if ProductManagementLib.dao_service.update_product(product,searchid):
                print('updated successfully....')
            else:
                print('something went wrong.....')
    @staticmethod
    def disable_product():
        searchid = int(input('Enter the product ID: '))
        #create a method in DAO
        product = ProductManagementLib.dao_service.find_by_product_id(searchid)
        if not product:
            print('product not found')
            return
        print(product)
        confirm = input('Do you want to disable this product?(Y/N)')
        if confirm.lower() == 'y':
            product.set_is_active('N')
            #pass the object to dao update
            if ProductManagementLib.dao_service.disable_product(product,searchid):
                print('disabled successfully....')
            else:
                print('something went wrong.....')

    @staticmethod
    def apply_gst_to_product():
        prodcct_id = int(input('Enter the product id to apply GST: '))
        gst_percent = float(input('Enter GST percentage to apply: '))
        if ProductManagementLib.dao_service.apply_gst(prodcct_id,gst_percent):
            print(f'GST of {gst_percent} applied to product ID: {prodcct_id}')
        else:
            print('Failed to apply GST!!!')
