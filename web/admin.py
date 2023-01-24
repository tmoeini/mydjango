from django.contrib import admin
from .models import Expense,Income,Token

# Register your models here.
class ExpenseAdmin(admin.ModelAdmin):
    list_display=('text','amount','date')
    search_fields=('text',)
    list_filter=(['date'])

admin.site.register(Expense,ExpenseAdmin)
admin.site.register(Income)
admin.site.register(Token)
