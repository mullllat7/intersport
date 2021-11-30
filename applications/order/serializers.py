from rest_framework import serializers
from applications.order.models import OrderClothes, Order


class OrderClothesSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderClothes
        fields = ('clothes', 'quantity', 'total_cost')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['clothes'] = f'{instance.clothes}'
        return representation


class OrderSerializer(serializers.ModelSerializer):
    items = OrderClothesSerializer(many=True, write_only=True, required=True)
    total_cost = serializers.DecimalField(max_digits=100, decimal_places=2, default=0)
    delivery_address = serializers.CharField(max_length=100, required=True)
    contact_number = serializers.CharField(max_length=100, required=True)
    first_name = serializers.CharField(max_length=100, required=True)

    class Meta:
        model = Order
        fields = (
            'items', 'total_cost', 'delivery_address', 'contact_number', 'first_name', 'status'
        )

    def create(self, validated_data):
        request = self.context.get('request')
        items = validated_data.pop('items')
        total_order_cost = 0
        if request.user.is_authenticated:
            validated_data['user'] = request.user
        order = Order.objects.create(**validated_data)
        for item in items:
            order_clothes = OrderClothes.objects.create(order=order,
                                                        clothes=item['clothes'],
                                                        quantity=item['quantity'])
            total_order_cost += order_clothes.total_cost
        order.total_cost = total_order_cost
        order.save()
        return order

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['clothes'] = OrderClothesSerializer(OrderClothes.objects.filter(order=instance.id), many=True).data
        return representation
