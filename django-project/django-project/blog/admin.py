from django.contrib import admin
from .models import Member, Santri

# Register your models here.

class MemberAnggota():
  list_display = ("NAMA", "NIM", "TANGGAL_LAHIR", "ALAMAT_TINGGAL",)
  
admin.site.register(Santri)
admin.site.register(Member)