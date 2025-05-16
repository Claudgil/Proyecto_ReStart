# 📊 Modelo Predictivo para Restaurantes

Este proyecto fue desarrollado como parte del programa **AWS Re/Start** y tiene como objetivo anticipar la demanda de productos en restaurantes, utilizando datos históricos de ventas. Esto permite **optimizar inventarios**, **reducir desperdicios** y **mejorar la toma de decisiones** en fechas clave como el Día de la Madre, Navidad, entre otras.

## 🧠 Objetivo

Predecir la cantidad de productos que se deben pedir o preparar en base a patrones históricos de consumo, ajustando los pedidos según temporadas de alta demanda.

## 📁 Dataset

El dataset contiene 1000 registros con las siguientes columnas:

- `order_id`
- `date`
- `item_name`
- `item_type`
- `item_price`
- `quantity`
- `transaction_amount`
- `transaction_type`
- `received_by`
- `time_of_sale`

## 🔧 Tecnologías utilizadas

- Python 3.x  
- Pandas  
- Scikit-learn  
- Matplotlib / Seaborn  
- Jupyter Notebook (a través de Anaconda)

## 🔍 Etapas del proyecto

1. **Análisis exploratorio de datos (EDA)**
2. **Limpieza y transformación de datos**
3. **Selección de variables clave**
4. **Entrenamiento del modelo predictivo**
5. **Evaluación del modelo**
6. **Visualización de resultados y patrones estacionales**

## 📈 Resultados

El modelo identifica tendencias de consumo y ayuda a prever la demanda de productos, lo que permite tomar decisiones informadas al momento de realizar pedidos, sobre todo en eventos especiales o temporadas de alta rotación.

## 🚀 Cómo ejecutar

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/tu-repo.git
