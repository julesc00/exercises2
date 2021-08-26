class PhotovoltaicSystemSerializer(serializers.ModelSerializer):
    """Serialize data for the Photovoltaic object."""

    # Return the user's username and manufacture's name instead of the ids.
    user = serializers.CharField(source="user.username", read_only=True)
    link_account = serializers.CharField(source="link_account.username", read_only=True)
    manufacture = serializers.CharField(source="manufacture.name", read_only=True)
    # address = PhotovoltaicSystemAdditionalInfoSerializer(source="address", read_only=True)

    class Meta:
        model = PhotovoltaicSystem
        fields = "__all__"
        read_only_fields = ("id",)




class PhotovoltaicSystemView(generics.ListAPIView):
    """List photovoltaic_system and paginate."""

    queryset = PhotovoltaicSystem.objects.all().order_by("-id")
    serializer_class = PhotovoltaicSystemSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = TenResultSetPagination
    filter_backends = (OrderingFilter, SearchFilter)
    filterset_class = PVSFilter
    search_fields = ("user", "contact_name", "contact_email", "contact_mobile", "link_account", "manufacture",
                     "sync_monitoring_active", "is_favourite")
    ordering = ("contact_name",)

    def get_queryset(self):
        queryset = self.queryset
        return queryset.filter(user=self.request.user)

    def get_page_number(self):
        return get_paginator_class(
            page_size=int(self.request.user.GET.get("page_size", ""))
        )

    def list_filter_alerts(self):
        queryset = self.queryset

        query_filter = {
            "user": self.request.user,
            "contact_name": queryset.filter(contact_name__icontains=""),
            "linked_installs": PhotovoltaicSystem.objects.filter(sync_monitoring_active=True),
            "tension_rates": queryset.filter(),
            "low_tension": Rates.objects.values_list("name", flat=True).filter(category__name__icontains="baja"),
            "high_tension": Rates.objects.filter(category__name__icontains="alta"),
            "other_tension": Rates.objects.filter(category__name__icontains="otra")
        }
        for field in query_filter:
            query_filter[field] = self.kwargs[field]

        return Response(self.queryset, **query_filter)


# Sunday
class PhotovoltaicSystemView(generics.ListAPIView):
    """List photovoltaic_system and paginate."""

    queryset = PhotovoltaicSystem.objects.all().order_by("-id")
    serializer_class = PhotovoltaicSystemSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = TenResultSetPagination
    filter_backends = (OrderingFilter, SearchFilter)
    filterset_class = PVSFilter
    search_fields = ("user", "contact_name", "contact_email", "contact_mobile", "link_account", "manufacture",
                     "sync_monitoring_active", "is_favourite")
    ordering = ("contact_name",)

    def get_queryset(self):
        queryset = self.queryset
        return queryset.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        queryset = self.queryset
        context = super().get_context_data(**kwargs)
        context["address"] = PhotovoltaicSystemAdditionalInfo.objects.distinct("address")
        queryset.union(context)

        return queryset

    def get_page_number(self):
        return get_paginator_class(
            page_size=int(self.request.user.GET.get("page_size", ""))
        )


query = {

            "address": PhotovoltaicSystemAdditionalInfo.objects.filter(pv_system__user__username="Panchito")
            .values_list("address", flat=True),
        }


# Monday

import datetime

from rest_framework import generics, permissions, views, status
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter, SearchFilter

from django_filters import rest_framework as filters

from .models import PhotovoltaicSystem
from accounts.models import AccountLinkManufacture

from .serializers import (PhotovoltaicSystemSerializer, GeneralStatusSerializer)
from .pagination import (get_paginator_class, TenResultSetPagination)


class PVSFilter(filters.FilterSet):

    class Meta:
        model = PhotovoltaicSystem
        fields = {
            "contact_name": ["icontains"],
            "contact_email": ["icontains"],
            "contact_mobile": ["icontains"],
            # "address": ["icontains"],
            # "city": ["icontains"],
            # "country_state": ["icontains"],
            # "country": ["icontains"],
            # "energy_rate": ["icontains"],
            "manufacture": ["in"],
        }
        ordering_fields = ("user", "contact_name", "contact_email", "contact_mobile",
                           "link_account", "manufacture", "sync_monitoring_active", "created")
        search_fields = ("user", "contact_name", "contact_email", "contact_mobile", "link_account",
                         "manufacture", "sync_monitoring_active", "is_favourite", "created")


