"""
Implementing pg. 113 -

Incomplete.
"""

class Contract:

    def __init__(self, product, revenue, whenSigned):
        self.product = product
        self.revenue = revenue
        self.whenSigned = whenSigned
        self.revenueRecognitions = []

class RevenueRecognitions:

    def __init__(self, amount, date):
        self.amount = amount
        self.date = date

class Product:

    def __init__(self, productType):
        self.productType = productType

class Money:

    @staticmethod
    def split(amount, ways):
        # HACK: There are likely subtle bugs in this code.
        cents = int(round(amount * 100))
        lowAmount = cents / ways
        highAmount = lowAmount + 1
        remainder = cents % ways
        print cents, remainder
        splits = [highAmount / 100.0 for i in xrange(remainder)] + \
                     [lowAmount / 100.0 for i in xrange(ways - remainder)]
        return splits

class RecognitionService:

    def RecognizedRevenue(self, contract, as_of):
        return 0

    def CalculateRevenueRecognitions(self, contract):
        if contract.productType == "word_processor":
            splits = Money.split(contract.revenue, 3)
            contract.revenueRecognitions.append(splits[0], )
        elif contract.productType == "database":
            pass
        elif contract.productType == "spreadsheet":
            pass
        else:
            raise "Missing productType"
