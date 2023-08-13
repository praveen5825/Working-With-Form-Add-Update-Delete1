from django.urls import path
from . import views

urlpatterns = [
    path('',views.show_detail),
    path('Add_new',views.Add_new),
    path('update/<int:id>',views.update_form),
    path('delete/<int:id>',views.delete_form),
]
