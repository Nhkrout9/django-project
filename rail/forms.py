from django import forms 
from .models import Member
Berth_CHOICES= [
    ('SideUpper', 'SideUpper'),
    ('SideLower', 'SideLower'),
    ('Lower', 'Lower'),
    ('Middle', 'Middle'),
    ('Upper', 'Upper'),
    ]
sex=[('Male','M'),('Female','F')]
# creating a form 
class InputForm(forms.ModelForm): 
    class Meta:
         model = Member
         fields = "__all__"
         #class CommentForm(forms.ModelForm):
         def __init__(self, *args, **kwargs):
             super().__init__(*args, **kwargs)
             self.fields["berth_choice"].widget.attrs.update({"class": "lower","class":"upper"})
      # first_name= forms.CharField(max_length=100)
      # last_name= forms.CharField(max_length=100)
      # email= forms.EmailField()
      # age= forms.IntegerField()
      # sex=forms.CharField(label='Sex', widget=forms.Select(choices=sex))

      
    #   Berth_Choices= forms.CharField(label='Berth Choice', widget=forms.Select(choices=Berth_CHOICES))

