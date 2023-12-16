from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
    path('user/<int:pk>', views.AuthorStories.as_view(), name='authorStories'),
    path('<int:pk>/comments', views.AddCommentView.as_view(), name='addComment'),
    path('edit/<int:pk>', views.EditStoryView.as_view(), name='edit')
]
