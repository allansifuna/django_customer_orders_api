from django.urls import path

from .apis import (
    GoogleLoginApi,
    GoogleLoginRedirectApi,
)

urlpatterns = [
    path("callback/", GoogleLoginApi.as_view(), name="callback"),
    path("redirect/", GoogleLoginRedirectApi.as_view(), name="redirect"),
]
