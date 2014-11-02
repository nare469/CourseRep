from django.contrib import admin
from courses.models import Course, Resource, Vote, Topic

admin.site.register(Course)
admin.site.register(Resource)
admin.site.register(Vote)
admin.site.register(Topic)