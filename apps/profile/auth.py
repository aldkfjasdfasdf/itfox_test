from rest_framework.authentication import BaseAuthentication
from .models import Token


class TokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get("HTTP_AUTHORIZATION")
        if token:
            token_obj = Token.objects.filter(token=token[7:]).first()
            if token_obj:
                return (token_obj.user, None)

        return None

    def authenticate_header(self, request):
        return "Token"
