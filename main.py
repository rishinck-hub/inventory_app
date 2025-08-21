from db.db_connection import DBConnection
from lib.PoductManagementLib import ProductManagementLib

def main():
    while True:
        print('\n=============Product Management Menu===============')
        print('1.Add Product')
        print('2.Display All Product')
        print('3.Update Product')
        print('4.Searcg Product by ID')
        print('5.Disable Product')
        print('6.Apply GST')
        print('7.Exit')
        choice = input('Enter your choice :')
        if choice =='1':
            ProductManagementLib.add_product()
        elif choice =='3':
            ProductManagementLib.update_product()
        elif choice =='2':
            ProductManagementLib.display_all()
        elif choice =='5':
            ProductManagementLib.disable_product()
        elif choice =='6':
            ProductManagementLib.apply_gst_to_product()
        elif choice =='7':
            break
        else:
            print('Enter a valid choice')
if __name__ == "__main__":
    main()