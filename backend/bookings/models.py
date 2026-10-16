from django.db import models
from django.conf import settings

# Create your models here.
class Booking(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = "pending", "Pending"
        CONFIRMED = "confirmed", "Confirmed"
        CANCELLED = "cancelled", "Cancelled"
        COMPLETED = "completed", "Completed"

    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    slot = models.ForeignKey(
        "tutors.AvailabilitySlot",
        on_delete=models.PROTECT
    )
    subject = models.ForeignKey(
        "tutors.Subject",
        on_delete=models.PROTECT
    )
    status = models.CharField(
        max_length=9,
        choices=StatusChoices.choices,
        default=StatusChoices.PENDING
    )
    notes = models.TextField(
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    #tutor comes from slot.tutor (not stored)

    def __str__(self):
        return f"{self.student} with {self.slot.tutor} - {self.subject} ({self.get_status_display()})"