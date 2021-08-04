from django.contrib import admin, messages
from .models import Person, FeedPerson, Place, Rollup, RefreshRollup
from django_object_actions import DjangoObjectActions

# Register your models here.

#### Things to test:

# * That the button is visible in the appropriate admin template
# * That the button has the correct label
# * Clicking the button triggers the RefreshRollup function and results in the RollUp being dropped and refreshed
# * Upon completion of RefreshRollup, user is redirected back to person admin screen with the appropriate success message visible in the template

class PersonAdmin(DjangoObjectActions, admin.ModelAdmin):
    
    def PushToScreens(self, request, queryset):
        RefreshRollup()
        self.message_user(request, 'Successfully pushed people to the screens!', level=messages.SUCCESS, fail_silently=False)
        print("Import button pushed")
    
    PushToScreens.label = "Push to screens"  # optional
        
    changelist_actions = ('PushToScreens', )

admin.site.register(Person, PersonAdmin)


class FeedPersonAdmin(admin.ModelAdmin):
  pass

admin.site.register(FeedPerson, FeedPersonAdmin)

class PlaceAdmin(admin.ModelAdmin):
  pass

admin.site.register(Place, PlaceAdmin)

class RollupAdmin(admin.ModelAdmin):
  pass

admin.site.register(Rollup, RollupAdmin)




# class ImportAdmin(DjangoObjectActions, admin.ModelAdmin):
#     def importer(modeladmin, request, queryset):
#         print("Import button pushed")

#     changelist_actions = ('import', )