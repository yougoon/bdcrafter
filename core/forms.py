from django import forms
from .models import ProjectRequest, Subscriber, ContactMessage

class ProjectRequestForm(forms.ModelForm):
    class Meta:
        model = ProjectRequest
        fields = ['full_name', 'company_org', 'phone_number', 'email', 'project_description', 'budget']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-xl border border-gray-200 focus:border-[#01A649] focus:ring-2 focus:ring-[#01A649]/20 outline-none transition-all',
                'placeholder': 'Your full name'
            }),
            'company_org': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-xl border border-gray-200 focus:border-[#01A649] focus:ring-2 focus:ring-[#01A649]/20 outline-none transition-all',
                'placeholder': 'Your company or organization'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-xl border border-gray-200 focus:border-[#01A649] focus:ring-2 focus:ring-[#01A649]/20 outline-none transition-all',
                'placeholder': 'Your phone number'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-4 py-3 rounded-xl border border-gray-200 focus:border-[#01A649] focus:ring-2 focus:ring-[#01A649]/20 outline-none transition-all',
                'placeholder': 'Your email address'
            }),
            'project_description': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 rounded-xl border border-gray-200 focus:border-[#01A649] focus:ring-2 focus:ring-[#01A649]/20 outline-none transition-all',
                'placeholder': 'Tell us about your project...',
                'rows': 4
            }),
            'budget': forms.Select(attrs={
                'class': 'w-full px-4 py-3 rounded-xl border border-gray-200 focus:border-[#01A649] focus:ring-2 focus:ring-[#01A649]/20 outline-none transition-all bg-white'
            }),
        }
    
    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        if len(phone) < 6:
            raise forms.ValidationError("Please enter a valid phone number")
        return phone

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'bg-white text-sm rounded-l-full px-4 py-2 w-full border border-gray-200 focus:outline-none focus:border-[#01A649]',
                'placeholder': 'Enter Email Address'
            })
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-4 py-3 rounded-xl border border-gray-200 focus:border-[#01A649] outline-none', 'placeholder': 'Your name'}),
            'email': forms.EmailInput(attrs={'class': 'w-full px-4 py-3 rounded-xl border border-gray-200 focus:border-[#01A649] outline-none', 'placeholder': 'Your email'}),
            'subject': forms.TextInput(attrs={'class': 'w-full px-4 py-3 rounded-xl border border-gray-200 focus:border-[#01A649] outline-none', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'w-full px-4 py-3 rounded-xl border border-gray-200 focus:border-[#01A649] outline-none', 'placeholder': 'Your message...', 'rows': 4}),
        }
