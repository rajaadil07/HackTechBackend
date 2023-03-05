from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.exceptions import NotFound

from .models import Newspaper
from permissions import IsStaffPermission
from .serializers import NewsPaperSerializer

class NewsPaperAPIView(generics.ListCreateAPIView):
    queryset = Newspaper.objects.all()
    serializer_class = NewsPaperSerializer
    permission_classes = [IsStaffPermission]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        newspaper_object = serializer.save()

        return Response({'message': 'Newspaper created successfully'}, status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            try:
                newspaper = self.get_queryset().get(pk=pk)
            except Newspaper.DoesNotExist:
                raise NotFound('Newspaper not found')
            serializer = self.get_serializer(newspaper)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return super().get(request, *args, **kwargs)