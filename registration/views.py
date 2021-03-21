from registration.models import NewsLetter
from django.shortcuts import render
from formApp.settings import EMAIL_HOST_USER
from .forms import NewsLetterForm
from django.core.mail import send_mail

def regform(request):
    #news = NewsLetter.objects.get()
    form = NewsLetterForm(request.POST or None)
    if form.is_valid():
        subject = 'Techy Tech'
        message = 'Welcome, Thank you for your subscription to our news'
        recepient = str(form['email'].value())
        send_mail(subject, 
        message, EMAIL_HOST_USER, 
        [recepient], fail_silently=False)
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()

        #form = NewsLetterForm()
        return render(request, 'success.html', {'recepient': recepient})
    return render(request, 'signup.html', {'form': form})

# def regform(request):
#     form = forms.SignUp()
#     if request.method == 'POST':
#         form = forms.SignUp(request.POST)
#         html = 'We have received this form before. '
#         if form.is_valid():
#             html = html + 'The form is valid'
#             form = forms.SignUp()
#     else:
#         html = 'Welcome for first time'
#     return render(request, 
#     'signup.html', {'html': html, 'form': form})

