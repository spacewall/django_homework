from django.contrib import admin
from django.forms import BaseInlineFormSet, ValidationError

from .models import Article, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_main_list = list()

        for form in self.forms:
            is_main_list.append(form.cleaned_data['is_main'])
        
        if is_main_list.count(True) == 1:
            return super().clean()
        else:
            raise ValidationError('Неверно указан основной тэг!')


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'published_at', 'image']
    inlines = [ScopeInline]
