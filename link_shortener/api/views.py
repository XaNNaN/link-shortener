from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import TokenSrializer


class TokenAPIView(APIView):

    def post(self, request):
        serializer = TokenSrializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            token,status_code = serializer.create(
                validated_data=serializer.validated_data
            )
            return Response(TokenSrializer(token).data, status=status_code)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

