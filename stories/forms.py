from django import forms
from .models import Story


class StoryForm(forms.ModelForm):
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label
            
    class Meta:
        model = Story
        fields = [
            'story_title','place_name',"city_name","thumbnail","photos","nearby_places","food_to_try","precautions","things_to_try","visit_season","trip_highlights","brief_summary"
        ]