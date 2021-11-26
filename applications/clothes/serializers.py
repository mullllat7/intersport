from rest_framework import serializers

from applications.clothes.models import Clothes, ClothesImage


class ClothesImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClothesImage
        fields = ('image', )

    def _get_image_url(self, obj):
        if obj.image:
            url = obj.image.url
            request = self.context.get('request')
            if request is not None:
                url = request.build_absolute_url(url)
        else:
            url = ''
        return url

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = self._get_image_url(instance)
        return representation


class ClothesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clothes
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        total_rating = [i.rating for i in instance.review.all()]
        if len(total_rating) >0:
            representation['total_rating'] = sum(total_rating) / len(total_rating)
        representation['images'] = ClothesImageSerializer(ClothesImage.objects.filter(clothes = instance.id,), many=True , context=self.context).data
        return representation


class ClothesDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clothes
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        total_rating = [i.rating for i in instance.review.all()]
        if len(total_rating) > 0:
            representation['total_rating'] = sum(total_rating) / len(total_rating)
        representation['images'] = ClothesImageSerializer(ClothesImage.objects.filter(clothes=instance.id,), many=True, context=self.context).data
        return representation
