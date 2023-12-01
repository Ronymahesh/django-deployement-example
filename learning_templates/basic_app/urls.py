from django.urls import path
from basic_app import views

# Template Tagging
app_name = 'basic_app'

urlpatterns = [
    path('maheshtemplates/',views.maheshtemplates,name ='maheshtemplates'),
    path("other/",views.other,name="other"),

]
# Note: Please dont use Relative or Templates builtin names
