from django.contrib import admin
from django.urls import path
from parser_app.views import Parser

urlpatterns = [
    path('admin/', admin.site.urls),
    path('find_by_part_number/<str:part_number>', Parser.as_view()),
]
