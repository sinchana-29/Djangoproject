from django import forms
class FeedBackForm(forms.Form):
	name=forms.CharField()
	rollno=forms.IntegerField()
	email=forms.EmailField()
	feedback=forms.CharField(widget=forms.Textarea)
	def clean_name(self):
		n=self.cleaned_data['name']
		if(len(n)<5):
			raise forms.ValidationError("Min no of char must be >5")
		return n
	def clean_rollno(self):
		r=self.cleaned_data['rollno']
		if r<=0:
			raise forms.ValidationError("roll no must be positive")
		return r