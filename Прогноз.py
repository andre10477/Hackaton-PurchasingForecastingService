import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Функция для чтения CSV файла с различными кодировками
def read_csv_with_encodings(file_path, encodings):
    for encoding in encodings:
        try:
            df = pd.read_csv(file_path, encoding=encoding)
            return df
        except Exception as e:
            print(f"Ошибка чтения {file_path} с кодировкой {encoding}: {e}")
    return None

# Функция для поиска товара в файлах и вывода информации
def search_product_in_files(product_name, csv_files):
    product_data = []
    columns_of_interest = [
        'Остаточная стоимость', 'Сальдо на конец периода, дебет',
        'Остаток на 31 марта 2022 г. дебет', 'Остаток на 30 июня 2022 г. дебет',
        'Остаток на 30 сентября 2022 г. дебет', 'Остаток на 31 декабря 2022 г. дебет',
        'Количество(конец периода)', 'Суммарный остаток на 31 декабря 2022 г. дебет', 
        'Количество'
    ]

    for file_name, encodings in csv_files:
        print(f"Чтение: {file_name}")
        df = read_csv_with_encodings(file_name, encodings)
        
        if df is not None:
            if 'Основные средства' in df.columns:
                product_info = df[df['Основные средства'].str.contains(product_name, na=False)]
            elif 'Наименование нефинансового актива' in df.columns:
                product_info = df[df['Наименование нефинансового актива'].str.contains(product_name, na=False)]
            elif 'МОЛ' in df.columns:
                product_info = df[df['МОЛ'].str.contains(product_name, na=False)]
            else:
                print(f"Товар не найден в файле {file_name}")
                continue
            
            if not product_info.empty:
                print(product_info)
                # Сохраняем данные по остаткам товара
                if 'Дата' in df.columns:
                    for _, row in product_info.iterrows():
                        date = pd.to_datetime(row['Дата'])
                        value = None
                        for column in columns_of_interest:
                            if column in row and not pd.isna(row[column]):
                                value = row[column]
                                break
                        if value is not None:
                            product_data.append((date, value))
                        else:
                            print(f"Нет данных по остаткам для строки: {row}")
            else:
                print(f"Товар '{product_name}' не найден в файле {file_name}")
        else:
            print(f"Ошибка чтения {file_name}")

    print(f"Собранные данные по товару: {product_data}")
    return product_data

# Функция для рассчета потребления за каждый квартал
def calculate_consumption(product_data):
    quarterly_consumption = []
    
    # Сортируем данные по дате, хотя в данном случае сортировка может быть не нужна
    product_data.sort(key=lambda x: x[0])
    
    # Рассчитываем потребление за каждый квартал
    for i in range(len(product_data) - 1):
        start_date, start_value = product_data[i]
        end_date, end_value = product_data[i + 1]
        
        # Рассчитываем потребление как разницу между конечным и начальным остатками
        consumption = start_value - end_value
        quarterly_consumption.append((start_date, consumption))
    
    return quarterly_consumption

# Функция для прогнозирования времени до окончания товара
def forecast_end_date(quarterly_consumption):
    # Преобразуем данные в формат, пригодный для обучения регрессии
    X = np.array([date.timestamp() for date, _ in quarterly_consumption]).reshape(-1, 1)
    y = np.array([consumption for _, consumption in quarterly_consumption])
    
    # Создаем и обучаем модель линейной регрессии
    model = LinearRegression()
    model.fit(X, y)
    
    # Прогнозируем время до окончания товара
    last_date = quarterly_consumption[-1][0]
    future_date = last_date + pd.DateOffset(days=int(model.intercept_ / (-model.coef_[0])))
    
    return future_date

# Функция для построения графика остатков
def plot_product_data(product_data):
    if not product_data:
        print("Нет данных для построения графика.")
        return

    product_data.sort(key=lambda x: x[0])  # Сортируем по дате
    dates, values = zip(*product_data)

    plt.figure(figsize=(10, 5))
    plt.plot(dates, values, marker='o')
    plt.xlabel('Дата')
    plt.ylabel('Остаток')
    plt.title('График остатков товара')
    plt.grid(True)
    plt.show()

