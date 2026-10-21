from django.contrib import admin
from .models import Booking

# Register your models here
#.
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ["student", "subject", "status", "created_at"]
    search_fields = ["student__username"] #double underscores let you follow relationships between models.
    list_filter = ["status"]
