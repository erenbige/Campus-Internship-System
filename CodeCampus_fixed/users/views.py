from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import RegisterSerializer, UserProfileSerializer
from .factories import UserFactory


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_type = serializer.validated_data.pop('user_type')

        user = UserFactory.create_user(
            user_type=user_type,
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password'],
            email=serializer.validated_data.get('email', ''),
            company_name=serializer.validated_data.get('company_name', ''),
            student_skills=serializer.validated_data.get('student_skills', ''),
        )

        return Response(
            {
                "message": "User created successfully via Factory",
                "username": user.username,
                "role": user_type
            },
            status=status.HTTP_201_CREATED
        )


class MeView(APIView):
    """Giriş yapan kullanıcının profil bilgisini döner. Login sonrası rol tespiti için kullanılır."""
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)
