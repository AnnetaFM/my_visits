from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import SalePoint, Visit, Worker
from .serializers import SalePointSerializer, VisitSerializer


@api_view(['GET'])
def get_sale_points(request, telephone_number):
    """Обработчик для получения торговых точек по номеру телефона работника."""
    worker = get_object_or_404(
        Worker,
        telephone_number=telephone_number
    )
    sale_points = SalePoint.objects.filter(worker=worker)
    serialized_sale_points = SalePointSerializer(sale_points, many=True)
    return Response(serialized_sale_points.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_visit(request, telephone_number):
    """ Обработчик для создания записи о посещении торговой точки."""
    serializer = VisitSerializer(data=request.data)
    if serializer.is_valid():
        sale_point = serializer.validated_data['shop']
        latitude = serializer.validated_data['latitude']
        longitude = serializer.validated_data['longitude']

        try:
            get_object_or_404(
                Worker,
                telephone_number=telephone_number,
                # visiter=sale_point
                )
        except Worker.DoesNotExist:
            return Response(
                'Данный номер не привязан к указанной торговой точке.',
                status=status.HTTP_400_BAD_REQUEST
                )
        visit = Visit.objects.create(
            shop=sale_point,
            latitude=latitude,
            longitude=longitude
            )
        return Response(
            {'Вы посетили точку': visit.pk, 'в дату:': visit.visit_datetime},
            status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
