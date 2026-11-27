from django.contrib import admin

from .models import Post, Author, Tag, Comment

# Register your models here.'

class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "tags", "date") # Here make spefify the fields you want to filter in the admin panel. one thing remembre that all fields are case sensitive, so make sure you write the field name exactly as it is in the model(that you created in models.py file).
    list_display = ("title", "date", "author") # It will show the filter options at the right side of the admin panel. You can also add multiple fields in the tuple.
    prepopulated_fields = {"slug" : ("title",)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ("comment_text", "user_name", "post")

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)