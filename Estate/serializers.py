from rest_framework import serializers
from .models import Profile, RealEstate, RealEstateImages, Favorite, LANGUAGE_CHOICES, STYLE_CHOICES


class FavoriteSerializer(serializers.ModelSerializer):
    owner = serializers.Field(source='owner.username')

    class Meta:
        model = Favorite
        fields = ('id', 'owner', 'created_on')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealEstateImages
        fields = '__all__'


class EstateSerializer(serializers.ModelSerializer):
    details = serializers.HyperlinkedIdentityField(view_name='realestate-detail', format='html')
    images = ImageSerializer(source='get_images', many=True, required=False, read_only=True)
    user = serializers.HyperlinkedIdentityField(view_name='profile-detail', read_only=True)

    class Meta:
        model = RealEstate
        depth = 1
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.HyperlinkedIdentityField(view_name='profile-detail', read_only=True)
    favorites = FavoriteSerializer(many=True)
    estate = EstateSerializer(source='get_estate', many=True, required=False)

    class Meta:
        model = Profile
        fields = ['user', 'favorites', 'estate']
        depth = 1
