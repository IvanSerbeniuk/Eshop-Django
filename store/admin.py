from django.contrib import admin

from . models import Product, Category


@admin.register(Category) #we want create pre populated field
class CategoryAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug':('name',)}

@admin.register(Product) 
class ProductAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug':('title',)}