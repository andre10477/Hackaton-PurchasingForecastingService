import psycopg2
import pandas as pd

# Параметры подключения к базе данных
dbname = "your_dbname"
user = "your_user"
password = "your_password"
host = "your_host"  # Адрес вашего удаленного сервера
port = "your_port"  # Обычно 5432

# Подключение к базе данных
conn = psycopg2.connect(
    dbname=dbname,
    user=user,
    password=password,
    host=host,
    port=port
)
cur = conn.cursor()

# Чтение CSV файла с помощью pandas
csv_file_path = 'Ведомость остатков по сч. 21, 101, 105 за 2022г. .csv'
df = pd.read_csv(csv_file_path)

# Создание таблицы (если таблица уже существует, этот шаг можно пропустить)
create_table_query = """
CREATE TABLE IF NOT EXISTS assets (
    Основное_средство VARCHAR,
    Инвентарный_номер VARCHAR,
    ОКОФ VARCHAR,
    Амортизационная_группа VARCHAR,
    Способ_начисления_амортизации VARCHAR,
    Дата_принятия_к_учету DATE,
    Состояние VARCHAR,
    Срок_полезного_использования INT,
    Мес_норма_износа_проц FLOAT,
    Износ_проц FLOAT,
    Балансовая_стоимость FLOAT,
    Количество INT,
    Сумма_амортизации FLOAT,
    Остаточная_стоимость FLOAT,
    Номер_счёта VARCHAR,
    Дата DATE,
    Классификатор VARCHAR,
    МОЛ VARCHAR,
    Цена FLOAT,
    Сумма FLOAT
);
"""
cur.execute(create_table_query)
conn.commit()

# Преобразование названий колонок для использования в SQL
columns = [col.replace(' ', '_').replace(',', '').replace('.', '') for col in df.columns]
df.columns = columns

# Вставка данных из DataFrame в таблицу
for index, row in df.iterrows():
    values = tuple(row)
    placeholders = ', '.join(['%s'] * len(values))
    insert_query = f"INSERT INTO assets ({', '.join(columns)}) VALUES ({placeholders})"
    cur.execute(insert_query, values)

# Подтверждение изменений и закрытие соединения
conn.commit()
cur.close()
conn.close()