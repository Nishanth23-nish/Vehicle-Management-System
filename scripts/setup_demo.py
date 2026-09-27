import os
from datetime import date, timedelta
from decimal import Decimal

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vehicle_management.settings')

import django

django.setup()

from django.contrib.auth.models import Group, User
from django.core.management import call_command

from vehicles.models import Driver, Vehicle


def create_user(username, password, group_name, is_superuser=False):
    group, _ = Group.objects.get_or_create(name=group_name)
    user, _ = User.objects.get_or_create(username=username)
    user.set_password(password)
    user.is_staff = True
    user.is_superuser = is_superuser
    user.save()
    user.groups.set([group])


def create_driver(name, license_number, phone, experience_years, is_available=True):
    driver, _ = Driver.objects.update_or_create(
        license_number=license_number,
        defaults={
            'name': name,
            'phone': phone,
            'experience_years': experience_years,
            'is_available': is_available,
        },
    )
    return driver


def create_vehicle(vehicle_number, make, model, year, vehicle_type, owner_name, driver, status, days_until_service, service_cost):
    Vehicle.objects.update_or_create(
        vehicle_number=vehicle_number,
        defaults={
            'make': make,
            'model': model,
            'year': year,
            'vehicle_type': vehicle_type,
            'owner_name': owner_name,
            'driver': driver,
            'status': status,
            'last_service_date': date.today() - timedelta(days=90),
            'next_service_date': date.today() + timedelta(days=days_until_service),
            'repair_notes': 'Routine inspection completed.',
            'service_cost': Decimal(service_cost),
        },
    )


create_user('admin', 'student', 'Admin', is_superuser=True)
create_user('staff', 'staff123', 'Staff')
create_user('viewer', 'viewer123', 'Viewer')

fixture_path = os.path.join('vehicles', 'fixtures', 'vehicle_data.json')
if os.path.exists(fixture_path):
    Vehicle.objects.all().delete()
    Driver.objects.all().delete()
    call_command('loaddata', fixture_path, verbosity=1)
    print('Vehicle and driver data loaded from fixture.')
    raise SystemExit(0)

drivers = [
    create_driver('Ravi Kumar', 'DL-2024-1001', '9876543210', 7, False),
    create_driver('Meena Joseph', 'KL-2023-2245', '9876501234', 5, True),
    create_driver('Suresh Reddy', 'AP-2022-7781', '9845012345', 9, False),
    create_driver('Imran Khan', 'MH-2021-4509', '9822011122', 6, True),
    create_driver('Priya Nair', 'TN-2024-3312', '9790012345', 4, True),
]

sample_vehicles = [
    ('AP-09-QW-3344', 'Ashok Leyland', 'Dost', 2021, 'Truck', 'Logistics Team', drivers[0], Vehicle.STATUS_ASSIGNED, 20, '5200.00'),
    ('AP-31-DD-7362', 'Honda', 'City', 2018, 'Car', 'Admin Office', None, Vehicle.STATUS_MAINTENANCE, 5, '8400.00'),
    ('DL-03-VV-8800', 'Mahindra', 'XUV700', 2024, 'SUV', 'Operations', drivers[1], Vehicle.STATUS_AVAILABLE, 32, '0.00'),
    ('DL-08-XY-9101', 'Maruti Suzuki', 'Swift Dzire', 2019, 'Car', 'Field Team', drivers[2], Vehicle.STATUS_ASSIGNED, 10, '2900.00'),
    ('GJ-01-RT-9087', 'Tata', 'Nexon EV', 2024, 'Electric Car', 'Management', drivers[3], Vehicle.STATUS_AVAILABLE, 40, '0.00'),
    ('KA-05-MN-1188', 'Toyota', 'Innova', 2020, 'Van', 'Guest Transport', drivers[4], Vehicle.STATUS_ASSIGNED, 18, '4600.00'),
    ('MH-12-AA-3310', 'Eicher', 'Pro 2049', 2022, 'Truck', 'Warehouse', None, Vehicle.STATUS_MAINTENANCE, 2, '12600.00'),
    ('TN-10-BB-4421', 'Hyundai', 'Creta', 2023, 'SUV', 'Sales Team', None, Vehicle.STATUS_AVAILABLE, 55, '0.00'),
]

for vehicle in sample_vehicles:
    create_vehicle(*vehicle)

print('Demo users and vehicle data are ready.')
