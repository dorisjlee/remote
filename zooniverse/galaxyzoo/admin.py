from django.contrib import admin

# Register your models here.
from .models import Parent, Question, Round, Edge, Bulge, Bar, Pattern, Sa, Sa_num, Prominence, Tidal, Odd


admin.site.register(Question)
admin.site.register(Parent)
admin.site.register(Round)
admin.site.register(Edge)
admin.site.register(Bulge)
admin.site.register(Bar)
admin.site.register(Pattern)
admin.site.register(Sa)
admin.site.register(Sa_num)
admin.site.register(Prominence)
admin.site.register(Tidal)
admin.site.register(Odd)

