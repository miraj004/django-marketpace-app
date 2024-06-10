from django.urls import path

from . import views

app_name = 'conversation'

urlpatterns = [
    path('<int:item_pk>/new-conversation/', views.new_conversation, name='new'),
    path('conversations/', views.inbox, name='inbox'),
    path('detail/<int:pk>', views.detail, name='detail')
]