# Основной блок кода для выполнения программы
if __name__ == "__main__":
    product_name = input(f"Введите имя товара: ")
    csv_files = [
        ('Оборотная ведомость сч. 21 за 2022г. .csv', ['utf-32', 'utf-8-sig', 'utf-16', 'latin1']),
        ('Оборотная ведомость сч. 101 за 2022г. .csv', ['utf-32', 'utf-8-sig', 'utf-16', 'latin1']),
        ('Оборотная ведомость сч. 105 за 2022г. .csv', ['utf-32', 'utf-8-sig', 'utf-16', 'latin1']),
        ('Ведомость остатков сч. 21 за 2022г. .csv', ['utf-8-sig', 'utf-32', 'utf-16', 'latin1']),
        ('Ведомость остатков сч. 101 за 2022г. .csv', ['utf-8-sig', 'utf-32', 'utf-16', 'latin1']),
        ('Ведомость остатков сч. 105 за 2022г. .csv', ['utf-8-sig', 'utf-32', 'utf-16', 'latin1'])
    ]
    
    # Поиск товара в файлах и сбор данных
    product_data = search_product_in_files(product_name, csv_files)

    if product_data:
        plot_product_data(product_data)
        
        # Рассчет потребления за кварталы
        quarterly_consumption = calculate_consumption(product_data)
        
        if quarterly_consumption:
            # Вывод потребления за каждый квартал
            print("Потребление за каждый квартал:")
            for date, consumption in quarterly_consumption:
                print(f"{date.date()}: {consumption}")
            
            # Прогнозирование времени до окончания товара
            end_date = forecast_end_date(quarterly_consumption)
            
            if end_date:
                print(f"Товар '{product_name}' закончится через {end_date.date() - product_data[-1][0].date()} с учетом расходов.")
            else:
                print("Не удалось спрогнозировать дату окончания товара.")
        else:
            print("Недостаточно данных для расчета потребления.")
    else:
        print("Нет данных для построения графика и прогнозирования.")


















