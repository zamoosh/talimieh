from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from unidecode import unidecode
from django.contrib.auth import get_user_model
User = get_user_model()