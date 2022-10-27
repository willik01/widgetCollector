from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Widget, Accessory
from .forms import CleaningForm

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

# class WidgetList(ListView):
#     model = Widget
#     template_name = 'widgets/index.html'

#     def get_queryset(self):
#       # print('st88ff: ', Widget.objects.all())
#       widgets = Widget.objects.all()
#       return widgets

def widgets_detail(request, widget_id):
    widget = Widget.objects.get(id=widget_id)
    # id_list = widget.accessories.all().values_list('id')
    # accessories_widget_doesnt_have = Widget.objects.exclude(id__in=id_list)
    cleaning_form = CleaningForm()
    return render(request, 'widgets/detail.html', { 
      'widget': widget, 
      'cleaning_form' : cleaning_form, 
      # 'accessories' : accessories_widget_doesnt_have,
    })
class WidgetCreate(CreateView):
  model = Widget
  fields = '__all__'
  success_url = '/widgets/'

class WidgetUpdate(UpdateView):
  model = Widget
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['type', 'description', 'price']

class WidgetDelete(DeleteView):
  model = Widget
  success_url = '/widgets/'

def add_cleaning(request, widget_id):
    # create a ModelForm instance using the data in request.POST
  form = CleaningForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_cleaning = form.save(commit=False)
    new_cleaning.widget_id = widget_id
    new_cleaning.save()
  return redirect('detail', widget_id=widget_id)
    
def assoc_accessory(request, widget_id, accessory_id):
  # Note that you can pass a accessories id instead of the whole accessory object
  Widget.objects.get(id=widget_id).accessories.add(accessory_id)
  return redirect('detail', widget_id=widget_id)

class AccessoryList(ListView):
  model = Accessory

class AccessoryDetail(DetailView):
  model = Accessory

class AccessoryCreate(CreateView):
  model = Accessory
  fields = '__all__'

class AccessoryUpdate(UpdateView):
  model = Accessory
  fields = ['name', 'function']

class AccessoryDelete(DeleteView):
  model = Accessory
  success_url = '/accessories/'