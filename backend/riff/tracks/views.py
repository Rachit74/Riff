from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from rest_framework.parsers import MultiPartParser, FormParser

from .serializers import TrackSerializer
from .models import Track

class UploadTrackView(APIView):
    """
    Post method to handle track uploads
    """
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = TrackSerializer(data=request.data)
        if serializer.is_valid():
            # track = serializer.save(commit=False)  # Let the serializer handle other fields
            # track.artist = request.user  # Assign the artist manually
            serializer.save(artist=request.user)  # Save the track instance
            return Response('Track Uploaded', status=status.HTTP_201_CREATED)

        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return detailed errors
    
class GetAllTracks(APIView):
    def get(self, request):
        tracks = Track.objects.all()
        serializer = TrackSerializer(tracks, many=True)
        return Response(serializer.data)
