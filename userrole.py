from enum import Enum

def normalizeUsers(users):
    for user in users:
        if not isinstance(user, UserRole):
            user.role = normalizeRoleText(user.role)

    return users

def normalizeRoleText(text):
    match text:
        case 'Verantwortlicher':
            return UserRole.RESPONSIBLE
        case 'Admin':
            return UserRole.ADMIN
        case 'Lehrer':
            return UserRole.TEACHER

        case _:
            if isinstance(text, UserRole):
                return text
            return None


class UserRole(Enum):
    RESPONSIBLE = "Verantwortlicher"
    ADMIN = "Admin"
    TEACHER = "Lehrer"


