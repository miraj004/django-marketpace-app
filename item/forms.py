from django import forms

from .models import Item

INPUT_CLASS = ('bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 '
               'focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 '
               'dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500')
INPUT_ATTR = {'class': INPUT_CLASS}


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image',)
        widgets = {
            'category': forms.Select(attrs=INPUT_ATTR),
            'name': forms.TextInput(attrs=INPUT_ATTR),
            'description': forms.Textarea(attrs=INPUT_ATTR),
            'price': forms.NumberInput(attrs=INPUT_ATTR),
            'image': forms.FileInput(attrs=INPUT_ATTR)
        }


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'sold')
        widgets = {
            'name': forms.TextInput(attrs=INPUT_ATTR),
            'description': forms.Textarea(attrs=INPUT_ATTR),
            'price': forms.NumberInput(attrs=INPUT_ATTR),
            'image': forms.FileInput(attrs=INPUT_ATTR),

        }
