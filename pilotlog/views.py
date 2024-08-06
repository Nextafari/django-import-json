from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from pilotlog.models import Aircraft
from pilotlog.serializers import DynamicFieldSerializer


class AirCraftViewSet(ViewSet):
    permission_classes = [AllowAny]
    queryset = Aircraft.objects.all()

    @action(detail=False)
    def stats(self, request):
        """Return Aircrafts Statistics using model method."""
        aircrafts_stats = Aircraft.aircraft_stats(self.queryset)

        return Response(
            {
                "status": "success",
                "message": "Statistics retrieved!!!",
                "data": aircrafts_stats,
            },
            status=status.HTTP_200_OK,
        )

    def list(self, request):
        """Return Aircraft data dyanimcally based on fields specified by
        client or default specified fields in views
        """

        # comma separate params of fields the client wants returned.
        client_fields = request.query_params.get("fields")
        client_fields = (
            client_fields.split(",")
            if client_fields is not None
            else ("id", "created", "meta")
        )

        serializer = DynamicFieldSerializer(
            self.queryset, many=True, fields=("id", "created", "meta")
        )

        return Response(
            {
                "status": "success",
                "message": "Dynamic aircraft serializer retrieved.",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )
