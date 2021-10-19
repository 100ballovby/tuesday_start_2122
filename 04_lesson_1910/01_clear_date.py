"""
YYYY-MM-DD Z HH:MM - дата в таком виде хранится в БД.
Z - это часовой пояс, который может хранить значения от GMT до GMT12
Необходимо очистить данные и собрать дату в нормальный (без часового пояса).
"""
raw_date = '2021-10-19 GMT3 16:38'
c_date, c_time = raw_date[:10], raw_date[-6:]
new_date = c_date + c_time
print(new_date)