'''import pandas as pd
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

# Функция для чтения CSV файла с различными кодировками
def read_csv_with_encodings(file_path, encodings):
    for encoding in encodings:
        try:
            df = pd.read_csv(file_path, encoding=encoding)
            return df
        except Exception as e:
            print(f"Ошибка чтения {file_path} с кодировкой {encoding}: {e}")
    return None

# Функция для поиска товара в файлах и вывода информации
def search_product_in_files(product_name, csv_files):
    product_data = []
    columns_of_interest = [
        'Остаточная стоимость', 'Сальдо на конец периода, дебет',
        'Остаток на 31 марта 2022 г. дебет', 'Остаток на 30 июня 2022 г. дебет',
        'Остаток на 30 сентября 2022 г. дебет', 'Остаток на 31 декабря 2022 г. дебет',
        'Количество(конец периода)', 'Суммарный остаток на 31 декабря 2022 г. дебет', 
        'Количество'
    ]

    for file_name, encodings in csv_files:
        print(f"Чтение: {file_name}")
        df = read_csv_with_encodings(file_name, encodings)
        
        if df is not None:
            if 'Основные средства' in df.columns:
                product_info = df[df['Основные средства'].str.contains(product_name, na=False)]
            elif 'Наименование нефинансового актива' in df.columns:
                product_info = df[df['Наименование нефинансового актива'].str.contains(product_name, na=False)]
            elif 'МОЛ' in df.columns:
                product_info = df[df['МОЛ'].str.contains(product_name, na=False)]
            else:
                print(f"Товар не найден в файле {file_name}")
                continue
            
            if not product_info.empty:
                print(product_info)
                # Сохраняем данные по остаткам товара
                if 'Дата' in df.columns:
                    for _, row in product_info.iterrows():
                        date = pd.to_datetime(row['Дата'])
                        value = None
                        for column in columns_of_interest:
                            if column in row and not pd.isna(row[column]):
                                value = row[column]
                                break
                        if value is not None:
                            product_data.append((date, value))
                        else:
                            print(f"Нет данных по остаткам для строки: {row}")
            else:
                print(f"Товар '{product_name}' не найден в файле {file_name}")
        else:
            print(f"Ошибка чтения {file_name}")

    print(f"Собранные данные по товару: {product_data}")
    return product_data

# Построение графика остатков
def plot_product_data(product_data):
    if not product_data:
        print("Нет данных для построения графика.")
        return

    product_data.sort(key=lambda x: x[0])  # Сортируем по дате
    dates, values = zip(*product_data)

    plt.figure(figsize=(10, 5))
    plt.plot(dates, values, marker='o')
    plt.xlabel('Дата')
    plt.ylabel('Остаток')
    plt.title('График остатков товара')
    plt.grid(True)
    plt.show()

# Подготовка данных для нейросети
def prepare_data_for_nn(product_data):
    if not product_data:
        print("Нет данных для подготовки нейросети.")
        return None, None
    
    product_data.sort(key=lambda x: x[0])
    dates, values = zip(*product_data)
    dates = np.array([date.timestamp() for date in dates]).reshape(-1, 1)  # Преобразуем даты в числа
    values = np.array(values)
    return dates, values

# Поиск товара на наименованию и аналитика
product_name = input(f"Введите имя товара: ")
csv_files = [
    ('Оборотная ведомость сч. 21 за 2022г. .csv', ['utf-32', 'utf-8-sig', 'utf-16', 'latin1']),
    ('Оборотная ведомость сч. 101 за 2022г. .csv', ['utf-32', 'utf-8-sig', 'utf-16', 'latin1']),
    ('Оборотная ведомость сч. 105 за 2022г. .csv', ['utf-32', 'utf-8-sig', 'utf-16', 'latin1']),
    ('Ведомость остатков сч. 21 за 2022г. .csv', ['utf-8-sig', 'utf-32', 'utf-16', 'latin1']),
    ('Ведомость остатков сч. 101 за 2022г. .csv', ['utf-8-sig', 'utf-32', 'utf-16', 'latin1']),
    ('Ведомость остатков сч. 105 за 2022г. .csv', ['utf-8-sig', 'utf-32', 'utf-16', 'latin1'])
]
product_data = search_product_in_files(product_name, csv_files)

if product_data:
    plot_product_data(product_data)
    dates, values = prepare_data_for_nn(product_data)
    if dates is not None and values is not None:
        # Определение и обучение нейросети
        model = Sequential()
        model.add(Dense(10, input_dim=1, activation='relu'))
        for _ in range(30):
            model.add(Dense(10, activation='relu'))
        model.add(Dense(1, activation='linear'))

        model.compile(loss='mean_squared_error', optimizer='adam')
        model.fit(dates, values, epochs=10, batch_size=8, verbose=1)

        # Прогнозирование даты окончания товара
        def predict_end_of_stock(dates, values, model):
            future_dates = np.linspace(dates[-1], dates[-1] + 60*60*24*365, num=365).reshape(-1, 1)  # Следующий год по дням
            future_values = model.predict(future_dates)
            
            for future_date, future_value in zip(future_dates, future_values):
                if future_value <= 0:
                    end_date = pd.to_datetime(future_date[0], unit='s')
                    return end_date

            return None

        end_date = predict_end_of_stock(dates, values, model)
        if end_date:
            print(f"Товара '{product_name}' осталось ещё на {end_date.date() - pd.to_datetime(dates[-1], unit='s').date()}.")
        else:
            print("Не удалось спрогнозировать дату окончания товара.")
else:
    print("Нет данных для построения графика и прогнозирования.")'''


