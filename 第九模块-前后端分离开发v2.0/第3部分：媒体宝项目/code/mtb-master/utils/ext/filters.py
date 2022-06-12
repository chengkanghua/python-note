from apps.base import models
from rest_framework.filters import BaseFilterBackend


class SelfFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(mtb_user_id=request.user.user_id)
