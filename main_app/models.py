from django.db import models
from django.urls import reverse

CLEANING = (
  ('D', 'Dusting'),
  ('V', 'Vacuuming'),
  ('B', 'Dusting & Vacuuming'),
)

# Create your models here.

class Accessory(models.Model):
  name = models.CharField(max_length=50)
  function = models.CharField(max_length=100)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('accessories_detail', kwargs={'pk': self.id})
  
class Widget(models.Model): 
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    price = models.IntegerField()
    accessories = models.ManyToManyField(Accessory)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'widget_id':self.id})
 
class Cleaning(models.Model):
    date = models.DateField()
    c_type = models.CharField(
        'cleaning type',
        max_length=1,
        choices=CLEANING,
        default=CLEANING[2][0],
        )
    widget = models.ForeignKey(Widget, on_delete=models.CASCADE)    
    
    def __str__(self):
        return f"{self.get_c_type_display()} on {self.date}"
    
    # change the default sort
    class Meta:
        ordering = ['-date']