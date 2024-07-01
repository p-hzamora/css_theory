import jwt
import datetime
from decouple import config

from ..models.user import User


class Auth:
    SECRET = config("JWT_KEY")


    @classmethod
    def generate_token(cls, authenticated_user: User):
        iat = datetime.datetime.now(datetime.UTC)
        payload = {
            "iat": iat.timestamp(),
            "exp": (iat + datetime.timedelta(minutes=15)).timestamp(),
            "username": authenticated_user.first_name,
            "email": authenticated_user.email,
        }

        return jwt.encode(payload, cls.SECRET, algorithm="HS256")

    @classmethod
    def verify_token(cls, headers: dict[str, str]) -> bool:
        auth = headers.get("Authorization", None)
        if not auth:
            return False

        try:
            encode_token: str = auth.removeprefix("Bearer ").lower()
            jwt.decode(encode_token, cls.SECRET, algorithms=["HS256"])
            return True
        except (jwt.ExpiredSignatureError, jwt.InvalidSignatureError):
            return False
        
