from django.http import HttpResponse
from rest_framework.views import APIView


class VersionView(APIView):
    """Returns the current version of the project"""

    def get(self, request):
        versioning_file = open("VERSION", "r")
        return HttpResponse({'version': versioning_file.read().strip()})
