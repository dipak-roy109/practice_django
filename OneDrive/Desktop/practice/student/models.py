from django.db import models

# Create your models here.

# one to one 
class Person(models.Model):
    name = models.CharField(max_length = 50)
    age = models.IntegerField()

    def __self__(self):
        return self.name

class Nid(models.Model):
    person = models.OneToOneField(Person, on_delete = models.CASCADE)
    id_no = models.IntegerField()

    def __self__(self):
        return self.person

# Many to one
class Cetegory(models.Model):
    name = models.CharField(max_length = 50)

    def __self__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length = 50)
    cetegory = models.ForeignKey(Cetegory, on_delete = models.CASCADE)
    
    def __self__(self):
        return self.name

# many to many
class Group(models.Model):
    name = models.CharField(max_length = 100)
    person = models.ManyToManyField(Person)

    def __self__(self):
        return self.name