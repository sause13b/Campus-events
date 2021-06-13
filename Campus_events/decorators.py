from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper(request):
        if request.user.is_authenticated:
            return redirect('map')
        else:
            return view_func(request)
    return wrapper
