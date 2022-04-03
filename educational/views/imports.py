from django.db import models
from django.db.models import Q
from educational.models import *
from django.contrib.auth.models import AbstractUser, Permission
from PIL import Image
from unidecode import unidecode
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.urls import reverse
from utils.user_checker import is_normal
