from django.contrib.auth.models import User
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.utils.html import mark_safe
from django.db.models.signals import post_save
from django.core.files.storage import FileSystemStorage
from django.dispatch import receiver
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from Morgan.settings import MEDIA_ROOT, MEDIA_URL

fs = FileSystemStorage(location=MEDIA_ROOT)
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

HEATING_CHOICES = (
    ('cirkó', 'Gáz(cirkó)'),
    ('központi', 'Központi'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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

    def get_estate(self):
        estate = RealEstate.objects.filter(owner=self)
        return estate

    def __str__(self):
        return self.user.username


class Favorite(models.Model):
    owner = models.ForeignKey(Profile, related_name='favorites', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.created_on


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


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
    favorite = models.BooleanField(null=True, default=False)

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
