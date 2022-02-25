from django.db import models
from .imports import *


def profile_image(instance, filename):
    return "%s/%s/%s" % ('profile', instance.id, filename)


def owner_image(instance, filename):
    return "%s/%s/%s" % ('document', instance.id, filename)


class User(AbstractUser):
    cellphone = models.CharField(max_length=15, unique=True, blank=True, null=True)
    TYPE = (
        (0, 'arabic'),
        (1, 'afghanistan'),
    )
    nationality = models.IntegerField(choices=TYPE, default=0)
    profile_image = models.ImageField(blank=True, null=True, upload_to=profile_image)
    father_name = models.CharField(max_length=15, null=True, blank=True)
    ancestor_name = models.CharField(max_length=15, null=True, blank=True)
    nick_name = models.CharField(max_length=15, null=True, blank=True)
    pass_number = models.CharField(max_length=25, null=True, blank=True)
    birth_date = models.DateField(auto_now_add=True)
    pass_issue_date = models.DateField(auto_now_add=True)
    pass_expiration = models.DateField(auto_now_add=True)
    place_birth = models.CharField(max_length=15, blank=True, null=True)
    place_issue = models.CharField(max_length=15, blank=True, null=True)
    whatsapp = models.CharField(max_length=15, blank=True, null=True)

    def save(self, *args, **kwargs):
        super(User, self).save()
        if self.profile_image:
            try:
                img = Image.open(self.profile_image)
                img.save(self.profile_image.path, quality=95)
            except:
                pass


class Owner_document(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    image = models.ImageField(blank=True, null=True, upload_to=owner_image)

    def save(self, *args, **kwargs):
        if self.image:
            if not self.id:
                img = self.image
                self.image = None
                super(Owner_document, self).save()
                self.image = img
            super(Owner_document, self).save()

    def __str__(self):
        return self.owner.first_name
