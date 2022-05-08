from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView


class Main(APIView):
    def get(self, request):
        return render(request, "index.html")
