from .models import *


def org(request):
    if request.user.is_authenticated:
        profile_instance = profiles.objects.get(user=request.user)
        origanisers = origaniser.objects.filter(user=profile_instance)

        return {'origanisers':origanisers}
    else:
        return {}