# email_api/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
from rest_framework import status

class SendEmailAPIView(APIView):
    def post(self, request):
        data = request.data
        
        email = data.get('email')
        subject = data.get('subject')
        body = data.get('body')

        if not email or not subject or not body:
            return Response({'error': 'Email, subject, and body are required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            send_mail(subject, body, 'your_email@example.com', [email])
            return Response({'message': 'Email sent successfully'})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
