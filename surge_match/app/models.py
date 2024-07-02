from django.db import models
from django.utils import timezone

class Alert(models.Model):
    molnix_id = models.IntegerField(null=True, blank=True)
    alert_record_created_at = models.DateTimeField(default=timezone.now)
    event = models.CharField(max_length=255, null=True, blank=True)
    role_profile = models.CharField(max_length=255, null=True, blank=True)
    rotation = models.CharField(max_length=255, null=True, blank=True)
    modality = models.CharField(max_length=255, null=True, blank=True)
    language_required = models.CharField(max_length=255, null=True, blank=True)
    molnix_status = models.CharField(max_length=255, null=True, blank=True)
    alert_status = models.CharField(max_length=255, null=True, blank=True)
    opens = models.DateTimeField(null=True, blank=True)
    start = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    sectors = models.CharField(max_length=255, null=True, blank=True)
    role_tags = models.CharField(max_length=255, null=True, blank=True)
    scope = models.CharField(max_length=255, null=True, blank=True)
    im_filter = models.BooleanField(default=False)
    iso3 = models.CharField(max_length=255, null=True, blank=True)
    country_name = models.CharField(max_length=255, null=True, blank=True)
    disaster_type_id = models.IntegerField(null=True, blank=True)
    disaster_type_name = models.CharField(max_length=255, null=True, blank=True)
    disaster_go_id = models.IntegerField(null=True, blank=True)
    ifrc_severity_level_display = models.CharField(max_length=255, null=True, blank=True)
    alert_id = models.IntegerField(null=True, blank=True)
    region_id = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Alert('{self.event}', '{self.alert_status}')"

class Deployment(models.Model):
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    molnix_id = models.IntegerField(null=True, blank=True)
    surge_alert = models.ForeignKey(Alert, on_delete=models.CASCADE, related_name='deployments', db_column='alert_id')
    is_active = models.BooleanField(default=False)
    name = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    role = models.CharField(max_length=255, null=True, blank=True)
    event_name = models.CharField(max_length=255, null=True, blank=True)
    funding = models.CharField(max_length=255, null=True, blank=True)
    rotation = models.CharField(max_length=10, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Deployment('{self.name}', '{self.event_name}')"