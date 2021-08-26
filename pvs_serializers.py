
# Monday

from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import PhotovoltaicSystem
from accounts.models import AccountLinkManufacture
from manufactures.models import Manufacture


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Serialize the user object."""

    model = User
    fields = ("username",)


class AccountLinkManufactureSerializer(serializers.ModelSerializer):
    """Serialize the AccountLinkManufacture object."""

    model = AccountLinkManufacture
    fields = ("username",)


class ManufactureSerializer(serializers.ModelSerializer):
    """Serialize data for the manufacture object."""

    class Meta:
        model = Manufacture
        fields = ("name",)


class PhotovoltaicSystemSerializer(serializers.ModelSerializer):
    """Serialize data for the Photovoltaic object."""

    # Return the user's username and manufacture's name instead of the ids.
    id = serializers.IntegerField()
    user = serializers.CharField(source="user.username", read_only=True)
    link_account = serializers.CharField(source="link_account.username", read_only=True)
    manufacture = serializers.CharField(source="manufacture.name", read_only=True)

    class Meta:
        model = PhotovoltaicSystem
        fields = "__all__"
        read_only_fields = ("id",)


class GeneralStatusSerializer(serializers.Serializer):
    """Serialize data for the General Status object."""

    linked_accounts_enabled = serializers.IntegerField()
    linked_accounts_disabled = serializers.IntegerField()
    pvs_enabled = serializers.IntegerField()
    pvs_disabled = serializers.IntegerField()
    show_alert = serializers.BooleanField(default=False)
    alert_data = serializers.JSONField()
