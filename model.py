import sqlite3
from typing import List
from user import User
from item import Item

class Model:
    def __init__(self, db_path: str = "local.db"):
        self.db_path = db_path
        self.users: List[User] = []
        self.items: List[Item] = []

    def _ensure_tables(self, conn: sqlite3.Connection) -> None:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS Users (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            FirstName TEXT,
            LastName TEXT,
            UserName TEXT UNIQUE,
            Password TEXT,
            Role TEXT
        )""")
        conn.execute("""
        CREATE TABLE IF NOT EXISTS Items (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            GroupName TEXT,
            Department TEXT,
            Subject TEXT,
            Location TEXT,
            ResponsiblePerson TEXT
        )""")
        conn.commit()

    def save(self) -> None:
        with sqlite3.connect(self.db_path) as conn:
            self._ensure_tables(conn)
            conn.execute("DELETE FROM Users")
            if self.users:
                conn.executemany(
                    "INSERT INTO Users (FirstName, LastName, UserName, Password, Role) VALUES (?, ?, ?, ?, ?)",
                    ((u.firstName, u.lastName, u.userName, u.password, u.role) for u in self.users)
                )

            conn.execute("DELETE FROM Items")
            if self.items:
                conn.executemany(
                    "INSERT INTO Items (GroupName, Department, Subject, Location, ResponsiblePerson) VALUES (?, ?, ?, ?, ?)",
                    ((i.group, i.department, i.subject, i.location, i.responsiblePerson) for i in self.items)
                )

    def load(self) -> None:
        with sqlite3.connect(self.db_path) as conn:
            self._ensure_tables(conn)

            cur = conn.execute("SELECT FirstName, LastName, UserName, Password, Role FROM Users ORDER BY Id")
            self.users = [
                User(
                    firstName=row[0] or "",
                    lastName=row[1] or "",
                    userName=row[2] or "",
                    password=row[3] or "",
                    role=row[4] or ""
                )
                for row in cur.fetchall()
            ]

            cur = conn.execute("SELECT GroupName, Department, Subject, Location, ResponsiblePerson FROM Items ORDER BY Id")
            self.items = [
                Item(group=row[0], department=row[1], subject=row[2], location=row[3], responsiblePerson=row[4])
                for row in cur.fetchall()
            ]


    def add_user(self, user: User) -> None:
        self.users.append(user)

    def add_item(self, item: Item) -> None:
        self.items.append(item)

    def clear_users(self) -> None:
        self.users.clear()

    def clear_items(self) -> None:
        self.items.clear()

    def login(self, userName: str, password: str) -> User | None:
        for u in self.users:
            if u.userName == userName and u.password == password:
                return u
        return None
