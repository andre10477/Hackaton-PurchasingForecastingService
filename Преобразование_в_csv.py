import pandas as pd

#преобразование данных в csv
data_xlsx = pd.read_excel('Ведомость остатков на 31.03.2022г. (сч. 105).xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('105_31.03.2022.csv', encoding='cp1251')

data_xlsx = pd.read_excel('Ведомость остатков на 31.03.2022г. (сч. 101).xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('101_31.03.2022.csv', encoding='cp1251')

data_xlsx = pd.read_excel('Ведомость остатков на 31.03.2022г. (сч. 21).xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('21_31.03.2022.csv', encoding='cp1251')



data_xlsx = pd.read_excel('Ведомость остатков на 30.06.2022г. (сч. 105).xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('105_30.06.2022.csv', encoding='cp1251')

data_xlsx = pd.read_excel('Ведомость остатков на 30.06.2022г. (сч. 101).xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('101_30.06.2022.csv', encoding='cp1251')

data_xlsx = pd.read_excel('Ведомость остатков на 30.06.2022г. (сч. 21).xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('21_30.06.2022.csv', encoding='cp1251')



data_xlsx = pd.read_excel('Ведомость остатков на 30.09.2022г. (сч. 105).xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('105_30.09.2022.csv', encoding='cp1251')

data_xlsx = pd.read_excel('Ведомость остатков на 30.09.2022г. (сч. 101).xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('101_30.09.2022.csv', encoding='cp1251')

data_xlsx = pd.read_excel('Ведомость остатков на 30.09.2022г. (сч. 21).xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('21_30.09.2022.csv', encoding='cp1251')



data_xlsx = pd.read_excel('Ведомость остатков на 31.12.2022г. (сч. 105).xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('105_31.12.2022.csv', encoding='cp1251')

data_xlsx = pd.read_excel('Ведомость остатков на 31.12.2022г. (сч. 101).xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('101_31.12.2022.csv', encoding='cp1251')

data_xlsx = pd.read_excel('Ведомость остатков на 31.12.2022г. (сч. 21).xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('21_31.12.2022.csv', encoding='cp1251')

print("закончил")