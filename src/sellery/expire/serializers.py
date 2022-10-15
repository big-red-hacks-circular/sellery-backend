from expire.models import Expire
from rest_framework import serializers


class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expire
        fields = (
          "id", 
          "category", 
          "fridge_lower", 
          "fridge_upper", 
          "freezer_lower", 
          "freezer_upper", 
          "pantry_lower", 
          "pantry_upper", 
          "default_pref"
        )
        read_only_fields = fields