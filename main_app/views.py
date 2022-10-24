from django.shortcuts import render
from .models import Widget

# fake data for testing
# class Widget: 
#   def __init__(self, name, type, description, price):
#     self.name = name
#     self.type = type
#     self.description = description
#     self.price = price

# widgets = [
#   Widget('Thing 1', 'object', '6 sided cube', 3),
#   Widget('Thing 2', 'consumer item', 'fidget spinner', 5),
#   Widget('Thing 3', 'business item', 'pencil sharpener', 23)
# ]


# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

# Add new view
def widgets_index(request):
    widgets = Widget.objects.all()
    return render(request, 'widgets/index.html', { 'widgets': widgets })

def widgets_detail(request, widget_id):
    widget = Widget.objects.get(id=widget_id)
    return render(request, 'widgets/detail.html', { 'widget': widget })
    
