class Payment:
    def pay(self):
        print("Paid")

class GooglePay(Payment):
    def pay(self):
        print("Paid using  Gpay")

class PhonePe(Payment):
    def pay(self):
        print("Paid using  Phonepe")

class CreditCard(Payment):
    def pay(self):
        print("Paid using Card")

pmt = Payment()
Gpay = GooglePay()
PPe = PhonePe()
CC = CreditCard()
pmt.pay()
Gpay.pay()
PPe.pay()
CC.pay()