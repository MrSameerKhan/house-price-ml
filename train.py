import pickle
import numpy as np
from sklearn.linear_model import LinearRegression

# Training data
X = np.array([[500], [800], [1000], [1200], [1500]])
y = np.array([50, 80, 100, 120, 150])

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved")
