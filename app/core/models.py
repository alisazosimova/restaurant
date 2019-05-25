from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


# Create your models here.
class MenuItem(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default="")
    description = models.TextField()
    price = models.FloatField(default=0.0)
    is_available = models.BooleanField(default=False)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Image(models.Model):
    id = models.AutoField(primary_key=True)
    menu_item_id = models.ForeignKey(MenuItem, on_delete=None)
    image = models.ImageField(upload_to="img/photo/", default="")
    image_full = ImageSpecField(source='image',
                                processors=[ResizeToFill(1920, 1080)],
                                format='JPEG',
                                options={'quality': 85})
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(375, 258)],
                                     format='JPEG',
                                     options={'quality': 85})
    alt_text = models.CharField(max_length=255, default="", blank=True)

    class Meta:
        ordering = ["alt_text"]

    def __str__(self):
        return self.alt_text


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default="")
    phone_number = models.CharField(max_length=14, default="+380")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Table(models.Model):
    id = models.AutoField(primary_key=True)
    max_seats = models.IntegerField(default=1)
    is_available = models.BooleanField(default=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return "table {}, seats {}".format(self.id, self.max_seats)


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    order_datetime = models.DateTimeField(auto_now=True)
    is_closed = models.BooleanField(default=False)

    table = models.ForeignKey(Table, on_delete=models.CASCADE, default=1)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=1)
    # menu_items = models.ManyToManyField(MenuItem)

    class Meta:
        ordering = ["-order_datetime"]

    def __str__(self):
        return "id {}, datetime {}".format(self.id, self.order_datetime)


class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25, default="")
    schedule = models.CharField(max_length=25, default="")
    # menu_items = models.ManyToManyField(MenuItem)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    review_datetime = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Customer, on_delete=models.CASCADE, default=1)
    text_review = models.TextField(default="")

    class Meta:
        ordering = ["review_datetime"]

    def __str__(self):
        return "{} {}".format(self.author_name, self.review_datetime)
