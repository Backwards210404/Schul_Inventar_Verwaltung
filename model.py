import sqlite3
from typing import List

from itemstate import normalizeItems
from user import User
from item import Item
from userrole import normalizeUsers, UserRole
from department import Department
from subject import Subject
from groups import Group
from teacher import Teacher


class Model:
    def __init__(self, db_path: str = "local.db"):
        self.db_path = db_path
        self.users: List[User] = []
        self.items: List[Item] = []
        self.departments: List[Department] = []
        self.subjects: List[Subject] = []
        self.groups: List[Group] = []
        self.teachers: List[Teacher] = []
        self.load()

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
            ResponsiblePerson TEXT,
            State TEXT
        )""")
        conn.execute("""
        CREATE TABLE IF NOT EXISTS Departments (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT
        )""")
        conn.execute("""
        CREATE TABLE IF NOT EXISTS Subjects (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT
        )""")
        conn.execute("""
        CREATE TABLE IF NOT EXISTS Groups (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT
        )""")
        conn.execute("""
        CREATE TABLE IF NOT EXISTS Teachers (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            FirstName TEXT,
            LastName TEXT
        )""")
        conn.commit()

    def save(self) -> None:
        with sqlite3.connect(self.db_path) as conn:
            self._ensure_tables(conn)
            conn.execute("DELETE FROM Users")
            if self.users:
                conn.executemany(
                    "INSERT INTO Users (FirstName, LastName, UserName, Password, Role) VALUES (?, ?, ?, ?, ?)",
                    ((u.firstName, u.lastName, u.userName, u.password, u.role.value if isinstance(u.role, UserRole) else u.role) for u in self.users)
                )

            conn.execute("DELETE FROM Items")
            if self.items:
                conn.executemany(
                    "INSERT INTO Items (GroupName, Department, Subject, Location, ResponsiblePerson, State) VALUES (?, ?, ?, ?, ?, ?)",
                    ((i.group, i.department, i.subject, i.location, i.responsiblePerson.userName if isinstance(i.responsiblePerson, User) else i.responsiblePerson, i.state.value if hasattr(i.state, 'value') else i.state) for i in self.items)
                )

            conn.execute("DELETE FROM Departments")
            if self.departments:
                conn.executemany(
                    "INSERT INTO Departments (Name) VALUES (?)",
                    ((u.name) for u in self.departments)
                )
            conn.execute("DELETE FROM Subjects")
            if self.departments:
                conn.executemany(
                    "INSERT INTO Subjects (Name) VALUES (?)",
                    ((u.name) for u in self.subjects)
                )
            conn.execute("DELETE FROM Groups")
            if self.departments:
                conn.executemany(
                    "INSERT INTO Groups (Name) VALUES (?)",
                    ((u.name) for u in self.groups)
                )
            conn.execute("DELETE FROM Teachers")
            if self.departments:
                conn.executemany(
                    "INSERT INTO Teachers (FirstName, LastName) VALUES (?,?)",
                    ((u.firstName,u.lastName) for u in self.teachers)
                )

    def load(self) -> None:
        with sqlite3.connect(self.db_path) as conn:
            self._ensure_tables(conn)

            cur = conn.execute("SELECT FirstName, LastName, UserName, Password, Role FROM Users ORDER BY Id")
            self.users = normalizeUsers([
                User(
                    firstName=row[0] or "",
                    lastName=row[1] or "",
                    userName=row[2] or "",
                    password=row[3] or "",
                    role=row[4] or ""
                )
                for row in cur.fetchall()
            ])

            cur = conn.execute("SELECT GroupName, Department, Subject, Location, ResponsiblePerson, State FROM Items ORDER BY Id")
            self.items = normalizeItems([
                Item(group=row[0], department=row[1], subject=row[2], location=row[3], responsiblePerson=row[4], state=row[5] )
                for row in cur.fetchall()
            ])


    def addUser(self, user: User) -> None:
        self.users.append(user)

    def addItem(self, item: Item) -> None:
        self.items.append(item)

    def clearUsers(self) -> None:
        self.users.clear()

    def clearItems(self) -> None:
        self.items.clear()

    def login(self, userName: str, password: str) -> User | None:
        for u in self.users:
            if u.userName == userName and u.password == password:
                return u
        return None

    def getAllResponsibiltityUserNames(self):
        self.load()
        users = self.users
        responsibilityUserNames = []
        for user in users:
            if user.role.value == UserRole.RESPONSIBLE.value:
                responsibilityUserNames.append(user.userName)
        return responsibilityUserNames
