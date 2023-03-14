from django.db import models


class ContactDetails(models.Model):
    from_name = models.CharField(max_length=1000)
    message_received = models.CharField(max_length=1000)
    contact_number = models.IntegerField()
    reply_to = models.EmailField(max_length=254)

    def __str__(self):
        return self.name
