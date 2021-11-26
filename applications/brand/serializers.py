from rest_framework import serializers

from applications.brand.models import Brand


class BrandSerializers(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if not instance.parent:
            representation.pop('parent')
        return representation
