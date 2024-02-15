from django.urls import path

from .views import HomePageView
from .views import SnackListView
from .views import SnackDetailView

urlpatterns=[
    path('', HomePageView.as_view(), name='home'),
    path('snacks/', SnackListView.as_view(), name='snack_list'), # add to urlpatterns
    path('<int:pk>/', SnackDetailView.as_view(), name='snack_detail'), # add to url
]
