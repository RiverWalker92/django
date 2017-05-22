from django.contrib import admin

from .models import Layout, Content, SmallContent, TeamMember



class LayoutAdmin(admin.ModelAdmin):
    list_display = ("title_id",)
    search_fields = ["title_id"]

admin.site.register(Layout, LayoutAdmin)

class SmallContentInline(admin.TabularInline):
    model = SmallContent
    extra = 6


class ContentAdmin(admin.ModelAdmin):
    list_display = ("title_id",)
    search_fields = ["title_id"]
    inlines = [SmallContentInline]

admin.site.register(Content, ContentAdmin)

class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("main_title", "id",)
    search_fields = ["main_title"]

admin.site.register(TeamMember, TeamMemberAdmin)