from rest_framework import viewsets
from rest_framework import permissions
from .models import Blog, Post, Comment
from .serializers import BlogSerializer, PostSerializer, CommentSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class BlogViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing blog instances.
    """
    serializer_class = BlogSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # A user should only see their own blogs,
        # Unless they are a staff member, in which case they should see all blogs.
        if self.request.user.is_staff:
            return Blog.objects.all()
        return Blog.objects.filter(user=self.request.user)

class PostViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing post instances.
    """
    serializer_class = PostSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Optionally restricts the returned posts to a given blog,
        by filtering against a `blog` query parameter in the URL.
        """
        queryset = Post.objects.filter(user=self.request.user)
        blog = self.request.query_params.get('blog', None)
        if blog is not None:
            queryset = queryset.filter(blog=blog)
        return queryset

class CommentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing comment instances.
    """
    serializer_class = CommentSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(user=self.request.user)
