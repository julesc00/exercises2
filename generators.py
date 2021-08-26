


class GeneralStatusView(views.APIView):
    """List general_status object."""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = self.request.user

        alert_type = "SUCCESS"
        status = [
            {
                "linked_accounts_enabled": AccountPhotovoltaicSystem.objects.filter(
                    user=user, is_active=True).count(),
                "linked_accounts_disabled": AccountPhotovoltaicSystem.objects.filter(
                    user=user, is_active=False).count(),
                "pvs_enabled": PhotovoltaicSystem.objects.filter(
                    user=user, link_account__is_active=True).count(),
                "pvs_disabled": PhotovoltaicSystem.objects.filter(
                    user=user, link_account__is_active=False).count(),
                "show_alert": "",
                "alert_data": {"alert_type": alert_type}
            }
        ]

        if status[0].get("linked_accounts_enabled") == 0 \
                and status[0].get("linked_accounts_disabled") == 0 \
                and status[0].get("pvs_enabled") == 0 \
                and status[0].get("pvs_disabled") == 0:
            status[0]["show_alert"] = True
            if status[0]["show_alert"]:
                alert_type = "DANGER"
                message = "Primero debes vincularte con un fabricante"
                status[0]["alert_data"]["alert_type"] = alert_type
                status[0]["alert_data"]["message"] = message

            else:
                alert_info = "INFO"
                message = "200"
                status[0]["alert_data"]["alert_type"] = alert_info
                status[0]["alert_data"]["message"] = message

        results = GeneralStatusSerializer(status, many=True).data

        return Response(results)