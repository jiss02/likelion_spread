from django.urls import path
from . import views

urlpatterns = [
    path("new/", views.new, name="new"),
    path('create/', views.create, name = 'blogcreate'),

    # 업뎃
    path('update/<int:blog_id>', views.update, name = 'blogupdate'),
    path("edit/", views.delete, name="edit"),

    # 삭제
    path('delete/<int:blog_id>', views.delete, name = 'blogdelete'),

    # 댓글
    path("comment/<int:blog_id>", views.commentcreate, name="commentcreate")
]
