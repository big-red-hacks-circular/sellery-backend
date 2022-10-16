from food.models import Food
from rest_framework import serializers


class FoodSerializer(serializers.ModelSerializer):
    labels = serializers.SerializerMethodField("get_labels")

    def get_labels(self, food):
        return food.labels.split(",")

    class Meta:
        model = Food
        fields = (
          "id", 
          "name", 
          "labels",
        )
        read_only_fields = fields