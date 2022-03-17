from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from .models import User
from django import forms
import csv
from import_export.admin import ImportExportActionModelAdmin

class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()


class UserAdmin(ImportExportActionModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'client_member_id', 'account_id' )
    

admin.site.register(User, UserAdmin)

