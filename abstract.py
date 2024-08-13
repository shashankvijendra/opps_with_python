""" Mandatory to use the abstractmethod function in child class 
with Any logic """

from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    
    @abstractmethod
    def process_payment(self, amount):
        pass
    
    def display_processor_name(self):
        pass


class CreditCardPayment(PaymentProcessor):
    
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")
        # Additional logic for credit card payment processing
        
    def display_processor_name(self):
        print("Displaying Credit Card Processor Name")

class PayPalPayment(PaymentProcessor):
    
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")
        # Additional logic for PayPal payment processing
        
    def display_processor_name(self):
        print("Displaying PayPal Processor Name")


cc_payment = CreditCardPayment()
paypal_payment = PayPalPayment()

cc_payment.process_payment(100)
paypal_payment.process_payment(200)

cc_payment.display_processor_name()
paypal_payment.display_processor_name()
