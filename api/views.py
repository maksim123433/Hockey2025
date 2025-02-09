from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import ClubSerializer
from clubs.models import Clubs
from api.serializers import ProuserSerializer, MatchSerializer
from authorization.models import ProUser
from matches.models import Matches


class ClubListAPI(APIView):
    def get(self, request, format=None):
        clubs = Clubs.objects.all()
        serializer = ClubSerializer(clubs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ClubSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProuserApiView(APIView):
    def get(self, request, format=None):
        prousers = ProUser.objects.all()
        serializer = ProuserSerializer(prousers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProuserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MathesApiView(APIView):
    def get(self, request, format=None):
        matches = Matches.objects.all()
        serializer = MatchSerializer(matches, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

