from django.db import models
#from django.db.models.signals import pre_save
#from django.utils.text import slugify

# from django.autoslug import AutoSlugField
from django.utils import timezone
from django.conf import settings

from django.urls import reverse

# Create your models here.


class PostManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(PostManager, self).filter(draft=False).filter(publish__lte=timezone.now())


def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)





class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=120)
    # slug = models.SlugField()
    # slug = AutoSlugField(populate_from='title', unique_with='pub_date__month')
    image = models.ImageField(upload_to=upload_location,
                              null=True, blank=True,
                              width_field='width_field',
                              height_field='height_field')

    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField()
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)


    objects=PostManager()


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('detail', kwargs={'id': self.id})


    class Meta:
        ordering = ["-timestamp", "-updated"]


# def create_slug(instance, new_slug=None):
#     slug = slugify(instance.title)
#     if new_slug is not None:
#         slug=new_slug
#     qs = Post.objects.filter(slug=slug).order_by("-id")
#
#     exists = qs.exists()
#     if exists:
#         new_slug = "%s-%s" %(slug, qs.first().id)
#         return create_slug(instance, new_slug=new_slug)
#     return slug
#
#
#
#
# def pre_save_post_receiver(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = create_slug(instance)
#
#
#
# pre_save.connect(pre_save_post_receiver, sender=Post)

