class BaseRole:
    def __init__(self, username):
        self.username = username

    def get_role_name(self):
        return "Base Role"


class AdminRole(BaseRole):
    def get_role_name(self):
        return "Admin"


class CustomerRole(BaseRole):
    def get_role_name(self):
        return "Customer"


class DriverRole(BaseRole):
    def get_role_name(self):
        return "Driver"
