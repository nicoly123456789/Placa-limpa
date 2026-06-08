def grupos_usuario(request):
    user = request.user

    if user.is_authenticated:
        return {
            'is_admin': user.is_superuser,
            'is_policial': user.is_superuser or user.groups.filter(name='Policial').exists(),
            'is_civil': user.is_superuser or user.groups.filter(name='Civil').exists(),
        }

    return {
        'is_admin': False,
        'is_policial': False,
        'is_civil': False,
    }