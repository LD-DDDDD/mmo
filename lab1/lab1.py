import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Загрузим данные
data = pd.read_csv("winequality-red-folds.csv")

# Посмотрим на первые несколько строк датасета
print(data.head())

# Посмотрим на информацию о датасете
print(data.info())

# Посмотрим на статистику датасета
print(data.describe())

# Построим гистограмму распределения качества вина
plt.figure(figsize=(8, 6))
sns.histplot(data['quality'], bins=6, kde=True)
plt.title('Распределение качества вина')
plt.xlabel('Качество')
plt.ylabel('Количество')
plt.grid(True)
plt.show()

# Построим тепловую карту корреляции
plt.figure(figsize=(10, 8))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Тепловая карта корреляции признаков')
plt.show()

# Построим ящик с усами для распределения алкоголя
plt.figure(figsize=(8, 6))
sns.boxplot(x='quality', y='alcohol', data=data)
plt.title('Распределение содержания алкоголя по качеству вина')
plt.xlabel('Качество')
plt.ylabel('Содержание алкоголя')
plt.show()

# Построим точечную диаграмму для сравнения pH и качества вина
plt.figure(figsize=(8, 6))
sns.scatterplot(x='pH', y='quality', data=data)
plt.title('Сравнение pH и качества вина')
plt.xlabel('pH')
plt.ylabel('Качество')
plt.show()

# Построим полосчатую диаграмму для сравнения содержания алкоголя по качеству вина
plt.figure(figsize=(8, 6))
sns.barplot(x='quality', y='alcohol', data=data, ci=None)
plt.title('Среднее содержание алкоголя по качеству вина')
plt.xlabel('Качество')
plt.ylabel('Среднее содержание алкоголя')
plt.show()