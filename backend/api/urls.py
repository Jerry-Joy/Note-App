from django.urls import path
from .views import NoteListCreateView, NoteDetailView, CreateUserView

urlpatterns = [
    path('notes/', NoteListCreateView.as_view(), name='note-list-create'),
    path('notes/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
]
