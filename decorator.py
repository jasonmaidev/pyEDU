def requires_permission(func):
    def wrapper(user, *args, **kwargs):
        if not user.get('is_admin'):
            raise PermissionError("User does not have permission!")
        return func(user, *args, **kwargs)
    return wrapper

@requires_permission
def view_admin_dashboard(user):
    print ("Welcome to Admin dashboard")

admin_user = {'is_admin': True}
view_admin_dashboard(admin_user)