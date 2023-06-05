import sqlite3


def is_database_locked(database_file):
    try:
        connection = sqlite3.connect(database_file)
        connection.close()
        return False
    except sqlite3.OperationalError:
        return True


# Usage
database_file = "instance/unireq.db"
is_locked = is_database_locked(database_file)
if is_locked:
    print("The database file is locked.")
else:
    print("The database file is not locked.")
