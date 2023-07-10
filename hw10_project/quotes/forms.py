from django.forms import ModelForm, CharField, TextInput, DateField, DateInput, ModelChoiceField, \
    ModelMultipleChoiceField, Select, SelectMultiple
from .models import Author, Quote, Tag


class AuthorForm(ModelForm):
    fullname = CharField(max_length=50, widget=TextInput(attrs={'class': 'form-control'}))
    date_born = DateField(widget=DateInput(attrs={'class': 'form-control'}))
    location_born = CharField(max_length=100, widget=TextInput(attrs={'class': 'form-control'}))
    bio = CharField(max_length=500, widget=TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Author
        fields = ('fullname', 'date_born', 'location_born', 'bio')


class TagForm(ModelForm):
    tag = CharField(max_length=25, required=True, widget=TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Tag
        fields = ['tag']


class QuoteForm(ModelForm):
    quote = CharField(max_length=1000, widget=TextInput(attrs={'class': 'form-control'}))
    author = ModelChoiceField(queryset=Author.objects.all().order_by('fullname'),
                              widget=Select(attrs={"class": "form-select"}))
    tags = ModelMultipleChoiceField(queryset=Tag.objects.all().order_by('id'),
                                    widget=SelectMultiple(attrs={"class": "form-select", "size": "7"}))

    class Meta:
        model = Quote
        fields = ['quote', 'author', 'tags']
