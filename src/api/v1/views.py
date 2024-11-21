import pandas as pd
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from catalog.models import Material, Category
from .serializers import MaterialSerializer, TreeSerializer, CategorySerializer


class MaterialViewSet(viewsets.ModelViewSet):
    """CRUD for materials."""

    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """CRUD for categories."""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TreeViewSet(viewsets.ReadOnlyModelViewSet):
    """Show category tree."""

    queryset = Category.objects.all()
    serializer_class = TreeSerializer


class MaterialImportView(APIView):
    def post(self, request):
        """Upload materials from excel."""
        file = request.FILES.get('file')
        if not file:
            return Response(
                {'error': 'File not found.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        data_from_file = pd.read_excel(file)
        try:
            for _, row in data_from_file.iterrows():
                Material.objects.update_or_create(
                    code=row['Код материала'],
                    defaults={
                        'name': row['Наименование материала'],
                        'price': row['Стоимость материала'],
                        'category_id': row['Category id']
                    }
                )
        except Exception as e:
            return Response(
                {
                    'error': f'Invalid format data in file.'
                             f'Error: {str(e)}'
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response({'status': 'Success upload data from file.'})
