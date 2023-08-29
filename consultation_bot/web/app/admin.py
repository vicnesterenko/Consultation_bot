from django.contrib import admin

# Register your models here.
from .models import MyTable
from .models import Question
from .models import Option
from .models import Link


admin.site.register(MyTable)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Link)
