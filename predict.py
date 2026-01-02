import pickle
import sys

size = float(sys.argv[1])

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

price = model.predict([[size]])
print(f"Predicted price: {price[0]}")