class PhotovoltaicSystemView(generics.ListAPIView):
    """List photovoltaic_system and paginate."""

    queryset = PhotovoltaicSystem.objects.all().order_by("-id")
    serializer_class = PhotovoltaicSystemSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = TenResultSetPagination
    filter_backends = (OrderingFilter, SearchFilter)
    filterset_class = PVSFilter
    search_fields = ("user", "contact_name", "contact_email", "contact_mobile",
                     "link_account", "manufacture", "sync_monitoring_active",
                     "is_favourite")
    ordering = ("contact_name",)

    def get_queryset(self):
        queryset = self.queryset
        return queryset.filter(user=self.request.user)

    def get_page_number(self):
        return get_paginator_class(
            page_size=int(self.request.user.GET.get("page_size", ""))
        )


class GeneralStatusView(views.APIView):
    """List general_status object."""
    permission_classes = [permissions.IsAuthenticated]

    FREE_TRIAL_EXPIRED = 'Tu periodo de prueba del servicio de monitoreo ha finalizado.'

    def get(self, request):
        user = self.request.user

        alert_type = "SUCCESS"
        status = {
            "linked_accounts_enabled": AccountLinkManufacture.objects.filter(
                user=user, is_active=True).count(),
            "linked_accounts_disabled": AccountLinkManufacture.objects.filter(
                user=user, is_active=False).count(),
            "pvs_enabled": PhotovoltaicSystem.objects.filter(
                user=user, link_account__is_active=True).count(),
            "pvs_disabled": PhotovoltaicSystem.objects.filter(
                user=user, link_account__is_active=False).count(),
            "show_alert": "",
            "alert_data": {"alert_type": alert_type}
        }

        has_linked_accounts = status.get("linked_accounts_enabled") and status.get("linked_accounts_disabled")
        has_pvs = status.get("pvs_enabled") and status.get("pvs_disabled")

        if not has_linked_accounts and not has_pvs:
            alert_data = {
                "alert_type": "DANGER",
                "message": "Primero debes vincularte con un fabricante."
            }
            status = {**status, "show_alert": True, "alert_data": alert_data}

        results = GeneralStatusSerializer(status).data

        return Response(results)

    def create_new_installation_alert(self, user_id, *args, **kwargs):
        """
        Create a new installation alert based on free-trial or installation
        count expiration.
        """

        wallet = self.request.user.RelatedWallet.first()
        expired_free_trail = datetime.datetime.now() >= wallet.free_trial_end_date
        not_allow_free_trial_installations = wallet.free_trial_installation_number == 0

        if not_allow_free_trial_installations or expired_free_trail:
            return Response(self.FREE_TRIAL_EXPIRED, status=status.HTTP_200_OK)

        remaining_installs = wallet.free_trial_installation_number
        remaining_trial_days = datetime.datetime.now() - wallet.free_trial_end_date
        active_time = f"Usted cuenta con {remaining_installs} instalaciones o {remaining_trial_days} días."
        remaining_active_data = {"message": active_time}

        return Response(remaining_active_data, status=status.HTTP_200_OK)


# Tuesday
    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user)

        if self.request.query_params.get("contact_name"):
            order_by = self.filterset_fields.items("contact_name")
            return queryset.filter(contact_name__icontains=order_by)
        elif self.request.query_params.get("contact_email"):
            order_by = self.filterset_fields.items("contact_email")
            return queryset.filter(contact_email__icontains=order_by)
        elif self.request.query_params.get("contact_mobile"):
            order_by = self.filterset_fields.items("contact_mobile")
            return queryset.filter(contact_mobile__icontains=order_by)
        elif self.request.query_params.get("manufacture__name"):
            order_by = self.filterset_fields.items("manufacture__name")
            return queryset.filter(manufacture__name__icontains=order_by)
        elif self.request.query_params.get("address"):
            order_by = self.filterset_fields.items(
                "link_account__photovoltaicsystem__PhotovoltaicSystemAdditionalInfoRelated__address__icontains"
            )
            return queryset.filter(
                link_account__photovoltaicsystem__PhotovoltaicSystemAdditionalInfoRelated__address__icontains=order_by
            )

        return queryset