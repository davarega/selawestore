import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error

X = np.linspace(0, 2 * np.pi, 200).reshape(-1, 1)
y = np.sin(X).ravel()

ann = MLPRegressor(hidden_layer_sizes=(100, 50),
                   activation='tanh',
                   solver='adam',
                   max_iter=2000,
                   random_state=42)

print("Melatih model ANN...")
ann.fit(X, y)
print("Pelatihan selesai.")

y_pred = ann.predict(X)

mse = mean_squared_error(y, y_pred)
print(f"\nMean Squared Error (MSE): {mse:.6f}")

plt.figure(figsize=(10, 6))
plt.plot(X, y, label='Fungsi sin(x) Original', color='blue', linewidth=2)
plt.plot(X, y_pred, label='Prediksi ANN', color='red', linestyle='--', linewidth=2)
plt.title('Aproksimasi Fungsi sin(x) dengan ANN')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.legend()
plt.grid(True)
plt.show()
