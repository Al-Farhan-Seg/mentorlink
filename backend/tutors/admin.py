from django.contrib import admin
from .models import Subject, TutorProfile, AvailabilitySlot

# Register your models here.
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ["subject_name", "subject_code"]
    search_fields = ["subject_name"]


@admin.register(TutorProfile)
class TutorProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "years_of_experience", "is_verified"]
    search_fields = ["user__username"] #double underscores let you follow relationships between models.
    list_filter = ["is_verified", "education_level"]


@admin.register(AvailabilitySlot)
class AvailabilitySlotAdmin(admin.ModelAdmin):
    list_display = ["tutor", "start_at", "end_at"]

