# Importación de datos
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_1%20.csv"
url2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_2.csv"
url3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_3.csv"
url4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_4.csv"

tienda = pd.read_csv(url)
tienda2 = pd.read_csv(url2)
tienda3 = pd.read_csv(url3)
tienda4 = pd.read_csv(url4)

tienda.head() #

# 1. Análisis de facturación

# Calcular el ingreso total de cada tienda
ingreso_tienda1 = tienda['Precio'].sum()
ingreso_tienda2 = tienda2['Precio'].sum()
ingreso_tienda3 = tienda3['Precio'].sum()
ingreso_tienda4 = tienda4['Precio'].sum()

print(f"Ingreso total tienda 1: $ {ingreso_tienda1:,.2f}")
print(f"Ingreso total tienda 2: $ {ingreso_tienda2:,.2f}")
print(f"Ingreso total tienda 3: $ {ingreso_tienda3:,.2f}")
print(f"Ingreso total tienda 4: $ {ingreso_tienda4:,.2f}")

ingresos = pd.DataFrame({
    'Tienda': ['Tienda 1', 'Tienda 2', 'Tienda 3', 'Tienda 4'],
    'Ingreso': [ingreso_tienda1, ingreso_tienda2, ingreso_tienda3, ingreso_tienda4]
})
# Graficar los ingresos
plt.figure(figsize=(10, 6))
sns.barplot(x='Tienda', y='Ingreso', data=ingresos, palette='viridis', hue='Tienda', legend=False)
plt.title('Ingreso Total por Tienda')
plt.xlabel('Tienda')
plt.ylabel('Ingreso ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 2. Ventas por categoría

categorias_tienda1 = tienda['Categoría del Producto'].value_counts()
categorias_tienda2 = tienda2['Categoría del Producto'].value_counts()
categorias_tienda3 = tienda3['Categoría del Producto'].value_counts()
categorias_tienda4 = tienda4['Categoría del Producto'].value_counts()

print(f"\nCategorías en tienda 1: {categorias_tienda1}")
print(f"\nCategorías en tienda 2: {categorias_tienda2}")
print(f"\nCategorías en tienda 3: {categorias_tienda3}")
print(f"\nCategorías en tienda 4: {categorias_tienda4}")

# Crear un DataFrame para las categorías
categorias = pd.DataFrame({
    'Tienda': ['Tienda 1', 'Tienda 2', 'Tienda 3', 'Tienda 4'],
    'Categorías': [categorias_tienda1.sum(), categorias_tienda2.sum(), categorias_tienda3.sum(), categorias_tienda4.sum()]
})
# Graficar las categorías
plt.figure(figsize=(10, 6))
sns.barplot(x='Tienda', y='Categorías', data=categorias, palette='coolwarm', hue='Tienda', legend=False)
plt.title('Número de Categorías por Tienda')
plt.xlabel('Tienda')
plt.ylabel('Número de Categorías')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 3. Calificación promedio de la tienda

calificacion_tienda1 = tienda['Calificación'].mean()
calificacion_tienda2 = tienda2['Calificación'].mean()
calificacion_tienda3 = tienda3['Calificación'].mean()
calificacion_tienda4 = tienda4['Calificación'].mean()

print(f"Calificación promedio tienda 1: {calificacion_tienda1:.2f}")
print(f"Calificación promedio tienda 2: {calificacion_tienda2:.2f}")
print(f"Calificación promedio tienda 3: {calificacion_tienda3:.2f}")
print(f"Calificación promedio tienda 4: {calificacion_tienda4:.2f}")

# Crear un DataFrame para las calificaciones
calificaciones = pd.DataFrame({
    'Tienda': ['Tienda 1', 'Tienda 2', 'Tienda 3', 'Tienda 4'],
    'Calificación': [calificacion_tienda1, calificacion_tienda2, calificacion_tienda3, calificacion_tienda4]
})
# Graficar las calificaciones
plt.figure(figsize=(10, 6))
sns.barplot(x='Tienda', y='Calificación', data=calificaciones, palette='mako', hue='Tienda', legend=False)
plt.title('Calificación Promedio por Tienda')
plt.xlabel('Tienda')
plt.ylabel('Calificación Promedio')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 4. Productos más y menos vendidos

# Productos más vendidos
productos_mas_vendidos_tienda1 = tienda['Producto'].value_counts().head(5)
productos_mas_vendidos_tienda2 = tienda2['Producto'].value_counts().head(5)
productos_mas_vendidos_tienda3 = tienda3['Producto'].value_counts().head(5)
productos_mas_vendidos_tienda4 = tienda4['Producto'].value_counts().head(5)

# Productos menos vendidos
productos_menos_vendidos_tienda1 = tienda['Producto'].value_counts().tail(5)
productos_menos_vendidos_tienda2 = tienda2['Producto'].value_counts().tail(5)
productos_menos_vendidos_tienda3 = tienda3['Producto'].value_counts().tail(5)
productos_menos_vendidos_tienda4 = tienda4['Producto'].value_counts().tail(5)

# Productos más vendidos
print(f"\nProductos más vendidos tienda 1: {productos_mas_vendidos_tienda1}")
print(f"\nProductos más vendidos tienda 2: {productos_mas_vendidos_tienda2}")
print(f"\nProductos más vendidos tienda 3: {productos_mas_vendidos_tienda3}")
print(f"\nProductos más vendidos tienda 4: {productos_mas_vendidos_tienda4}")

# Productos menos vendidos
print(f"\nProductos menos vendidos tienda 1: {productos_menos_vendidos_tienda1}")
print(f"\nProductos menos vendidos tienda 2: {productos_menos_vendidos_tienda2}")
print(f"\nProductos menos vendidos tienda 3: {productos_menos_vendidos_tienda3}")
print(f"\nProductos menos vendidos tienda 4: {productos_menos_vendidos_tienda4}")

# Crear un DataFrame para los productos más vendidos
productos_mas_vendidos = pd.DataFrame({
    'Tienda': ['Tienda 1', 'Tienda 2', 'Tienda 3', 'Tienda 4'],
    'Productos Más Vendidos': [
        productos_mas_vendidos_tienda1.sum(),
        productos_mas_vendidos_tienda2.sum(),
        productos_mas_vendidos_tienda3.sum(),
        productos_mas_vendidos_tienda4.sum()
    ]
})
# Graficar los productos más vendidos
plt.figure(figsize=(10, 6))
sns.barplot(x='Tienda', y='Productos Más Vendidos', data=productos_mas_vendidos, palette='rocket', hue='Tienda', legend=False)
plt.title('Productos Más Vendidos por Tienda')
plt.xlabel('Tienda')
plt.ylabel('Número de Productos Vendidos')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# Crear un DataFrame para los productos menos vendidos
productos_menos_vendidos = pd.DataFrame({
    'Tienda': ['Tienda 1', 'Tienda 2', 'Tienda 3', 'Tienda 4'],
    'Productos Menos Vendidos': [
        productos_menos_vendidos_tienda1.sum(),
        productos_menos_vendidos_tienda2.sum(),
        productos_menos_vendidos_tienda3.sum(),
        productos_menos_vendidos_tienda4.sum()
    ]
})
# Graficar los productos menos vendidos
plt.figure(figsize=(10, 6))
sns.barplot(x='Tienda', y='Productos Menos Vendidos', data=productos_menos_vendidos, palette='pastel', hue='Tienda', legend=False)
plt.title('Productos Menos Vendidos por Tienda')
plt.xlabel('Tienda')
plt.ylabel('Número de Productos Vendidos')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 5. Envío promedio por tienda

envio_promedio_tienda1 = tienda['Costo de envío'].mean()
envio_promedio_tienda2 = tienda2['Costo de envío'].mean()
envio_promedio_tienda3 = tienda3['Costo de envío'].mean()
envio_promedio_tienda4 = tienda4['Costo de envío'].mean()

print(f"Costo de envío promedio tienda 1: {envio_promedio_tienda1:.2f}")
print(f"Costo de envío promedio tienda 2: {envio_promedio_tienda2:.2f}")
print(f"Costo de envío promedio tienda 3: {envio_promedio_tienda3:.2f}")
print(f"Costo de envío promedio tienda 4: {envio_promedio_tienda4:.2f}")

# Calcular el costo promedio de envío de cada tienda
envio_promedio_tienda1 = tienda2['Costo de envío'].mean()
envio_promedio_tienda2 = tienda2['Costo de envío'].mean()
envio_promedio_tienda3 = tienda3['Costo de envío'].mean()
envio_promedio_tienda4 = tienda4['Costo de envío'].mean()
# Crear un DataFrame para los envíos
envios = pd.DataFrame({
    'Tienda': ['Tienda 1', 'Tienda 2', 'Tienda 3', 'Tienda 4'],
    'Costo de Envío Promedio': [envio_promedio_tienda1, envio_promedio_tienda2, envio_promedio_tienda3, envio_promedio_tienda4]
})
# Graficar los envíos
plt.figure(figsize=(10, 6))
# sns.barplot(x='Tienda', y='Costo de Envío Promedio', data=envios, palette='Blues')
sns.barplot(x='Tienda', y='Costo de Envío Promedio', data=envios, palette='Blues', hue='Tienda', legend=False)
plt.title('Costo Promedio de Envio por Tienda')
plt.xlabel('Tienda')
plt.ylabel('Costo de Envio Promedio ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()