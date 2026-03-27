from rest_framework import permissions

class IsStudentUser(permissions.BasePermission):
    def has_permission(self, request, view):
        
        return bool(request.user and request.user.is_authenticated and request.user.is_student)


class IsCompanyOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
       
        if request.method in permissions.SAFE_METHODS:
            return True
        
        
        return bool(obj.company and obj.company.user == request.user)

class IsCompanyUserOrReadOnly(permissions.BasePermission):
    """
    Herkes ilanları görebilir (GET), ama SADECE Şirket hesapları yeni ilan açabilir (POST).
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_authenticated and getattr(request.user, 'is_company', False))