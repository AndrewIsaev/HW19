from flask import request, abort
import jwt

from constants import JWT_ALGORITHM, JWT_SECRET_KEY


def auth_required(func):
    def wrapper(*args, **kwargs):
        if "Authorization" not in request.headers:
            abort(401)

        data = request.headers["Authorization"]
        token = data.split("Bearer ")[-1]
        try:
            jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        except Exception as e:
            print(f"jwt decode error {e}")
            abort(401)
        return func(*args, **kwargs)

    return wrapper


def admin_required(func):
    def wrapper(*args, **kwargs):
        data = request.headers["Authorization"]
        token = data.split("Bearer ")[-1]
        try:
            user = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
            if user.get("role") != "admin":
                print("Authorization not required")
                abort(403)
        except Exception as e:
            print(f"jwt decode error {e}")
            abort(401)
        return func(*args, **kwargs)

    return wrapper
