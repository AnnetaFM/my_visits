from django.contrib import admin

from .models import SalePoint, Visit, Worker


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('name', 'telephone_number',)
    search_fields = ('name',)


@admin.register(SalePoint)
class SalePointAdmin(admin.ModelAdmin):
    list_display = ('name', 'worker',)
    search_fields = ('name',)


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    readonly_fields = [field.name for field in Visit._meta.fields]
    search_fields = ('shop__name', 'shop__worker__name',)
