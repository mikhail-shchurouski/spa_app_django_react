from rest_framework.views import APIView
from rest_framework.response import Response


class TestAPIView(APIView):

    def get(self, request, *args, **kwargs):
        data = [{"id": 1, "name": "Greg"},   # JSON структура данных для передачи в React
                {"id": 2, "name": "Helga"}
                ]
        return Response(data)
