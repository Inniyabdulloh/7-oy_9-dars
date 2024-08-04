from django.contrib import admin
from users.models import User, Contact, Review
# Register your models here.

admin.site.register(User)
admin.site.register(Contact)
admin.site.register(Review)