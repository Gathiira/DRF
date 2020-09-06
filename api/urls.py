from django.urls import path

from .views import api_view, article_detail, ArticleView,ArticleDetailApiView

urlpatterns = [
    path('article/', ArticleView.as_view()),
    # path('article/', api_view),
    path('article/<int:id>/', ArticleDetailApiView.as_view()),
    # path('article/<int:id>/', article_detail),
]
