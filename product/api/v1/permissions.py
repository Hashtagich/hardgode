from rest_framework.permissions import BasePermission, SAFE_METHODS
from users.models import Subscription
from rest_framework import status
from rest_framework.response import Response


def make_payment(request):
    if request.method == 'POST':
        amount = request.data.get('amount')
        user = request.user

        if not amount or amount <= 0:
            return Response({"error": "Invalid payment amount"}, status=status.HTTP_400_BAD_REQUEST)

        subscription = Subscription.objects.filter(user=user).first()
        if not subscription or not subscription.is_active:
            return Response({"error": "User does not have an active subscription"}, status=status.HTTP_403_FORBIDDEN)

        return Response({"success": "Payment processed successfully"}, status=status.HTTP_200_OK)

    return Response({"error": "Invalid method"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class IsStudentOrIsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (request.user.is_student or request.user.is_staff)

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or (request.user.is_student and obj.user == request.user)


class ReadOnlyOrIsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff or request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or request.method in SAFE_METHODS
