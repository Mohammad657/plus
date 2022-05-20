from asyncio.windows_events import NULL
from cgitb import text
import string
from django import template
from django.db import models
from decimal import Decimal
import math

from django.forms import IntegerField

class calc(models.Model):
    number_1= models.IntegerField()
    number_2= models.IntegerField()
