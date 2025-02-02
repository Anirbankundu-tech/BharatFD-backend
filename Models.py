from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from django.core.cache import cache
from googletrans import Translator

class FAQ(models.Model):
    LANGUAGE_CHOICES = [
        ('en', 'English'),
        ('hi', 'Hindi'),
        ('bn', 'Bengali'),
    ]

    questions=models.TextField(verbose_name=_('Question'))
    answer=RichTextField(verbose_name=_('Answer'))
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES, default='en')

    def get_translated_text(self, lang='en'):
        cache_key = f"faq_{self.id}_{lang}"
        cached_translation = cache.get(cache_key)
        if cached_translation:
            return cached_translation
        
        translator = Translator()
        translated_text = translator.translate(self.question, dest=lang).text
        cache.set(cache_key, translated_text, timeout=86400)  # Cache for 1 day
        return translated_text
    
    def __str__(self):
        return f"{self.get_translated_text()} ({self.language})"
