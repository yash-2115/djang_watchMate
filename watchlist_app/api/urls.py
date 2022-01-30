from django.urls import path, include
from watchlist_app.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('stream', views.streamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('list/', views.WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>', views.WatchDetailAV.as_view(), name="movie-detail"),

    path("", include(router.urls)),

    # path('stream/', views.StreamPlatformAV.as_view(), name='platform-list'),
    # path('stream/<int:pk>', views.StreamPlatformDetailAV.as_view(), name="streamplatform-detail"),

    # path('review/', views.ReviewList.as_view(), name="review-list"),
    # path('review/<int:pk>', views.ReviewDetail.as_view(), name="review-detail")

    path('stream/<int:pk>/review-create', views.ReviewCreate.as_view(), name="streamplatform-detail"),
    path('stream/<int:pk>/review', views.ReviewList.as_view(), name="streamplatform-detail"),
    path('stream/review/<int:pk>', views.ReviewDetail.as_view(), name='review-detail'),
]