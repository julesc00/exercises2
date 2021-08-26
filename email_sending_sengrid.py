from rest_framework import generics, permissions, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from sendgrid.helpers.mail import From, HtmlContent

from .models import EmailSent
from .serializers import EmailSentSerializer
from core.mailing import Mailing


class SendNotificationsViaEmailView(generics.ListCreateAPIView):

    queryset = EmailSent.objects.all().order_by("-created")
    serializer_class = EmailSentSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    MAIL_DEFINITIONS = {
        "reconnection": {"template": "mailing/reconnection_template.html"},
        "maintenance": {"template": "mailing/maintenance_template.html"},
        "post_sale": {"template": "mailing/post_sale_template.html"}
    }

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def post(self, request, *args, **kwargs):
        """Send client a reconnection, maintenance or post-sale notification."""

        post_data = self.request.data

        # Sendgrid email
        from_email = From(post_data["sender"])
        pre_emails = list(post_data["recipient"].split(" "))
        to_emails = pre_emails
        subject = post_data["subject"]
        html_content = HtmlContent(post_data["message"])

        send_email = Mailing(from_email)
        send_email.send_with_sendgrid(
            from_email,
            to_emails,
            subject,
            html_content)

        # Save email to database
        user = self.request.user
        email_object = EmailSent(user=user)
        for key, value in post_data.items():
            if hasattr(email_object, key) and key != "user":
                setattr(email_object, key, value)
                email_object.save()

        serializer = EmailSentSerializer(email_object).data

        if serializer:
            return Response(
                {"message": "El correo se ha enviado correctamente."},
                status=status.HTTP_200_OK)

        return Response(
            {"message": "Hubo un error con su información, vuelva a intentarlo."},
            status=status.HTTP_400_BAD_REQUEST)