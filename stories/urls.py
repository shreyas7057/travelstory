from django.urls import path
from .views import *

urlpatterns = [
    path('create/',create_story,name='create_story'),
    path('all/',all_story,name='all_story'),
    path('fullstory/<int:id>/',detail_story,name='detail_story'),
    path('dashboard/',traveler_dashboard,name='traveler_dashboard'),
    path('mystories/',my_stories,name='my_stories'),
]
