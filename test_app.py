from app import predict_price

def test_predict_price():
    assert predict_price(1000) == 1_000_000
