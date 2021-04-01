from django.shortcuts import render
from .models import FormModel
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import ContactForm
from django.contrib.messages.views import SuccessMessageMixin
from .models import Contact

class VVVVVVVV(FormView,SuccessMessageMixin):
    template_name = "contact-us.html"
    form_class = ContactForm
    success_url = reverse_lazy("asdasdasdasdas")
    success_message = "Telebiniz Alınmıştır Enkısa Sürede Donüş Yapılacaktır"

    def get_contact_form(self,**kwargs):
        context = super(),get_context_data(**kwargs)
        context["contact"] = Contact.objects.all()
        return context
        
    def form_valid(self,form):
        form.save()
        return super().form_valid(form)

   


def contact(request):
    model = Contact.objects.all()

    return render(request,"contact-us.html",{
        "contact":model,

    })
