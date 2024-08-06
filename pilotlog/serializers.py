from rest_framework import serializers

from pilotlog.models import Aircraft


class DynamicFieldSerializer(serializers.ModelSerializer):
    """
    Modify __init__() to only return custom fields from client/views,
    remove fields not specificed.
    """

    class Meta:
        model = Aircraft
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop("fields")

        super().__init__(*args, **kwargs)

        if fields is not None:
            # Client fields
            allowed = set(fields)

            # All fields from model
            existing = set(self.fields.keys())

            # Drop any fields that are not specified in the 'fields' parameter
            for field_name in existing - allowed:
                self.fields.pop(field_name)
