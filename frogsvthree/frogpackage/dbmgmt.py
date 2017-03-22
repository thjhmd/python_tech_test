import sqlite3
import time
import datetime
import random
from frogpackage import names_list


def create_table():
    conn = sqlite3.connect('frogsalive.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS frogtable (unix REAL, name TEXT, gender TEXT, lifecycles INT, dob TEXT, "
              "copulation TEXT)")


def create_tadpole_table():
    conn = sqlite3.connect('frogsalive.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS tadpoletable (unix REAL, name TEXT, gender TEXT, dob TEXT, father TEXT, mother TEXT)")


def dynamic_data_entry_tadpole(gender, father, mother):
    conn = sqlite3.connect('frogsalive.db')
    c = conn.cursor()

    unix = time.time()
    tadpolegender = gender
    tadpoledob = str(datetime.datetime.fromtimestamp(unix).strftime("%d-%m-%Y %H:%M:%S"))
    tadpolefather = father
    tadpolemother = mother

    if gender == "Male":
        tadpolename = random.choice(names_list.male_lon)
    else:
        tadpolename = random.choice(names_list.fem_lon)

    c. execute("INSERT INTO tadpoletable (unix, name, gender, dob, father, mother) VALUES (?, ?, ?, ?, ?, ?)",
               (unix, tadpolename, tadpolegender, tadpoledob, tadpolefather, tadpolemother))
    conn.commit()


def dynamic_data_entry(gender, copulation):
    conn = sqlite3.connect('frogsalive.db')
    c = conn.cursor()

    unix = time.time()
    froggender = gender
    froglifecycles = random.randrange(5, 10)
    frogdob = str(datetime.datetime.fromtimestamp(unix).strftime("%d-%m-%Y %H:%M:%S"))
    frogmating = random.choice(copulation)

    if gender == "Male":
        frogname = random.choice(names_list.male_lon)
    else:
        frogname = random.choice(names_list.fem_lon)

    c. execute("INSERT INTO frogtable (unix, name, gender, lifecycles, dob, copulation) VALUES (?, ?, ?, ?, ?, ?)",
               (unix, frogname, froggender, froglifecycles, frogdob, frogmating))
    conn.commit()


def read_from_table():
    conn = sqlite3.connect('frogsalive.db')
    c = conn.cursor()

    c.execute("SELECT * FROM frogtable")
    [print(row) for row in c.fetchall()]


def read_from_tadpole_table():
    conn = sqlite3.connect('frogsalive.db')
    c = conn.cursor()

    c.execute("SELECT * FROM tadpoletable")
    [print(row) for row in c.fetchall()]


def delete_all():
    conn = sqlite3.connect('frogsalive.db')
    c = conn.cursor()
    c.execute("DELETE FROM frogtable")
    conn.commit()


def update_minus_lifecycles():
    conn = sqlite3.connect('frogsalive.db')
    c = conn.cursor()
    diff_lifecycles = random.randrange(1, 3)
    c.execute("UPDATE frogtable SET lifecycles = lifecycles - (?)", (diff_lifecycles,))
    conn.commit()
    return diff_lifecycles


def update_plus_lifecycles():
    conn = sqlite3.connect('frogsalive.db')
    c = conn.cursor()
    diff_lifecycles = random.randrange(1, 3)
    c.execute("UPDATE frogtable SET lifecycles = lifecycles + (?)", (diff_lifecycles,))
    conn.commit()
    return diff_lifecycles


def delete_dead_frogs():
    conn = sqlite3.connect('frogsalive.db')
    c = conn.cursor()
    c.execute("SELECT * FROM frogtable WHERE lifecycles <= 0")
    [print(row[1] + " has passed away...") for row in c.fetchall()]
    c.execute("DELETE FROM frogtable WHERE lifecycles <= 0")
    conn.commit()


def read_by_name(name):
    conn = sqlite3.connect('frogsalive.db')
    c = conn.cursor()
    c.execute("SELECT * FROM frogtable WHERE name = (?)", (name,))
    [print(row) for row in c.fetchall()]


def read_by_gender(gender):
    conn = sqlite3.connect('frogsalive.db')
    c = conn.cursor()
    c.execute("SELECT * FROM frogtable WHERE gender = (?)", (gender,))
    [print(row) for row in c.fetchall()]


def read_by_lifecycles(lifecycles):
    conn = sqlite3.connect('frogsalive.db')
    c = conn.cursor()
    c.execute("SELECT * FROM frogtable WHERE lifecycles = (?)", (lifecycles,))
    [print(row) for row in c.fetchall()]


def read_by_copulation(copulation):
    conn = sqlite3.connect('frogsalive.db')
    c = conn.cursor()
    c.execute("SELECT * FROM frogtable WHERE copulation = (?)", (copulation,))
    [print(row) for row in c.fetchall()]


def select_male_frog_mate():
    conn = sqlite3.connect('frogsalive.db')
    c = conn.cursor()
    c.execute("SELECT * FROM frogtable WHERE gender = 'Male' AND copulation = 'Y' ORDER BY RANDOM()")
    row = c.fetchone()
    return row


def select_female_frog_mate():
    conn = sqlite3.connect('frogsalive.db')
    c = conn.cursor()
    c.execute("SELECT * FROM frogtable WHERE gender = 'Female' AND copulation = 'Y' ORDER BY RANDOM()")
    row = c.fetchone()
    return row


def check_rows_exist():
    conn = sqlite3.connect('frogsalive.db')
    c = conn.cursor()
    male_exist = False
    female_exist = False
    c.execute("SELECT * FROM frogtable WHERE gender = 'Male' AND copulation = 'Y'")
    data_male = c.fetchall()
    if len(data_male) > 0:
        male_exist = True
    c.execute("SELECT * FROM frogtable WHERE gender = 'Female' AND copulation = 'Y'")
    data_female = c.fetchall()
    if len(data_female) > 0:
        female_exist = True
    if male_exist and female_exist is True:
        return True


def close_db():
    conn = sqlite3.connect('frogsalive.db')
    c = conn.cursor()
    c.close()
    conn.close()