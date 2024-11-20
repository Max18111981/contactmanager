from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from django.http import HttpResponse

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})

def add_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        Contact.objects.create(name=name, email=email, phone=phone)
        return redirect('contact_list')
    return render(request, 'contacts/add_contact.html')

def delete_contact(request, id):
    contact = get_object_or_404(Contact, id=id)
    contact.delete()
    return redirect('contact_list')
