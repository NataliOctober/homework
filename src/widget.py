# src/widgets.py
from django.forms.widgets import TextInput

class CustomTextInput(TextInput):
    icon = ''

    def render(self, name, value, attrs=None, renderer=None):
        if self.icon:
            final_attrs = self.build_attrs(attrs)
            return f'<div class="input-group">' \
                   f'<span class="input-group-addon"><img src="{self.icon}" /></span>' \
                   f'{super().render(name, value, final_attrs)}</div>'
        else:
            return super().render(name, value, attrs)