'''import pandas as pd
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
import numpy as np

# Функция для чтения CSV файла с различными кодировками
def read_csv_with_encodings(file_path, encodings):
    for encoding in encodings:
        try:
            df = pd.read_csv(file_path, encoding=encoding)
            return df
        except Exception as e:
            print(f"Ошибка чтения {file_path} с кодировкой {encoding}: {e}")
    return None

# Функция для поиска товара в файлах и вывода информации
def search_product_in_files(product_name, csv_files):
    product_data = []

    for file_name, encodings in csv_files:
        print(f"Чтение: {file_name}")
        df = read_csv_with_encodings(file_name, encodings)
        
        if df is not None:
            if 'Основные средства' in df.columns:
                product_info = df[df['Основные средства'].str.contains(product_name, na=False)]
            elif 'Наименование нефинансового актива' in df.columns:
                product_info = df[df['Наименование нефинансового актива'].str.contains(product_name, na=False)]
            elif 'МОЛ' in df.columns:
                product_info = df[df['МОЛ'].str.contains(product_name, na=False)]
            else:
                print(f"Товар не найден в файле {file_name}")
                continue
            
            if not product_info.empty:
                print(product_info)
                # Сохраняем данные по остаткам товара
                if 'Дата' in df.columns and ('Остаточная стоимость' in df.columns or 'Сальдо на конец периода, дебет' in df.columns):
                    for _, row in product_info.iterrows():
                        date = pd.to_datetime(row['Дата'])
                        if 'Остаточная стоимость' in row:
                            value = row['Остаточная стоимость']
                        elif 'Сальдо на конец периода, дебет' in row:
                            value = row['Сальдо на конец периода, дебет']
                        product_data.append((date, value))
            else:
                print(f"Товар '{product_name}' не найден в файле {file_name}")
        else:
            print(f"Ошибка чтения {file_name}")

    return product_data

# Имена файлов и кодировки
csv_files = [
    ('Оборотная ведомость сч. 21 за 2022г. .csv', ['utf-32', 'utf-8-sig', 'utf-16', 'latin1']),
    ('Оборотная ведомость сч. 101 за 2022г. .csv', ['utf-32', 'utf-8-sig', 'utf-16', 'latin1']),
    ('Оборотная ведомость сч. 105 за 2022г. .csv', ['utf-32', 'utf-8-sig', 'utf-16', 'latin1']),
    ('Ведомость остатков сч. 21 за 2022г. .csv', ['utf-8-sig', 'utf-32', 'utf-16', 'latin1']),
    ('Ведомость остатков сч. 101 за 2022г. .csv', ['utf-8-sig', 'utf-32', 'utf-16', 'latin1']),
    ('Ведомость остатков сч. 105 за 2022г. .csv', ['utf-8-sig', 'utf-32', 'utf-16', 'latin1'])
]

# Пример использования
product_name = "Клей Момент Столяр Экспресс,750г"
product_data = search_product_in_files(product_name, csv_files)

# Построение графика остатков
def plot_product_data(product_data):
    if not product_data:
        print("Нет данных для построения графика.")
        return

    product_data.sort(key=lambda x: x[0])  # Сортируем по дате
    dates, values = zip(*product_data)

    plt.figure(figsize=(10, 5))
    plt.plot(dates, values, marker='o')
    plt.xlabel('Дата')
    plt.ylabel('Остаток')
    plt.title('График остатков товара')
    plt.grid(True)
    plt.show()

plot_product_data(product_data)

# Подготовка данных для нейросети
def prepare_data_for_nn(product_data):
    product_data.sort(key=lambda x: x[0])
    dates, values = zip(*product_data)
    dates = np.array([date.timestamp() for date in dates]).reshape(-1, 1)  # Преобразуем даты в числа
    values = np.array(values)
    return dates, values

dates, values = prepare_data_for_nn(product_data)

# Определение и обучение нейросети
model = Sequential()
model.add(Dense(10, input_dim=1, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(1))

model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(dates, values, epochs=100, batch_size=32, verbose=1)

# Прогнозирование даты окончания товара
def predict_end_of_stock(dates, values, model):
    future_dates = np.linspace(dates[-1], dates[-1] + 60*60*24*365, num=365).reshape(-1, 1)  # Следующий год по дням
    future_values = model.predict(future_dates)
    
    for future_date, future_value in zip(future_dates, future_values):
        if future_value <= 0:
            end_date = pd.to_datetime(future_date[0], unit='s')
            return end_date

    return None

end_date = predict_end_of_stock(dates, values, model)
if end_date:
    print(f"Товара '{product_name}' осталось ещё на {end_date.date() - pd.to_datetime(dates[-1], unit='s').date()}.")
else:
    print("Не удалось спрогнозировать дату окончания товара.")'''