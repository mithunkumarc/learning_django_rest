#### To define a many-to-one relationship, use django.db.models.ForeignKey. 

read : https://github.com/mithunkumarc/learning_django_rest/tree/main/foreign_key_example



ForeignKey requires a positional argument: the class to which the model is related.

For example, if a Car model has a Manufacturer – that is, a Manufacturer makes multiple cars but each Car only has one Manufacturer – use the following definitions:

        from django.db import models

        class Manufacturer(models.Model):
            # ...
            pass

        class Car(models.Model):
            manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
            # car refer id/primary key of manufacturer
