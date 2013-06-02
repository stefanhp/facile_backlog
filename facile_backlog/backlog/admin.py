from django.contrib import admin

from .models import Project, Backlog, UserStory, BacklogUserStoryAssociation


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "active", "code")
    readonly_fields = ("story_counter", )
    search_fields = ("name", "code")


class BacklogAdmin(admin.ModelAdmin):
    list_display = ("name", "project", "kind")
    fields = ("name", "description", "project", "kind")
    filter_horizontal = ['user_stories']
    search_fields = ("project__name",)


class UserStoryAdmin(admin.ModelAdmin):
    list_display = ("code", "text", "project", "theme", "status")
    readonly_fields = ("number", )
    search_fields = ("project__name", "as_a", "i_want_to", "number", "theme")


class BacklogUserStoryAssociationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Project, ProjectAdmin)
admin.site.register(Backlog, BacklogAdmin)
admin.site.register(UserStory, UserStoryAdmin)
admin.site.register(BacklogUserStoryAssociation,
                    BacklogUserStoryAssociationAdmin)
