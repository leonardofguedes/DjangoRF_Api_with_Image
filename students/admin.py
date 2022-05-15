from django.contrib import admin
from students.models import Student

class Students(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'email', 'turma','foto',)
    list_display_links = ('nome', 'cpf', 'email', 'turma','foto',)
    search_fields = ('turmas',)
    list_per_page = 10


admin.site.register(Student, Students)

