from django.contrib import admin
from .models import employer
from .models import Category
from .models import files_doc
from .models import Confirm
# Register your models here.
admin.site.register(employer)
admin.site.register(Category)
admin.site.register(files_doc)
admin.site.register(Confirm)



 