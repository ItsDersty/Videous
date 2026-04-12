from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager

class Post(models.Model):
    name = models.CharField("title", max_length=64)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name="posts")
    
    tags = TaggableManager()
    file = models.FileField("video file", upload_to="videos/%Y/%m/%d/")
    thumbnail = models.ImageField("thumbnail", upload_to="thumbs/%Y/%m/%d/", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    moderated = models.BooleanField('moderated',default=False, db_index=True)

    def __str__(self):
        return self.name
    
class Playlist(models.Model):
    name = models.CharField("title", max_length=64)
    desc = models.TextField("description",max_length=256)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name="playlists")
    
    content = models.ManyToManyField(Post,related_name="playlists", through="PlaylistPost")

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    moderated = models.BooleanField('moderated',default=False, db_index=True)
    
    def __str__(self):
        return self.name
    
class PlaylistPost(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    order = models.PositiveIntegerField("order", default=0)

    class Meta:
        ordering = ['order']
        unique_together = ('playlist', 'post')