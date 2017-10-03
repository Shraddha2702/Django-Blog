from django.contrib import admin

# Register your models here.

from .models import Post

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title","updated","timestamp"] #To display in the admin bar, to see posts
	list_display_links = ["updated"] #To see the ones that have links and can be clicked to open
	list_editable = ["title"] #Can be edited in the bar itself by clicking, so can't have links
	list_filter = ["updated","timestamp"] #To have filters based on the current blog posts
	search_fields= ["title","content"] #To search based on fields
	
	class Meta:
		model = Post

admin.site.register(Post, PostModelAdmin)