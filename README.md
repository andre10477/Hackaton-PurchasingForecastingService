# Hackaton-PurchasingForecastingService

В данном репозитории содержится программный код на языке Python, выполняющий Backend часть проекта. Так же имеется документация ниже.

Техническая документация по выполненной работе 
ЛЦТ, задача 02 «Сервис прогнозирования и проведения закупок»
Автор: Жиряков А. Р., Команда: CP Zoro, Роль: Backend-разработка
В рамках выполнения задачи были выполнены скрипты на языке Python 3.11, выполняющие роль backend-обработки запросов пользователя. В документе приложены несколько листингов программных файлов и их текстовое описание функционала. В качестве базы данных используется PostgreSQL.
Список скриптов:
•	Преобразование_в_csv.py
•	Преобразование_csv_в_удобный_формат(обороты).py
•	Преобразование_csv_в_удобный_формат(остатки).py
•	Перенос_в_БД.py
•	Прогноз.py

Скрипт Преобразование_в_csv.py
Описание:
Данный программный код исполняет функцию преобразования таблиц формата MS Excel в вид csv таблиц для удобства обработки данных сервером. Используется библиотека pandas в качестве обработчика. Используются разные кодировки в силу различного содержимого файлов.
Листинг:
import pandas as pd

#преобразование данных в csv - ведомости остатков
data_xlsx = pd.read_excel('Ведомость остатков на 31.03.2022г. (сч. 105).xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('105_31.03.2022.csv', encoding='utf-8-sig')
data_xlsx = pd.read_excel('Ведомость остатков на 31.03.2022г. (сч. 101).xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('101_31.03.2022.csv', encoding='utf-8-sig')
data_xlsx = pd.read_excel('Ведомость остатков на 31.03.2022г. (сч. 21).xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('21_31.03.2022.csv', encoding='utf-8-sig')

data_xlsx = pd.read_excel('Ведомость остатков на 30.06.2022г. (сч. 105).xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('105_30.06.2022.csv', encoding='utf-8-sig')
data_xlsx = pd.read_excel('Ведомость остатков на 30.06.2022г. (сч. 101).xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('101_30.06.2022.csv', encoding='utf-8-sig')
data_xlsx = pd.read_excel('Ведомость остатков на 30.06.2022г. (сч. 21).xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('21_30.06.2022.csv', encoding='utf-8-sig')
data_xlsx = pd.read_excel('Ведомость остатков на 30.09.2022г. (сч. 105).xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('105_30.09.2022.csv', encoding='utf-8-sig')
data_xlsx = pd.read_excel('Ведомость остатков на 30.09.2022г. (сч. 101).xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('101_30.09.2022.csv', encoding='utf-8-sig')
data_xlsx = pd.read_excel('Ведомость остатков на 30.09.2022г. (сч. 21).xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('21_30.09.2022.csv', encoding='utf-8-sig')


data_xlsx = pd.read_excel('Ведомость остатков на 31.12.2022г. (сч. 105).xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('105_31.12.2022.csv', encoding='utf-8-sig')
data_xlsx = pd.read_excel('Ведомость остатков на 31.12.2022г. (сч. 101).xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('101_31.12.2022.csv', encoding='utf-8-sig')
data_xlsx = pd.read_excel('Ведомость остатков на 31.12.2022г. (сч. 21).xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('21_31.12.2022.csv', encoding='utf-8-sig')




#преобразование данных в csv - оборотно-счётные ведомости
data_xlsx = pd.read_excel('Оборотная ведомость по сч. 105 за 1 кв. 2022г..xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('105_1_2022.csv', encoding='utf-32')
data_xlsx = pd.read_excel('Оборотная ведомость по сч. 105 за 2 кв. 2022г..xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('105_2_2022.csv', encoding='utf-32')
data_xlsx = pd.read_excel('Оборотная ведомость по сч. 105 за 3 кв. 2022г..xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('105_3_2022.csv', encoding='utf-32')
data_xlsx = pd.read_excel('Оборотная ведомость по сч. 105 за 4 кв. 2022г..xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('105_4_2022.csv', encoding='utf-32')


data_xlsx = pd.read_excel('Оборотно-сальдовая ведомость по сч. 101 за 1 кв. 2022г..xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('101_1_2022.csv', encoding='utf-32')
data_xlsx = pd.read_excel('Оборотно-сальдовая ведомость по сч. 101 за 2 кв. 2022г..xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('101_2_2022.csv', encoding='utf-32')
data_xlsx = pd.read_excel('Оборотно-сальдовая ведомость по сч. 101 за 3 кв. 2022г..xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('101_3_2022.csv', encoding='utf-32')
data_xlsx = pd.read_excel('Оборотно-сальдовая ведомость по сч. 101 за 4 кв. 2022г..xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('101_4_2022.csv', encoding='utf-32')


data_xlsx = pd.read_excel('Оборотно-сальдовая ведомость по сч. 21 за 1 кв. 2022г..xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('21_1_2022.csv', encoding='utf-32')
data_xlsx = pd.read_excel('Оборотно-сальдовая ведомость по сч. 21 за 2 кв. 2022г..xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('21_2_2022.csv', encoding='utf-32')
data_xlsx = pd.read_excel('Оборотно-сальдовая ведомость по сч. 21 за 3 кв. 2022г..xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('21_3_2022.csv', encoding='utf-32')
data_xlsx = pd.read_excel('Оборотно-сальдовая ведомость по сч. 21 за 4 кв. 2022г..xlsx', 'Лист_1', index_col=None)
data_xlsx.to_csv('21_4_2022.csv', encoding='utf-32')
Скрипт Преобразование_csv_в_удобный_формат(обороты).py
Описание:
	В данном программном файле содержится скрипт, исполняющий преобразование Excel-таблиц оборотных и оборотно-сальдовых ведомостей в csv-файлы. 
Основные шаги и функции
1.	Импорт библиотек:
o	csv, os, pandas и re используются для работы с файлами CSV, обработки данных и регулярных выражений.
2.	Функция obrabotka(data, schN, qua):
o	Добавляет столбцы с кварталом, номером счёта и классификатором.
o	В зависимости от значения schN (номер счёта), выполняет различные преобразования данных.
o	Удаляет ненужные столбцы, заменяет пустые строки на NaN, удаляет строки с NaN в ключевых столбцах.
o	Упорядочивает столбцы для счёта 105.
o	Переиндексирует данные, начиная с 1.
3.	Чтение и обработка данных:
o	Чтение CSV файлов с оборотных ведомостей для каждого счёта (21, 101, 105) за разные кварталы в 2022 году.
o	Обработка данных с помощью функции obrabotka.
4.	Объединение и сохранение данных:
o	Объединение обработанных данных для каждого счёта в один DataFrame и сохранение в новые CSV файлы.
o	Объединение данных по всем счетам в один общий DataFrame и сохранение его в CSV файл.
Листинг:
import csv
import os
import pandas as pd
import re

#функция обработки данных для исследования
def obrabotka(data, schN, qua):
    
    #добавление столбца классификатора
    data['Классификатор'] = None

    #регулярное выражение для поиска классификаторов
    classifier_pattern = re.compile(fr'^({schN}\.\d+)')

    #текущий классификатор
    current_classifier = None
    
    #удаление ненужных столбцов
    if 'Unnamed: 0' in data.columns:
        data.drop(columns=['Unnamed: 0'], inplace=True)
        
    if 'Unnamed: 0.1' in data.columns:
        data.drop(columns=['Unnamed: 0.1'], inplace=True)
            
    #замена пустых строк на NaN
    data.replace('', pd.NA, inplace=True)

    #добавление столбцов с кварталом и номером счёта
    data['Квартал'] = qua
    data['Номер счёта'] = schN
    
    if schN == 105:
        #проход по строкам DataFrame
        for index, row in data.iterrows():
            unnamed_value = str(row['Инвентарный / номенклатурный номер']).strip()
            match = classifier_pattern.search(unnamed_value)
            if match:
                #оставляем только код, убирая текстовое описание
                current_classifier = match.group(1)
            elif pd.notna(row['Код справочника']) and pd.notna(row['Наименование нефинансового актива']):
                data.at[index, 'Классификатор'] = current_classifier

        #удаление строк, в которых 'Основные средства' является NaN
        data = data.dropna(subset=['Код справочника', 'Наименование нефинансового актива']).copy()
        #удаление ненужных столбцов
        if 'Инвентарный / номенклатурный номер' in data.columns:
            data.drop(columns=['Инвентарный / номенклатурный номер'], inplace=True)
            
        data.rename(columns = {'Наименование нефинансового актива':'Основные средства'}, inplace = True)

        # Список столбцов в нужном порядке
        columns_titles = [
        'Основное средство', 'Код справочника', 'Единица измерения',
        'Остаток на 1 января 2022 г. дебет', 'Сумма на 1 января 2022 г. дебет',
        'Оборот за 1 квартал 2022 г. дебет', 'Суммарный оборот за 1кв. дебет',
        'Оборот за 1 квартал 2022 г. кредит', 'Суммарный оборот за 1кв. кредит',
        'Остаток на 31 марта 2022 г. дебет ', 'Суммарный остаток на 31 марта 2022 г. дебет ',
        'Классификатор', 'Квартал', 'Номер счёта', 'Остаток на 1 апреля 2022 г. Дебет',
        'Сумма на 1 апреля 2022 г. дебет', 'Оборот за 2 квартал 2022 г. дебет',
        'Суммарный оборот за 2кв. дебет', 'Оборот за 2 квартал 2022 г. кредит',
        'Суммарный оборот за 2кв. кредит', 'Остаток на 30 июня 2022 г. дебет ',
        'Суммарный остаток на 30 июня 2022 г. дебет ', 'Остаток на 1 июля 2022 г. дебет',
        'Сумма на 1 июля 2022 г. дебет', 'Оборот за 3 квартал 2022 г. дебет',
        'Суммарный оборот за 3кв. дебет', 'Оборот за 3 квартал 2022 г. кредит',
        'Суммарный оборот за 3кв. кредит', 'Остаток на 30 сентября 2022 г. дебет ',
        'Суммарный остаток на 30 сентября 2022 г. дебет ', 'Остаток на 1 октября 2022 г. дебет',
        'Сумма на 1 октября 2022 г. дебет', 'Оборот за 4 квартал 2022 г. дебет',
        'Суммарный оборот за 4кв. дебет', 'Оборот за 4 квартал 2022 г. кредит',
        'Суммарный оборот за 4кв. кредит', 'Остаток на 31 декабря 2022 г. дебет ',
        'Суммарный остаток на 31 декабря 2022 г. дебет'
        ]

        # Переупорядочиваем столбцы
        data = data.reindex(columns=columns_titles)
        
    
    elif schN == 101 or schN == 21:

        #проход по строкам DataFrame
        for index, row in data.iterrows():
            unnamed_value = str(row['Основные средства']).strip()
            match = classifier_pattern.search(unnamed_value)
            if match:
                #оставляем только код, убирая текстовое описание
                current_classifier = match.group(1)
            elif pd.notna(row['Основные средства']) and pd.notna(row['Количество(начало периода)']) and pd.notna(row['Количество(конец периода)']):
                data.at[index, 'Классификатор'] = current_classifier

        #удаление строк, в которых 'Основные средства' является NaN
        data = data.dropna(subset=['Основные средства', 'Сальдо на начало периода, дебет',
                               'Продукт, в интересах которого осуществляется закупка, код']).copy()
    
    #удаление пустых строк
    data = data.dropna(how='all')
        
    #переиндексация, начиная с 1
    data.reset_index(drop=True, inplace=True)
    
    
    return data



#чтение CSV (ведомость остатков сч.21)

#обработка данных на основе оборотных ведомостей 2022 год

data_21_1 = pd.read_csv("21_1_2022.csv", encoding="utf-32")
data_21_2 = pd.read_csv("21_2_2022.csv", encoding="utf-32")
data_21_3 = pd.read_csv("21_3_2022.csv", encoding="utf-32")
data_21_4 = pd.read_csv("21_4_2022.csv", encoding="utf-32")

#обработка данных             сч.No  Q
data_21_1 = obrabotka(data_21_1, 21, 1)
data_21_2 = obrabotka(data_21_2, 21, 2)
data_21_3 = obrabotka(data_21_3, 21, 3)
data_21_4 = obrabotka(data_21_4, 21, 4)



#чтение CSV (ведомость остатков сч.101)

#обработка данных на основе оборотных ведомостей 2022 год

data_101_1 = pd.read_csv("101_1_2022.csv", encoding="utf-32")
data_101_2 = pd.read_csv("101_2_2022.csv", encoding="utf-32")
data_101_3 = pd.read_csv("101_3_2022.csv", encoding="utf-32")
data_101_4 = pd.read_csv("101_4_2022.csv", encoding="utf-32")

#обработка данных                сч.No  Q
data_101_1 = obrabotka(data_101_1, 101, 1)
data_101_2 = obrabotka(data_101_2, 101, 2)
data_101_3 = obrabotka(data_101_3, 101, 3)
data_101_4 = obrabotka(data_101_4, 101, 4)



#чтение CSV (ведомость остатков сч.105)

#обработка данных на основе оборотных ведомостей 2022 год

data_105_1 = pd.read_csv("105_1_2022.csv", encoding="utf-32")
data_105_2 = pd.read_csv("105_2_2022.csv", encoding="utf-32")
data_105_3 = pd.read_csv("105_3_2022.csv", encoding="utf-32")
data_105_4 = pd.read_csv("105_4_2022.csv", encoding="utf-32")

#обработка данных                сч.No  Q
data_105_1 = obrabotka(data_105_1, 105, 1)
data_105_2 = obrabotka(data_105_2, 105, 2)
data_105_3 = obrabotka(data_105_3, 105, 3)
data_105_4 = obrabotka(data_105_4, 105, 4)



#ведомость остатков по счёту 21
data21_q14 = pd.concat([data_21_1, data_21_2, 
                 data_21_3, data_21_4])

data21_q14.to_csv('Оборотная ведомость сч. 21 за 2022г. .csv', index=False, encoding="utf-32")


#ведомость остатков по счёту 101
data101_q14 = pd.concat([data_101_1, data_101_2, 
                 data_101_3, data_101_4])

data101_q14.to_csv('Оборотная ведомость сч. 101 за 2022г. .csv', index=False, encoding="utf-32")


#ведомость остатков по счёту 105
data105_q14 = pd.concat([data_105_1, data_105_2, 
                 data_105_3, data_105_4])

data105_q14.to_csv('Оборотная ведомость сч. 105 за 2022г. .csv', index=False, encoding="utf-32")

#общая оборотная ведомость по всем счетам
dataedinya = pd.concat([data21_q14, data101_q14, data105_q14])
dataedinya.to_csv('Оборотная ведомость по сч. 21, 101, 105 за 2022г. .csv', index=False, encoding="utf-32")

Скрипт Преобразование_csv_в_удобный_формат(остатки).py 
Основные шаги и функции
1.	Импорт библиотек:
o	csv, os, pandas и re используются для работы с файлами CSV, обработки данных и регулярных выражений.
2.	Функция obrabotka(data, schN, date):
o	Добавляет столбцы с датой и номером счёта.
o	В зависимости от значения schN (номер счёта), выполняет различные преобразования данных.
o	Преобразует столбцы в числовой формат, удаляет ненужные столбцы, добавляет и заполняет столбец классификатора.
o	Удаляет строки, не содержащие данных о товарах, и переименовывает столбцы.
3.	Чтение и обработка данных:
o	Чтение CSV файлов с ведомостями остатков для каждого счёта (21, 101, 105) за разные даты в 2022 году.
o	Обработка данных с помощью функции obrabotka.
4.	Объединение и сохранение данных:
o	Объединение обработанных данных для каждого счёта в один DataFrame и сохранение в новые CSV файлы.
o	Объединение данных по всем счетам в один общий DataFrame и сохранение его в CSV файл.
Листинг:
import csv
import os
import pandas as pd
import re



#функция обработки данных для исследования
def obrabotka(data, schN, date):
    
    #добавление столбцов с датой и номером счёта
    data['Номер счёта'] = schN
    data['Дата'] = date    

    if schN == 105:
        #преобразование в числовой формат
        data.loc[:, 'Цена'] = pd.to_numeric(data['Цена'], errors='coerce')
        data.loc[:, 'Количество'] = pd.to_numeric(data['Количество'], errors='coerce')
        data.loc[:, 'Сумма'] = pd.to_numeric(data['Сумма'], errors='coerce')
    
        #удаление ненужных столбцов
        data.drop(columns=['Unnamed: 0'], inplace=True)
        
        #переименование столбца с номером строки
        data.rename(columns={'Unnamed: 0': 'ID'}, inplace=True)        

        #добавление столбца классификатора
        data['Классификатор'] = None

        #регулярное выражение для поиска классификаторов в формате 105.№
        classifier_pattern = re.compile(r'^\d{3}\.\d+$')

        #текущий классификатор
        current_classifier = None

        #проход по строкам DataFrame
        for index, row in data.iterrows():
            mol_value = str(row['МОЛ']).strip()
            if classifier_pattern.match(mol_value):
                current_classifier = mol_value
            elif pd.notna(row['Цена']) and pd.notna(row['Количество']) and pd.notna(row['Сумма']):
                data.at[index, 'Классификатор'] = current_classifier

        #удаление строк, которые не содержат данные о товарах
        data = data.dropna(subset=['Цена', 'Количество', 'Сумма'], how='all').reset_index(drop=True)
        data = data.dropna(subset=['Цена']).copy() #удалить NaN-значные строки
        data.rename(columns = {'МОЛ':'Основные средства'}, inplace = True)
    
    elif schN == 101:
        
        # Преобразование в числовой формат
        columns_to_numeric = [
            'Инвентарный номер', 'Амортизационная группа', 'Срок полезного использования',
            'Мес. норма износа, %', 'Износ, %', 'Балансовая стоимость', 'Количество',
            'Сумма амортизации', 'Остаточная стоимость'
        ]
        
        for col in columns_to_numeric:
            data[col] = pd.to_numeric(data[col], errors='coerce')
                   
        # Добавление столбца классификатора
        data['Классификатор'] = None

        # Регулярное выражение для поиска классификаторов в формате 101.№
        classifier_pattern = re.compile(r'^(101\.\d+)')

        # Текущий классификатор
        current_classifier = None

        # Проход по строкам DataFrame
        for index, row in data.iterrows():
            osn_sredstvo_value = str(row['Unnamed: 0']).strip()
            match = classifier_pattern.search(osn_sredstvo_value)
            if match:
                # Оставляем только код, убирая текстовое описание
                current_classifier = match.group(1)
            elif pd.notna(row['Инвентарный номер']) and pd.notna(row['Балансовая стоимость']) and pd.notna(row['Количество']):
                data.at[index, 'Классификатор'] = current_classifier

        # Удаление ненужных столбцов
        if 'Unnamed: 0' in data.columns:
            data.drop(columns=['Unnamed: 0'], inplace=True)
        
        if 'Unnamed: 0.1' in data.columns:
            data.drop(columns=['Unnamed: 0.1'], inplace=True)

        # Удаление строк, которые не содержат данные о товарах
        data = data.dropna(subset=[
            'Основное средство', 'Инвентарный номер', 'ОКОФ', 'Амортизационная группа',
            'Способ начисления амортизации', 'Дата принятия к учету', 'Состояние',
            'Срок полезного использования', 'Мес. норма износа, %', 'Износ, %',
            'Балансовая стоимость', 'Количество', 'Сумма амортизации', 'Остаточная стоимость'
        ], how='all').reset_index(drop=True)
        
        # Удаление строк, в которых 'Инвентарный номер' является NaN
        data = data.dropna(subset=['Инвентарный номер']).copy()      
        
        data.rename(columns = {'Основное средство':'Основные средства'}, inplace = True)
        
    elif schN == 21:
        # Преобразование в числовой формат
        columns_to_numeric = [
            'Инвентарный номер', 'Амортизационная группа', 'Срок полезного использования',
            'Мес. норма износа, %', 'Износ, %', 'Балансовая стоимость', 'Количество',
            'Сумма амортизации', 'Остаточная стоимость'
        ]
        
        for col in columns_to_numeric:
            data[col] = pd.to_numeric(data[col], errors='coerce')
                   
        # Добавление столбца классификатора
        data['Классификатор'] = None

        # Регулярное выражение для поиска классификаторов в формате 21.№
        classifier_pattern = re.compile(r'^(21\.\d+)')

        # Текущий классификатор
        current_classifier = None

        # Проход по строкам DataFrame
        for index, row in data.iterrows():
            osn_sredstvo_value = str(row['Unnamed: 0']).strip()
            match = classifier_pattern.search(osn_sredstvo_value)
            if match:
                # Оставляем только код, убирая текстовое описание
                current_classifier = match.group(1)
            elif pd.notna(row['Дата принятия к учету']) and pd.notna(row['Балансовая стоимость']) and pd.notna(row['Количество']):
                data.at[index, 'Классификатор'] = current_classifier

        # Удаление ненужных столбцов
        if 'Unnamed: 0' in data.columns:
            data.drop(columns=['Unnamed: 0'], inplace=True)
        
        if 'Unnamed: 0.1' in data.columns:
            data.drop(columns=['Unnamed: 0.1'], inplace=True)

        # Удаление строк, которые не содержат данные о товарах
        data = data.dropna(subset=[
            'Основное средство', 'Инвентарный номер', 'ОКОФ', 'Амортизационная группа',
            'Способ начисления амортизации', 'Дата принятия к учету', 'Состояние',
            'Срок полезного использования', 'Мес. норма износа, %', 'Износ, %',
            'Балансовая стоимость', 'Количество', 'Сумма амортизации', 'Остаточная стоимость'
        ], how='all').reset_index(drop=True)
        
        # Удаление строк, в которых 'Дата принятия к учету' является NaN
        data = data.dropna(subset=['Дата принятия к учету']).copy()  
        
        data.rename(columns = {'Основное средство':'Основные средства'}, inplace = True)

    #переиндексация, начиная с 1
    data.reset_index(drop=True, inplace=True)
    
    return data



#чтение CSV (ведомость остатков сч.21)

#обработка данных на основе ведомости остатков 
#на 31.03, 30.06, 30.09, 31.12 2022 года.

data_21_31032022 = pd.read_csv("21_31.03.2022.csv", encoding="utf-8")
data_21_30062022 = pd.read_csv("21_30.06.2022.csv", encoding="utf-8")
data_21_30092022 = pd.read_csv("21_30.09.2022.csv", encoding="utf-8")
data_21_31122022 = pd.read_csv("21_31.12.2022.csv", encoding="utf-8")

#обработка данных                             сч.No    Дата
data_21_31032022 = obrabotka(data_21_31032022, 21, "31.03.2022")
data_21_30062022 = obrabotka(data_21_30062022, 21, "30.06.2022")
data_21_30092022 = obrabotka(data_21_30092022, 21, "30.09.2022")
data_21_31122022 = obrabotka(data_21_31122022, 21, "31.12.2022")

#чтение CSV (ведомость остатков сч.101)

#обработка данных на основе ведомости остатков 
#на 31.03, 30.06, 30.09, 31.12 2022 года.

data_101_31032022 = pd.read_csv("101_31.03.2022.csv", encoding="utf-8")
data_101_30062022 = pd.read_csv("101_30.06.2022.csv", encoding="utf-8")
data_101_30092022 = pd.read_csv("101_30.09.2022.csv", encoding="utf-8")
data_101_31122022 = pd.read_csv("101_31.12.2022.csv", encoding="utf-8")

#обработка данных                               сч.No    Дата
data_101_31032022 = obrabotka(data_101_31032022, 101, "31.03.2022")
data_101_30062022 = obrabotka(data_101_30062022, 101, "30.06.2022")
data_101_30092022 = obrabotka(data_101_30092022, 101, "30.09.2022")
data_101_31122022 = obrabotka(data_101_31122022, 101, "31.12.2022")

#чтение CSV (ведомость остатков сч.105)

#обработка данных на основе ведомости остатков 
#на 31.03, 30.06, 30.09, 31.12 2022 года.

data_105_31032022 = pd.read_csv("105_31.03.2022.csv", encoding="utf-8")
data_105_30062022 = pd.read_csv("105_30.06.2022.csv", encoding="utf-8")
data_105_30092022 = pd.read_csv("105_30.09.2022.csv", encoding="utf-8")
data_105_31122022 = pd.read_csv("105_31.12.2022.csv", encoding="utf-8")

#обработка данных                               сч.No    Дата
data_105_31032022 = obrabotka(data_105_31032022, 105, "31.03.2022")
data_105_30062022 = obrabotka(data_105_30062022, 105, "30.06.2022")
data_105_30092022 = obrabotka(data_105_30092022, 105, "30.09.2022")
data_105_31122022 = obrabotka(data_105_31122022, 105, "31.12.2022")



#ведомость остатков по счёту 21
data21 = pd.concat([data_21_31032022, data_21_30062022, 
                 data_21_30092022, data_21_31122022])

data21.to_csv('Ведомость остатков сч. 21 за 2022г. .csv', index=False, encoding="utf-8-sig")

#ведомость остатков по счёту 101
data101 = pd.concat([data_101_31032022, data_101_30062022, 
                 data_101_30092022, data_101_31122022])

data101.to_csv('Ведомость остатков сч. 101 за 2022г. .csv', index=False, encoding="utf-8-sig")

#ведомость остатков по счёту 105
data105 = pd.concat([data_105_31032022, data_105_30062022, 
                 data_105_30092022, data_105_31122022])

data105.to_csv('Ведомость остатков сч. 105 за 2022г. .csv', index=False, encoding="utf-8-sig")

#общая ведомость остатков по всем счетам
dataedinya = pd.concat([data21, data101, data105])
dataedinya.to_csv('Ведомость остатков по сч. 21, 101, 105 за 2022г. .csv', index=False, encoding="utf-8-sig")


Скрипт Перенос_в_БД.py
Описание:
Этот скрипт предназначен для автоматизированного создания таблиц в базе данных PostgreSQL и загрузки данных из CSV файлов в эти таблицы. Скрипт использует библиотеки psycopg2 для работы с PostgreSQL и pandas для чтения CSV файлов. Конфигурация базы данных хранится в отдельном файле config.py.
Основные шаги выполнения скрипта
1.	Импорт библиотек и конфигурации: импортируются необходимые библиотеки и конфигурация базы данных.
2.	Определение CSV файлов: задаются пути к CSV файлам, имена таблиц и кодировки.
3.	Функции для работы с PostgreSQL:
o	get_pg_type(dtype): определяет тип данных PostgreSQL на основе типа данных pandas.
o	get_db_connection(): Устанавливает соединение с базой данных.
o	get_table_columns(conn, table_name): Получает список столбцов таблицы из базы данных.
4.	Основная функция main():
o	Устанавливает соединение с базой данных и создает курсор.
o	Для каждого CSV файла читает его структуру и создает соответствующую таблицу в базе данных.
o	Загружает данные из CSV файла в созданную таблицу.
o	Выводит список столбцов созданной таблицы.
5.	Запуск скрипта: запускает выполнение основной функции при запуске скрипта.
Листинг:
# Импорт необходимых библиотек
import psycopg2  # Библиотека для работы с PostgreSQL
import pandas as pd  # Библиотека для работы с данными, в том числе CSV файлами
from config import DATABASE  # Импорт настроек базы данных из файла config.py

# Список CSV файлов с соответствующими названиями таблиц и кодировками
csv_files = [
    ('Оборотная ведомость сч. 21 за 2022г. .csv', 'oboroty_21_2022', 'utf-32'),
    ('Оборотная ведомость сч. 101 за 2022г. .csv', 'oboroty_101_2022', 'utf-32'),
    ('Оборотная ведомость сч. 105 за 2022г. .csv', 'oboroty_105_2022', 'utf-32'),
    ('Ведомость остатков сч. 21 за 2022г. .csv', 'ostatki_21_2022', 'utf-8-sig'),
    ('Ведомость остатков сч. 101 за 2022г. .csv', 'ostatki_101_2022', 'utf-8-sig'),
    ('Ведомость остатков сч. 105 за 2022г. .csv', 'ostatki_105_2022', 'utf-8-sig')
]

# Функция для определения типа данных PostgreSQL на основе типа данных pandas
def get_pg_type(dtype):
    if dtype == 'object':
        return 'TEXT'
    elif dtype == 'int64':
        return 'NUMERIC'
    elif dtype == 'float64':
        return 'NUMERIC'
    else:
        return 'TEXT'

# Функция для установления соединения с базой данных PostgreSQL
def get_db_connection():
    conn = psycopg2.connect(
        database=DATABASE['dbname'],
        user=DATABASE['user'],
        password=DATABASE['password'],
        host=DATABASE['host'],
        port=DATABASE['port']
    )
    return conn

# Функция для получения списка столбцов таблицы из базы данных
def get_table_columns(conn, table_name):
    with conn.cursor() as cur:
        cur.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table_name}';")
        columns = cur.fetchall()
    return [column[0] for column in columns]

# Основная функция, выполняющая всю логику скрипта
def main():
    conn = None
    cur = None

    try:
        print("Подключение к базе данных...")
        conn = get_db_connection()  # Подключаемся к базе данных
        cur = conn.cursor()  # Создаем курсор для выполнения операций

        for csv_file, table_name, encoding in csv_files:
            try:
                print(f"Чтение файла {csv_file} с кодировкой {encoding}...")
                df = pd.read_csv(csv_file, nrows=1, encoding=encoding)  # Читаем CSV файл

                # Получаем названия и типы столбцов
                column_names = df.columns.tolist()
                column_types = [get_pg_type(str(df[col].dtype)) for col in df.columns]

                # Формируем запрос для создания таблицы
                create_table_query = f"CREATE TABLE {table_name} ("
                for i, (col_name, col_type) in enumerate(zip(column_names, column_types)):
                    create_table_query += f'"{col_name}" {col_type}'
                    if i < len(column_names) - 1:
                        create_table_query += ", "
                create_table_query += ");"

                print(f"Создание таблицы {table_name}...")
                cur.execute(create_table_query)  # Создаем таблицу
                conn.commit()  # Применяем изменения

                print(f"Загрузка данных в таблицу {table_name}...")
                copy_query = f"COPY {table_name} FROM STDIN WITH (FORMAT CSV, HEADER true, DELIMITER ',');"
                with open(csv_file, 'r', encoding=encoding) as f:
                    cur.copy_expert(sql=copy_query, file=f)  # Загружаем данные из CSV в таблицу
                    conn.commit()  # Применяем изменения

                print(f"Таблица {table_name} создана и данные успешно загружены из CSV в PostgreSQL!")

                # Вывод названий столбцов для созданной таблицы
                columns = get_table_columns(conn, table_name)
                print(f"Таблица {table_name} имеет столбцы: {columns}")

            except Exception as e:
                print(f"Ошибка при обработке файла {csv_file}: {e}")

    except psycopg2.Error as e:
        print("Ошибка при подключении к PostgreSQL:", e.pgcode, e.pgerror, e.diag.message_primary)

    finally:
        if cur:
            cur.close()  # Закрываем курсор
        if conn:
            conn.close()  # Закрываем соединение с базой данных

# Запуск основной функции
if __name__ == '__main__':
    main()


Скрипт Прогноз.py
Описание:
Основные шаги выполнения скрипта:
•  Импорт библиотек:
•	pandas для работы с данными.
•	matplotlib.pyplot для построения графиков.
•	numpy для вычислений.
•  Функция read_csv_with_encodings:
•	Пробует читать CSV файл с различными кодировками, возвращает DataFrame, если чтение успешно.
•  Функция search_product_in_files:
•	Ищет указанный товар в каждом из предоставленных CSV файлов.
•	Сохраняет данные по остаткам товара, если они найдены.
•  Функция calculate_consumption:
•	Рассчитывает потребление товара за каждый квартал на основе данных по остаткам.
•  Функция forecast_end_date:
•	Прогнозирует дату окончания товара, используя среднюю скорость потребления.
•  Функция plot_product_data:
•	Строит график остатков товара по времени.
•  Основной блок кода:
•	Запрашивает у пользователя имя товара.
•	Читает данные из CSV файлов и ищет товар.
•	Если данные найдены, строит график остатков, рассчитывает потребление за кварталы и прогнозирует дату окончания товара.
Листинг:
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Функция для чтения CSV файла с различными кодировками
# Пробует читать файл с каждой кодировкой по очереди, пока не найдет подходящую
def read_csv_with_encodings(file_path, encodings):
    for encoding in encodings:
        try:
            df = pd.read_csv(file_path, encoding=encoding)
            return df
        except Exception as e:
            print(f"Ошибка чтения {file_path} с кодировкой {encoding}: {e}")
    return None

# Функция для поиска товара в файлах и вывода информации
# Ищет товар в каждом из CSV файлов и собирает данные по остаткам
def search_product_in_files(product_name, csv_files):
    product_data = []  # Список для хранения данных по остаткам товара
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
            # Проверяем наличие нужных столбцов в DataFrame и ищем товар
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

# Функция для расчета потребления за каждый квартал
# Определяет разницу между начальным и конечным остатками за каждый квартал
def calculate_consumption(product_data):
    quarterly_consumption = []
    
    # Сортируем данные по дате
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
# Использует среднюю скорость потребления для прогнозирования даты окончания
def forecast_end_date(product_data):
    # Посчитаем среднее время для потребления одной единицы товара
    consumption_rates = []
    for i in range(len(product_data) - 1):
        start_date, start_value = product_data[i]
        end_date, end_value = product_data[i + 1]
        
        # Рассчитываем потребление за период
        consumption = start_value - end_value
        if consumption > 0:
            rate = (end_date - start_date) / consumption
            consumption_rates.append(rate.days)
    
    # Среднее время потребления одной единицы товара
    average_consumption_rate = np.mean(consumption_rates)
    
    if np.isnan(average_consumption_rate) or average_consumption_rate <= 0:
        print("Недостаточно данных для прогноза или неверные данные.")
        return None
    
    # Прогнозируем время до окончания товара
    last_date, last_value = product_data[-1]
    future_date = last_date + pd.DateOffset(days=int(last_value * average_consumption_rate))
    
    return future_date

# Функция для построения графика остатков
# Строит график изменения остатков товара по времени
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
    product_name = input("Введите имя товара: ")
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
        # Построение графика остатков товара
        plot_product_data(product_data)
        
        # Рассчет потребления за кварталы
        quarterly_consumption = calculate_consumption(product_data)
        
        if quarterly_consumption:
            # Вывод потребления за каждый квартал
            print("Потребление за каждый квартал:")
            for date, consumption in quarterly_consumption:
                print(f"{date.date()}: {consumption}")
            
            # Прогнозирование времени до окончания товара
            end_date = forecast_end_date(product_data)
            
            if end_date:
                print(f"Товар '{product_name}' закончится к {end_date.date()}.")
            else:
                print("Не удалось спрогнозировать дату окончания товара.")
        else:
            print("Недостаточно данных для расчета потребления.")
    else:
        print("Нет данных для построения графика и прогнозирования.")

Пример выполнения (Товар 'Бумага для офисной техники IQ Allround А3'):
 
Рисунок 1 ¬– График остатков товара
Потребление за каждый квартал:
2022-03-31: 15.0
2022-06-30: 25.0
2022-09-30: 8.0
Товар 'Бумага для офисной техники IQ Allround А3' закончится к 2023-12-12.
