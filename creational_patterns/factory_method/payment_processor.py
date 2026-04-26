from abc import ABC, abstractmethod

# Product
class PaymentProcessor(ABC):
    @abstractmethod
    def process(self, amount):
        pass

# Concrete Products
class CreditCardProcessor(PaymentProcessor):
    def process(self, amount):
        return f"Processed {amount} via Credit Card"

class PayPalProcessor(PaymentProcessor):
    def process(self, amount):
        return f"Processed {amount} via PayPal"

# Creator
class PaymentFactory(ABC):
    @abstractmethod
    def create_processor(self):
        pass

# Concrete Creators
class CreditCardFactory(PaymentFactory):
    def create_processor(self):
        return CreditCardProcessor()

class PayPalFactory(PaymentFactory):
    def create_processor(self):
        return PayPalProcessor()