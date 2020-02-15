import stocks


def test_calculateprofit():
    price_array = [2, 3, 5, 10, 22, 4, 2, 7]
    assert stocks.calculateprofit(price_array) == (20, 2, 22)

def test_calculateloss():
    price_array = [99, 98, 97, 96, 49, 30, 20, 18, 7, 1]
    assert stocks.calculateprofit(price_array) == (-1, 99, 98)
