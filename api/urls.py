from django.urls import path
from .views import *

"""
TODO:
Add the urlpatterns of the endpoints, required for implementing
Todo GET (List and Detail), PUT, PATCH and DELETE.
"""

urlpatterns = [
    path('todo/create/', TodoCreateView.as_view()),
    path('todo/list/', Todolistview.as_view()),
    path('todo/<int:id>/', TododetailView.as_view()),
    path('todo/<int:id>/add-collaborators/',addcontributorsview.as_view()),
    path('todo/<int:id>/del-collaborators/',delcontributorsview.as_view()),
    path('todo/<int:id>/listofcontributers',listofcontributers.as_view()),

    
]