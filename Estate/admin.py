from django.contrib.gis.admin import OSMGeoAdmin, register

from .models import Profile, RealEstate, RealEstateImages


@register(Profile)
class ProfileAdmin(OSMGeoAdmin):
    list_display = ('image_tag', 'user', 'search_location')
    readonly_fields = ['image_tag']


@register(RealEstate)
class EstateAdmin(OSMGeoAdmin):
    list_display = ('owner', 'created', 'location', 'city', 'address')


@register(RealEstateImages)
class EstatePictures(OSMGeoAdmin):
    pass
