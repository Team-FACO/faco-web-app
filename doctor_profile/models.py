from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
from datetime import datetime
from django.db.models.signals import pre_save
#from booking.models import AppointmentDetials

# Create your models here.
class Profile(models.Model):

    Male = 'Male'
    Female = 'Female'

    GENDER_CHOICES = (
        (Male, 'Male'),
        (Female, 'Female'),

    )

    ORTHOPAEDIC='ORTHOPAEDIC'
    GYNACEOLOGIST= 'GYNACEOLOGIST'
    ONCOLOGIST='ONCOLOGIST'
    NEUROLOGIST='NEUROLOGIST'

    SPECIALITY_CHOICES=(
        (ORTHOPAEDIC, 'ORTHOPAEDIC'),
        (GYNACEOLOGIST, 'GYNACEOLOGIST'),
        (ONCOLOGIST,'ONCOLOGIST'),
        (NEUROLOGIST,'NEUROLOGIST'),



    )

    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    verified=models.BooleanField(default=True)
    profile_photo=models.ImageField(upload_to='media_/profile_pic/')
    first_name=models.CharField(max_length=250)
    last_name=models.CharField(max_length=500)
    dob= models.DateField(default=date.today )
    gender=models.CharField(max_length=10, choices=GENDER_CHOICES)
    email_id=models.CharField(max_length=250)
    mobile_no=models.BigIntegerField()
    speciality=models.CharField(max_length=250, choices=SPECIALITY_CHOICES)
    qualification=models.CharField(max_length=250)
    locality=models.CharField(max_length=250)
    hospital=models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse('booking:doctor_detail',kwargs={'pk':self.pk})

    def get_absolute_url_show(self):
        return reverse('myapp:doctor_detail',kwargs={'pk':self.pk})

    def get_absolute_url_upcoming_appointments(self):
        return reverse('myapp:doctor_upcoming_appointments',kwargs={'pk':self.pk})

    def get_absolute_url_attended_appointments(self):
        return reverse('myapp:doctor_attended_appointments',kwargs={'pk':self.pk})
        
    def get_absolute_url_slot(self):
        return reverse('myapp:doctor_slot',kwargs={'pk':self.pk})
    def get_absolute_url_verify(self):
        return reverse('myapp:verify',kwargs={'pk':self.pk})

    def __str__(self):
        return str(self.id)

    def get_absolute_url_booking(self):
        return reverse('booking:enter_paitent_details',kwargs={'pk':self.pk})




class BookingDate(models.Model):
    doctor=models.ForeignKey(Profile,on_delete=models.CASCADE, null=True,blank=True)
    date=models.DateField(default=datetime.now)

    def __str__(self):
        return str(self.date)
    def get_absolute_url(self):
        return reverse('doctor_profile:create_slot',kwargs={'pk':self.pk})

class Slot(models.Model):
    TIME_CHOICES = (('08:00:00','8 am'),
                    ('09:00:00', '9 am'),
                    ('10:00:00','10 am'),
                    ('11:00:00','11 am'),
                    ('12:00:00', '12 pm'),
                    ('13:00:00','1 pm'),
                    ('14:00:00','2 pm'),
                    ('15:00:00','3 pm'),
                    ('16:00:00', '4 pm'),
                    ('17:00:00', '5 pm'),
                    ('18:00:00', '6 pm'),
                    ('19:00:00', '7 pm'),
                    ('20:00:00', '8 pm'),
                    ('21:00:00', '9 pm'),
                    ('22:00:00', '10 pm'),
                    ('23:00:00', '11 pm'),
                    ('00:00:00','12 am'),)
    doctor=models.ForeignKey(Profile,on_delete=models.CASCADE, null=True,blank=True)
    date=models.ForeignKey(BookingDate,on_delete=models.CASCADE, null=True,blank=True)
    start_time=models.CharField(max_length=200,choices=TIME_CHOICES,null=True,blank=True)
    slot_status=models.BooleanField(default=False)

    class Meta:
        unique_together = ('doctor','start_time','date')



    def __str__(self):
    	return str(self.start_time)
