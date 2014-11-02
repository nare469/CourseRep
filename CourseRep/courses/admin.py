from django.contrib import admin
from courses.models import Course, Subscription, Resource, Vote, Topic

admin.site.register(Course)
admin.site.register(Subscription)
admin.site.register(Resource)
admin.site.register(Vote)
admin.site.register(Topic)