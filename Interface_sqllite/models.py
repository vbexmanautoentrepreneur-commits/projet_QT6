from database import get_connection

class House:

    @staticmethod
    def add(city, address, surface, bedrooms, price):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO house
        (city, address, surface, bedrooms, price,internet_link)
        VALUES (?, ?, ?, ?, ?,?)
        """, (city, address, surface, bedrooms, price))

        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT * FROM house
        """)

        rows = cursor.fetchall()

        conn.close()
        return rows