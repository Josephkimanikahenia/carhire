from django.db import models
from datetime import datetime
# Create your models here.


class Car(models.Model):

    county_choice = {
        'KE-01', 'Baringo',
        'KE-17', 'Kisumu',
        'KE-26', 'Meru',
        'KE-13', 'Kiambu',
        'KE-40', 'Tana River',
        'KE-06', 'Embu',
        'KE-26', 'Mombasa',

    }

    features_choices = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )

    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )

    car_title = models.CharField(max_length=255)
    county = models.CharField(choices=county_choice, max_length=100)
    city = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(('year'), choices=year_choice)
    condition = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(max_length=500)
    car_photo = models.ImageField(upload_to='photos/%y/%m/%d/')
    car_photo_1 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    car_photo_2 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    car_photo_3 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    car_photo_4 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    features = models.CharField(choices=features_choices, max_length=100)
    body_style = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    interior = models.CharField(max_length=100)
    kilometer = models.IntegerField()
    doors = models.IntegerField(choices=door_choices)
    passengers = models.IntegerField()
    vin_no = models.CharField(max_length=100)
    milage = models.IntegerField()
    fuel_type = models.CharField(max_length=100)
    no_of_owners = models.CharField(max_length=100)
    is_featured = models.BooleanField(max_length=100)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
