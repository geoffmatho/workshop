from django.db import models
from django.contrib.auth import models as mod
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Workshop(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    school = models.ForeignKey('School', on_delete=models.SET_NULL, null=True)
    know_or_bring = models.TextField()
    workshop_is_for = models.TextField()
    presenter = models.ManyToManyField('User', related_name='Presenter')
    attendees = models.ManyToManyField('User', related_name='Attendee')
    campus = models.CharField(max_length=20, blank=True)
    room = models.CharField(max_length=20, blank=True)
    category = models.ForeignKey('Category', blank=True, null=True, on_delete=models.SET_NULL)
    week = models.ForeignKey('Week', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.title} at {self.school.short_name}"



class Week(models.Model):
    term = models.IntegerField()
    year = models.IntegerField(default=2020)
    start_date = models.DateField()

    def __str__(self):
        return f"Term {self.term}, {self.year}"


class School(models.Model):
    name = models.CharField(max_length=80)
    short_name = models.CharField(max_length=10)
    admin = models.ForeignKey('User', blank=True, null=True, on_delete=models.SET_NULL, related_name='administers')

    def __str__(self):
        return self.name


class Registration(models.Model):
    workshop = models.ForeignKey('Workshop', on_delete=models.CASCADE)
    attendee = models.ForeignKey('User', on_delete=models.CASCADE)


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    school = models.ForeignKey('School',  blank=True, null=True, on_delete=models.SET_NULL)
    auth_user = models.OneToOneField(mod.User, null=True, on_delete=models.CASCADE)


    '''@receiver(post_save, sender=mod.User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=mod.User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
    '''
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.school.short_name})"


class Category(models.Model):
    pass
