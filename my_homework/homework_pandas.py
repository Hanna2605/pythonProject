import pandas as pd
import mysql.connector

sdata = pd.read_csv('/Users/annapechyonkina/PycharmProjects/pythonProject_lessons/Python7/016_pandas/csv_files/survey_results_public.csv')
# pd.set_option('display.max_columns', 85)

print("1. Выводит данные о том сколько программистов является профессионалами и сколько хобби программистами. (столбец 'Hobbyist')")
print(sdata.groupby('Hobbyist').count()['Respondent'])
print('\n')

print("2. Выводит средний, максимальный и минимальный возраст (столбец 'Age') программистов")
print(f'maximum age: {sdata["Age"].max()}')
print(f'minimum age: {sdata["Age"].min()}')
print(f'median age: {sdata["Age"].mean()}')
print('\n')

print("3. Выводит таблицу со странами (столбец 'Country'). Группирует, считает кол-во и выводит в порядке убывания.")
print(sdata['Country'].value_counts(ascending=False))
print('\n')

print("4. Выводит таблицу с валютами (столбец 'CurrencyDesc'). Группирует и выводит в порядке убывания")
print(sdata['CurrencySymbol'].value_counts(ascending=False))


