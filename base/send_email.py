from django.core.mail import send_mail
from django.template.loader import render_to_string
from rest_framework.response import Response
from rest_framework.views import APIView

from demo import settings


class EmailAPI(APIView):
    def get(self, request):
        subject = self.request.GET.get('subject')
        txt_ = self.request.GET.get('text')
        html_ = render_to_string("email.html", {"message": txt_})
        recipient_list = self.request.GET.get('recipient_list')
        from_email = settings.DEFAULT_FROM_EMAIL

        if subject is None and txt_ is None and html_ is None and recipient_list is None:
            return Response({'msg': 'There must be a subject, a recipient list, and either HTML or Text.'}, status=200)
        # elif html_ is not None and txt_ is not None:
        #     return Response({'msg': 'You can either use HTML or Text.'}, status=200)
        elif html_ is None and txt_ is None:
            return Response({'msg': 'Either HTML or Text is required.'}, status=200)
        elif recipient_list is None:
            return Response({'msg': 'Recipient List required.'}, status=200)
        elif subject is None:
            return Response({'msg': 'Subject required.'}, status=200)
        else:
            sent_mail = send_mail(
                subject=subject,
                from_email=from_email,
                recipient_list=recipient_list.split(','),
                message=None,
                fail_silently=False,
                html_message=html_
            )
            return Response({'msg': sent_mail}, status=200)