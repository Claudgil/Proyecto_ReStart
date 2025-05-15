import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error
import joblib

def load_data(file_path):
    print("Cargando datos...")
    data = pd.read_csv(file_path)
    print("Datos cargados exitosamente.")
    return data

def preprocess_data(data):
    print("\nPreprocesando datos...")

    # Convertir "date" a datetime y extraer características
    data["date"] = pd.to_datetime(data["date"])
    data["day_of_week"] = data["date"].dt.dayofweek
    data["month"] = data["date"].dt.month

    # Agrupar por 'item_name' y generar características basadas en la cantidad
    grouped_data = data.groupby(["item_name", "date"]).agg({
        "quantity": "sum",
        "day_of_week": "first",
        "month": "first"
    }).reset_index()

    # Variables de entrada y objetivo
    features = ["day_of_week", "month"]
    X = grouped_data[features]
    y = grouped_data["quantity"]

    print(f"Características seleccionadas: {features}")
    return X, y, grouped_data["item_name"]

def train_model(X, y):
    print("\nDividiendo datos en conjuntos de entrenamiento y prueba...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print("Entrenando modelo Random Forest...")
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    print("Modelo entrenado exitosamente.")

    print("Evaluando el modelo...")
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    print(f"Error cuadrático medio (MSE): {mse:.2f}")
    print(f"Error absoluto medio (MAE): {mae:.2f}")

    return model

def save_model(model, model_path):
    print("\nGuardando modelo entrenado...")
    joblib.dump(model, model_path)
    print(f"Modelo guardado en: {model_path}")

if __name__ == "__main__":
    input_path = os.path.abspath("C:/Users/pavil/OneDrive/Escritorio/AWS ReStart/Proyecto/AWSproyecto.css/dataset/ventas_limpias.csv")
    model_path = os.path.abspath("C:/Users/pavil/OneDrive/Escritorio/AWS ReStart/Proyecto/AWSproyecto.css/model/modelo_ventas.pkl")

    data = load_data(input_path)
    X, y, item_names = preprocess_data(data)
    model = train_model(X, y)

    # Crear directorio para guardar el modelo si no existe
    model_dir = os.path.dirname(model_path)
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    save_model(model, model_path)

