class User:
    def __init__(self, user_id, email, password, role, status="active"):
        self.user_id = user_id
        self.email = email
        self.password = password
        self.role = role
        self.status = status

    def register(self):
        return f"User {self.email} registered."

    def login(self):
        return f"User {self.email} logged in."

    def logout(self):
        return f"User {self.email} logged out."