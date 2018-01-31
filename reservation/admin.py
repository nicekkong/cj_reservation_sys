from django.contrib import admin

# Register your models here.
from reservation.models import UserInfo, RoomInfo, ConferenceInfo, ConferenceMember

admin.site.register(UserInfo)
admin.site.register(RoomInfo)
admin.site.register(ConferenceInfo)
admin.site.register(ConferenceMember)