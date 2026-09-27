from django.db import models


class Driver(models.Model):
    name = models.CharField(max_length=120)
    license_number = models.CharField(max_length=40, unique=True)
    phone = models.CharField(max_length=20)
    experience_years = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name} ({self.license_number})'


class Vehicle(models.Model):
    STATUS_AVAILABLE = 'available'
    STATUS_ASSIGNED = 'assigned'
    STATUS_MAINTENANCE = 'maintenance'

    STATUS_CHOICES = [
        (STATUS_AVAILABLE, 'Available'),
        (STATUS_ASSIGNED, 'Assigned'),
        (STATUS_MAINTENANCE, 'Maintenance'),
    ]

    vehicle_number = models.CharField(max_length=20, unique=True)
    make = models.CharField(max_length=80)
    model = models.CharField(max_length=80)
    year = models.PositiveIntegerField()
    vehicle_type = models.CharField(max_length=60)
    owner_name = models.CharField(max_length=120)
    driver = models.ForeignKey(
        Driver,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='vehicles',
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_AVAILABLE,
    )
    last_service_date = models.DateField(blank=True, null=True)
    next_service_date = models.DateField(blank=True, null=True)
    repair_notes = models.TextField(blank=True)
    service_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['vehicle_number']

    def __str__(self):
        return f'{self.vehicle_number} - {self.make} {self.model}'


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} - {self.email}'
