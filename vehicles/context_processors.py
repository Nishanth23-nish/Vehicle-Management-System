def role_permissions(request):
    user = request.user
    can_manage = False
    can_delete = False
    role_name = 'Guest'

    if user.is_authenticated:
        groups = set(user.groups.values_list('name', flat=True))
        if user.is_superuser or 'Admin' in groups:
            role_name = 'Admin'
            can_manage = True
            can_delete = True
        elif 'Staff' in groups:
            role_name = 'Staff'
            can_manage = True
        elif 'Viewer' in groups:
            role_name = 'Viewer'

    return {
        'can_manage_vehicles': can_manage,
        'can_delete_vehicles': can_delete,
        'current_role': role_name,
    }
