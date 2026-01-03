def predict_price(area_sqft):
    return area_sqft * 1000

if __name__ == "__main__":
    print("Prediction:", predict_price(1200))
