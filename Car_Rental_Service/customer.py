class Customer:
    def __init__(self, driving_license, name, email):
        self.driving_license = driving_license
        self.name = name
        self.email = email

    def get_driving_license(self):
        return self.driving_license

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email
