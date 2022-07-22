from django.contrib.auth import login
from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
from .serializers import UserSerializer, RegisterSerializer, WeatherDataSerializer
from .updateDB import update
from .models import WeatherData
from threading import Thread

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

class GetWeatherInformationAPI(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self,request):
        obj = WeatherData.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(obj,request)
        serializer = WeatherDataSerializer(result_page,many=True)
        return Response(serializer.data)


# updateThread = Thread(target=update)
# updateThread.run()