import jwt
import requests

from random import SystemRandom
from urllib.parse import urlencode

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.urls import reverse_lazy
from oauthlib.common import UNICODE_ASCII_CHARACTER_SET


class GoogleLoginCredentials:  # pragma: no cover
    def __init__(self, client_id, client_secret, project_id):
        self.client_id = client_id
        self.client_secret = client_secret
        self.project_id = project_id


class GoogleAccessTokens:  # pragma: no cover
    def __init__(self, id_token, access_token):
        self.id_token = id_token
        self.access_token = access_token

    def decode_id_token(self):
        id_token = self.id_token
        decoded_token = jwt.decode(id_token, options={
                                   "verify_signature": False})
        return decoded_token


class GoogleLoginFlowService:  # pragma: no cover
    API_URI = reverse_lazy("callback")

    GOOGLE_AUTH_URL = "https://accounts.google.com/o/oauth2/auth"
    GOOGLE_ACCESS_TOKEN_OBTAIN_URL = "https://oauth2.googleapis.com/token"
    GOOGLE_USER_INFO_URL = "https://www.googleapis.com/oauth2/v3/userinfo"

    SCOPES = [
        "https://www.googleapis.com/auth/userinfo.email",
        "https://www.googleapis.com/auth/userinfo.profile",
        "openid",
    ]

    def __init__(self):
        self._credentials = google_login_get_credentials()

    @staticmethod
    def _generate_state_session_token(length=30, chars=UNICODE_ASCII_CHARACTER_SET):
        rand = SystemRandom()
        state = "".join(rand.choice(chars) for _ in range(length))
        return state

    def _get_redirect_uri(self):
        domain = settings.BASE_BACKEND_URL
        api_uri = self.API_URI
        redirect_uri = f"{domain}{api_uri}"
        return redirect_uri

    def get_authorization_url(self):
        redirect_uri = self._get_redirect_uri()

        state = self._generate_state_session_token()

        params = {
            "response_type": "code",
            "client_id": self._credentials.client_id,
            "redirect_uri": redirect_uri,
            "scope": " ".join(self.SCOPES),
            "state": state,
            "access_type": "offline",
            "include_granted_scopes": "true",
            "prompt": "select_account",
        }

        query_params = urlencode(params)
        authorization_url = f"{self.GOOGLE_AUTH_URL}?{query_params}"

        return authorization_url, state

    def get_tokens(self, *, code):  # pragma: no cover
        redirect_uri = self._get_redirect_uri()
        data = {
            "code": code,
            "client_id": self._credentials.client_id,
            "client_secret": self._credentials.client_secret,
            "redirect_uri": redirect_uri,
            "grant_type": "authorization_code",
        }

        response = requests.post(
            self.GOOGLE_ACCESS_TOKEN_OBTAIN_URL, data=data)

        if not response.ok:
            raise Exception(
                "Failed to obtain access token from Google.")

        tokens = response.json()
        google_tokens = GoogleAccessTokens(
            id_token=tokens["id_token"], access_token=tokens["access_token"])

        return google_tokens

    def get_user_info(self, *, google_tokens):  # pragma: no cover
        access_token = google_tokens.access_token
        response = requests.get(self.GOOGLE_USER_INFO_URL, params={
                                "access_token": access_token})

        if not response.ok:
            raise ApplicationError("Failed to obtain user info from Google.")

        return response.json()


def google_login_get_credentials():  # pragma: no cover
    client_id = settings.GOOGLE_OAUTH2_CLIENT_ID
    client_secret = settings.GOOGLE_OAUTH2_CLIENT_SECRET
    project_id = settings.GOOGLE_OAUTH2_PROJECT_ID

    if not client_id:
        raise ImproperlyConfigured("GOOGLE_OAUTH2_CLIENT_ID missing in env.")

    if not client_secret:
        raise ImproperlyConfigured(
            "GOOGLE_OAUTH2_CLIENT_SECRET missing in env.")

    if not project_id:
        raise ImproperlyConfigured("GOOGLE_OAUTH2_PROJECT_ID missing in env.")

    credentials = GoogleLoginCredentials(
        client_id=client_id, client_secret=client_secret, project_id=project_id)

    return credentials
