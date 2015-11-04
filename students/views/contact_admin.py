# -*- coding: utf-8 -*-
__author__ = 'sasha'
from django.shortcuts import render
from django import forms
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from studentdb.settings import ADMIN_EMAIL

class ContactForm(forms.Form):
    from_email = forms.EmailField(
        label='Ваша Емаіл Адреса'
    )

    subject = forms.CharField(
        label='Заголовок листа',
        max_length=128
    )

    message=forms.CharField(
        label='Текст повідомлення',
        max_length=2560,
        widget=forms.Textarea
    )

def contact_admin(request):
    # check if form was posted
    if request.method == 'POST':
        # create a Form instance and populate it with data from the request
        form = ContactForm(request.POST)

        # check whether user data is valid
        if form.is_valid():
            # send mail
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['from_email']

            try:
                send_mail(subject,message, from_email,[ADMIN_EMAIL])
            except Exception:
                message = 'під час відправки листа виникла ' \
                          'непередбачувана помилка.' \
                          'Спробуйте скористатися даною формою пізніше.'
            else:
                message = 'Повідомлення успішно відіслане'

            # redirect to same contact page with success message
            return HttpResponseRedirect(
                '%s?status_message=%s' % (reverse('contact_admin'), message)
            )
        # if there was not POST render blank form
        else:
            form = ContactForm()

        return render(request, 'contact_admin/form.html', {'form': form})

    return render(request, 'contact_admin/form.html')

