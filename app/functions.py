from app.dbConnection import *
from datetime import time

# df_partsOfRoadsByIndex = pd.read_excel("app/files/Участки_дорог_по_индексу.xlsx")
# df_dataAboutPoints = pd.read_excel("app/files/Данные_о_точках.xlsx", sheet_name = 1).dropna(axis=1, how='all')
# df_tariffs_full_w_geo = pd.read_excel("app/files/tariffs_full_w_geo.xlsx")

def get_first(index_road: int):
    ans = {}
    connection = get_connection()
    if connection is None:
        return None

    try:
        with connection:
            with connection.cursor() as cursor:
                query = """
                SELECT geoline, styleUrl
                FROM partsOfRoadsByIndex
                WHERE index_road = %s;
                """
                cursor.execute(query, (index_road, ))
                result = cursor.fetchall()

                for row in result:
                    ans = {
                        "geoline" : row[0],
                        "styleUrl" : row[1]
                    }
                return ans
    except psycopg2.Error as e:
        print(f"Ошибка при выполнении запроса: {e}")
        return None
    finally:
        connection.close()

# print(get_first(1))
    

def get_second(point_from, point_to):
    ans = {}
    connection = get_connection()
    if connection is None:
        return None

    try:
        with connection:
            with connection.cursor() as cursor:
                query = """
                SELECT zone, road, indexes
                FROM points_data
                WHERE point_from = %s
                AND point_to = %s;
                """
                cursor.execute(query, (point_from, point_to))
                result = cursor.fetchall()
                for row in result:
                    ans = {
                        "zone" : row[0],
                        "road" : row[1],
                        "indexes" : row[2]
                    }
                return ans
    except psycopg2.Error as e:
        print(f"Ошибка при выполнении запроса: {e}")
        return None
    finally:
        connection.close()

# print(get_second("Наро-Фоминское шоссе (север от М1)", "Кокошкинское шоссе"))
    
def get_third(road, day_of_week, time_range, time_start, time_end, car_type, zone, transponder, transponder_type, tariff, direction):
    connection = get_connection()
    if connection is None:
        return None

    try:
        with connection:
            with connection.cursor() as cursor:
                query = """
                SELECT price, postpay_time
                FROM tariffs_full_w_geo
                WHERE road = %s
                AND day_of_week = %s
                AND time_range = %s
                AND time_start = %s
                AND time_end = %s
                AND car_type = %s
                AND zone = %s
                AND transponder = %s
                AND transponder_type = %s
                AND tariff = %s
                AND direction = %s;
                """
                cursor.execute(query, (road, day_of_week, time_range, time.fromisoformat(time_start), time.fromisoformat(time_end), car_type, zone, transponder, transponder_type, tariff, direction))
                result = cursor.fetchall()
                return result
    except psycopg2.Error as e:
        print(f"Ошибка при выполнении запроса: {e}")
        return None
    finally:
        connection.close()

# print(get_third('проспект Багратиона (СДКП)', 'Понедельник', 'Круглосуточно', '00:00:00', '23:59:59',
#     '1 класс; Легковой транспорт', 'Весь участок (проспект Багратиона)', 'нет', None, 'Базовый', 'Все направления'))
