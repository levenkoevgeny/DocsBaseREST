from rest_framework import viewsets, mixins
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.decorators import action
from django.conf import settings

from .models import CustomUser, Region, Subdivision, CategoryItem, DocData
from .serializers import CustomUserSerializer, RegionSerializer, SubdivisionSerializer, CategoryItemSerializer, DocDataSerializer
from .serializers import ChangePasswordSerializer
from jose import jwt


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    filterset_fields = {'username': ['icontains'], 'last_name': ['icontains'], 'subdivision': ['exact'], 'is_superuser': ['exact'], 'is_staff': ['exact'], 'is_active': ['exact']}
    # permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'])
    def set_password(self, request, pk=None):
        user = self.get_object()
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.validated_data['password'])
            user.save()
            return Response({'status': 'password set'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

    def destroy(self, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SubdivisionViewSet(viewsets.ModelViewSet):
    queryset = Subdivision.objects.all()
    serializer_class = SubdivisionSerializer
    filterset_fields = {'subdivision_name': ['icontains']}
    # permission_classes = [permissions.IsAuthenticated]

    def destroy(self, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryItemViewSet(viewsets.ModelViewSet):
    queryset = CategoryItem.objects.all()
    serializer_class = CategoryItemSerializer
    filterset_fields = {'category_item_name': ['icontains'], 'parent_category': ['exact', 'isnull']}
    # permission_classes = [permissions.IsAuthenticated]

    def destroy(self, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DocDataViewSet(viewsets.ModelViewSet):
    queryset = DocData.objects.all()
    serializer_class = DocDataSerializer
    filterset_fields = {'file_name': ['icontains'], 'category': ['exact'], 'region': ['exact'], 'user': ['exact']}
    # permission_classes = [permissions.IsAuthenticated]

    def destroy(self, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_me(request):
    try:
        token = request.META['HTTP_AUTHORIZATION'].split(" ")[1]
        payload = jwt.decode(token, key=settings.SIMPLE_JWT['SIGNING_KEY'], algorithms=['HS256'])
    except jwt.JWTError:
        return Response(status=status.HTTP_403_FORBIDDEN)
    try:
        user_data = CustomUser.objects.get(pk=payload['user_id'])
        serializer = CustomUserSerializer(user_data)
        return Response(serializer.data)
    except CustomUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return Response(status=status.HTTP_400_BAD_REQUEST)