from rest_framework import serializers
from .models import Profile, RealEstate, RealEstateImages


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealEstateImages
        fields = '__all__'


class EstateSerializer(serializers.ModelSerializer):
    details = serializers.HyperlinkedIdentityField(view_name='realestate-detail', format='html')
    images = ImageSerializer(source='get_images', many=True, required=False, read_only=True)

    class Meta:
        model = RealEstate
        depth = 1
        fields = ['details', 'images', 'created', 'location', 'address', 'city', 'size', 'size_garden', 'room',
                  'room_half', 'price', 'level', 'heating']


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.HyperlinkedIdentityField(view_name='profile-detail', read_only=True)

    # estate = EstateSerializer(source='get_estate', many=True, required=False)

    class Meta:
        model = Profile
        fields = ['user']
        depth = 1
