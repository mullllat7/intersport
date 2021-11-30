from rest_framework.routers import DefaultRouter

from applications.comment.views import CommentViewSet

router = DefaultRouter()
router.register('comment', CommentViewSet)

urlpatterns = []
urlpatterns.extend(router.urls)
