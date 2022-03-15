import sqlite3
from sqlite3 import Error


def create_connection():
    """CREATE a database connection to a SQLite database"""
    conn = None
    try:
        conn = sqlite3.connect("predict.db")
        return conn
    except Error as e:
        print(e)


def create_tables(conn):
    """CREATE tables"""
    sql = conn.cursor()
    sql.execute(
        """
        CREATE TABLE IF NOT EXISTS prediction(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            age INTEGER NOT NULL,
            gender INTEGER NOT NULL,
            height REAL NOT NULL,
            weight REAL NOT NULL,
            body_fat REAL NOT NULL,
            diastolic REAL NOT NULL,
            systolic REAL NOT NULL,
            gripForce INTEGER NOT NULL,
            ben_forward REAL NOT NULL,
            sit_up_counts INTEGER NOT NULL,
            broad_jump REAL NOT NULL,
            class TEXT NOT NULL
        );"""
    )

    conn.commit()
    conn.close()


def insert_data(data, predicted_class):
    """
    Insert user data and predicted value into table
    :param data:
    :param target:
    """
    conn = create_connection()
    cur = conn.cursor()
    sql_insert = """ INSERT INTO prediction
                        VALUES (?,?,?,?,
                                ?,?,?,?,
                                ?,?,?,?,?)"""

    cur.execute(
        sql_insert,
        (
            None,
            data["age"],
            data["gender"],
            data["height"],
            data["weight"],
            data["body_fat"],
            data["diastolic"],
            data["systolic"],
            data["gripForce"],
            data["ben_forward"],
            data["sit_up_counts"],
            data["broad_jump"],
            predicted_class,
        ),
    )

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_tables(create_connection())
