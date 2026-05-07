from .models import CustomUser


class UserFactory:
    """
    Factory Pattern: Kullanıcı tipine göre (student / company) doğru
    CustomUser instance'ını oluşturur. Rol atama mantığı buraya izole edilmiştir.
    """

    @staticmethod
    def create_user(user_type: str, username: str, password: str, email: str, **kwargs) -> CustomUser:
        if user_type == 'student':
            return CustomUser.objects.create_user(
                username=username,
                password=password,
                email=email,
                is_student=True,
                is_company=False,
                **kwargs
            )
        elif user_type == 'company':
            return CustomUser.objects.create_user(
                username=username,
                password=password,
                email=email,
                is_student=False,
                is_company=True,
                **kwargs
            )
        else:
            raise ValueError(f"Invalid user_type: '{user_type}'. Must be 'student' or 'company'.")
