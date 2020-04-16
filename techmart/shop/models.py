from django.db import models

# Create your models here.
class banner(models.Model):
    banner_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    text = models.CharField(max_length=500)
    status = models.BooleanField()
    image = models.ImageField(upload_to='shop/banner')

    def __str__(self):
        return self.title


class product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    prize = models.IntegerField()
    image = models.ImageField(upload_to='shop/product')

    def __str__(self):
        return self.name

class contact_us(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    msg = models.CharField(max_length=500)
    status = models.BooleanField(default=0)

    def __str__(self):
        return self.email

class order(models.Model):
    order_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip = models.IntegerField(default=0)
    cnic = models.IntegerField()
    phone_number = models.IntegerField()
    status = models.BooleanField(default=0)

    def __str__(self):
        return self.name

class order_update(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    email = models.EmailField(default="")
    update_description = models.CharField(max_length=500, default="")
    update_time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return ("Id: "+str(self.order_id)+", Description: "+self.update_description[:17]+"...")
