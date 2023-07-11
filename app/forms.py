from django import forms
g=[('male','MALE'),('female','FEMALE')]
c=[('python','PYTHON'),('java','JAVA')]
def validate_for_a(svalue):
    if svalue[0].lower()=='a':
        raise forms.ValidationError('name is starting with a')
    
def validate_for_len(name):
    if len(name)<=5:
        raise forms.ValidationError('length is less than 5')    


class StudentForm(forms.Form):
    sname=forms.CharField(max_length=100,validators=[validate_for_a,validate_for_len])
    sage=forms.IntegerField()
    email=forms.EmailField(max_length=100)
    remail=forms.EmailField(max_length=100)
    url=forms.URLField()

    botcatcher=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)

    def clean(self):
        e=self.cleaned_data['email']
        re=self.cleaned_data['remail']
        
        
        if e!=re:
            raise forms.ValidationError('both email is not matching')
    
    def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher']

        if len(bot)>0:
            raise forms.ValidationError('bot')