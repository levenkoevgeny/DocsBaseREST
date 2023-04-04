from rest_framework import viewsets, mixins
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.conf import settings

from .models import CustomUser, Subdivision, CategoryItem, DocData
from .serializers import CustomUserSerializer, SubdivisionSerializer, CategoryItemSerializer, DocDataSerializer

from jose import jwt


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    # permission_classes = [permissions.IsAuthenticated]


class SubdivisionViewSet(viewsets.ModelViewSet):
    queryset = Subdivision.objects.all()
    serializer_class = SubdivisionSerializer
    filterset_fields = {'subdivision_name': ['icontains']}
    # permission_classes = [permissions.IsAuthenticated]


class CategoryItemViewSet(viewsets.ModelViewSet):
    queryset = CategoryItem.objects.all()
    serializer_class = CategoryItemSerializer
    # permission_classes = [permissions.IsAuthenticated]


class DocDataViewSet(viewsets.ModelViewSet):
    queryset = DocData.objects.all()
    serializer_class = DocDataSerializer
    # permission_classes = [permissions.IsAuthenticated]


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_me(request):
    try:
        token = request.META['HTTP_AUTHORIZATION'].split(" ")[1]
        payload = jwt.decode(token, key=settings.SIMPLE_JWT['SIGNING_KEY'], algorithms=['HS256'])
    except jwt.JWTError:
        return Response(status=status.HTTP_403_FORBIDDEN)
    try:
        user_data = CustomUser.objects.get(user_id=payload['user_id'])
        serializer = CustomUserSerializer(user_data)
        return Response(serializer.data)
    except CustomUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return Response(status=status.HTTP_400_BAD_REQUEST)