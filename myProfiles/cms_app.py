from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class MyProfilesApphook(CMSApp):
    name = _("Profile Apphook")
    urls = ["myProfiles.urls"]

apphook_pool.register(MyProfilesApphook)