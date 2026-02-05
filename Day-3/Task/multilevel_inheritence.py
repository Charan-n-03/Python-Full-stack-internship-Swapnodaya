class Product:
    def __init__(self,product_name,price):
        self.product_name=product_name
        self.price=price

    def dispaly_product(self):
        print("Product:",self.product_name)
        print("Price:",self.price)

class ElectronicProduct(Product):
    def __init__(self,brand,warranty,product_name,price):
        super().__init__(product_name,price)
        self.brand=brand
        self.warranty=warranty

    def display_electronic_product(self):
        print("Product:",self.product_name)
        print("Brand:",self.brand)
        print("Price:",self.price)
        print("Warranty:",self.warranty)
class MobilePhone(ElectronicProduct):
    def __init__(self,product_name,brand,price,ram,storage,warranty):
        super().__init__(brand,warranty,product_name,price)
        self.ram=ram
        self.storage=storage

    def display_mobile_details(self):
        print("Product:",self.product_name)
        print("Brand:",self.brand)
        print("Price:",self.price)
        print("RAM:",self.ram)
        print("Storage:",self.storage)
        print("Warranty:",self.warranty)

samsung = MobilePhone("Smartphone","SAMSUNG","1Lakh","12GB","256GB","2Years")
samsung.display_mobile_details()

