from django.db import models
from educational.models import *
from django.contrib.auth.models import AbstractUser
from PIL import Image
from unidecode import unidecode
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.urls import reverse
