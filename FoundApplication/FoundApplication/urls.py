from django.contrib import admin
from django.urls import path 
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.QuotePage.as_view()),
    path('quote/', views.QuotePage.as_view()),
    path('quotelist/',views.QuotePage.quoteList),
    path('quote/<int:id>',views.QuotePage.quoteFunctionality),
    path('quotelist/<int:id>',views.QuotePage.quoteFunctionality),
]

urlpatterns = format_suffix_patterns(urlpatterns)
