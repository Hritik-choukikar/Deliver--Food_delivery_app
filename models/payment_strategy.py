from abc import ABC, abstractmethod

class PaymentStragey(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class UPIPaymentStragey(PaymentStragey):
    def __init__(self, upi_id):
        self.upi_id = upi_id

    def pay(self, amount):
        print(f"Amount Paid of ₹{amount} through UPI-ID {self.upi_id}")
