from django.contrib.auth.models import User
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.utils.html import mark_safe
from django.core.files.storage import FileSystemStorage
from Morgan.settings import MEDIA_ROOT, MEDIA_URL
from dotenv import load_dotenv

fs = FileSystemStorage(location=MEDIA_ROOT)

load_dotenv()
HEATING_CHOICES = (
    ('cirkó', 'Gáz(cirkó)'),
    ('központi', 'Központi'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    profile_image = models.ImageField(storage=fs, default='default.jpg')

    def image_tag(self):
        return mark_safe('<img src="' + MEDIA_URL + '%s" width="150" height="150" />' % self.profile_image)

    image_tag.short_description = 'Image'
    bio = models.TextField(max_length=500, blank=True)
    user_location = models.PointField(null=True, blank=True)
    search_location = models.PointField(null=True, blank=True)
    search_distance = models.PositiveIntegerField(null=True, blank=True, editable=True, help_text="kilometer")
    # Todo user_location can come from address + city google api call
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=50, null=True)
    ip_address = models.GenericIPAddressField(null=True)
    ip_location = models.PointField(null=True, blank=True)

    class Meta:
        unique_together = (('user', 'ip_address'),('user', 'address'))

    def get_estate(self):
        estate = RealEstate.objects.filter(owner=self)
        return estate

    def __str__(self):
        return self.user.username


class RealEstate(models.Model):
    owner = models.OneToOneField(Profile, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)
    location = models.PointField(null=False, default=Point())
    address = models.CharField(max_length=100, null=False, default='')
    city = models.CharField(max_length=50, null=False, default='')
    size = models.PositiveIntegerField(null=False, default=0)
    size_garden = models.PositiveIntegerField(null=False, default=0)
    room = models.PositiveIntegerField(null=False, default=0)
    room_half = models.PositiveIntegerField(null=False, default=0)
    price = models.PositiveIntegerField(null=False, default=0)
    level = models.PositiveIntegerField(null=True, default=0)
    heating = models.CharField(choices=HEATING_CHOICES, max_length=50, null=True, default='')

    def get_images(self):
        images = RealEstateImages.objects.filter(estate=self)
        return images

    def __str__(self):
        return f'{self.owner.user.username} {self.city} - {self.address}'


class RealEstateImages(models.Model):
    estate = models.ForeignKey(RealEstate, related_name="pictures", on_delete=models.CASCADE)
    position = models.PositiveSmallIntegerField(null=False, default=0)
    image = models.ImageField(upload_to=fs)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.image.url


class Liked(models.Model):
    what = models.ForeignKey(RealEstate, on_delete=models.CASCADE)
    to_who = models.ForeignKey(Profile, on_delete=models.CASCADE)
    when = models.DateTimeField(auto_now_add=True)
    returned = models.BooleanField(null=True, default=False)

    class Meta:
        unique_together = ('what', 'to_who')
