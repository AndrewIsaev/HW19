import hashlib

from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS


class UserService:
    def __init__(self, dao):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def create(self, user_data):
        return self.dao.create(user_data)

    def update(self, user_data):
        self.dao.update(user_data)
        return self.dao

    def get_hash(self, password):
        return hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),  # Convert the password to bytes
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ).decode("utf-8", "ignore")