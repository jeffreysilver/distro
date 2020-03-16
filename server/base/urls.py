from django.contrib import admin
from django.urls import include, path
from ariadne.contrib.django.views import GraphQLView

from base.graphql.global_schema import schema

urlpatterns = [
    path("admin/", admin.site.urls),
    path('graphql/', GraphQLView.as_view(schema=schema), name='graphql'),
]
