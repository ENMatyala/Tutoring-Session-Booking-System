from creational_patterns.factory_method.payment_processor import (
    CreditCardFactory, PayPalFactory
)

def test_credit_card_payment():
    factory = CreditCardFactory()
    processor = factory.create_processor()
    result = processor.process(100)

    assert "Credit Card" in result


def test_paypal_payment():
    factory = PayPalFactory()
    processor = factory.create_processor()
    result = processor.process(200)

    assert "PayPal" in result
    
def test_invalid_payment_amount():
    factory = CreditCardFactory()
    processor = factory.create_processor()

    result = processor.process(0)
    assert "0" in result