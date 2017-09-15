class VCard(object):
    def __init__(self):
        self.tel = []
        self.email = []
        self.n = ''
        self.fn = ''

    def get_fullname(self):
        return self.fn

    def get_telephones(self):
        return self.tel

    def get_emails(self):
        return self.email

    def get_name(self):
        return self.n
