from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.views.generic.edit import FormMixin
from .forms import SignUpForm, SignInForm, ContactForm


# Create your views here.
class SignUpPage(FormMixin, TemplateView):
    """
    The sign up page for kuliahkita.com. There need to be forgot password link in this page.
    """

    template_name = "core/sign-up.html"
    form_class = SignUpForm
    success_url = reverse_lazy('sign-up-success')

    def get_context_data(self, **kwargs):
        context = super(SignUpPage, self).get_context_data(**kwargs)
        form_class = self.get_form_class()
        context['form'] = self.get_form(form_class)
        return context

    def post(self, request):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(SignUpPage, self).form_valid(form)


class SignInPage(FormMixin, TemplateView):
    """
    The sign in page for kuliahkita.com
    """

    template_name = "core/sign-in.html"
    form_class = SignInForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super(SignInPage, self).get_context_data(**kwargs)
        form_class = self.get_form_class()
        context['form'] = self.get_form(form_class)
        return context

    def post(self, request):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        # todo login logic
        username_or_email = form.cleaned_data['username_or_email']
        password = form.cleaned_data['password']
        user = authenticate(username=username_or_email, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                messages.success(self.request, 'Berhasil masuk!')
                if self.request.GET.get('next'):
                    return redirect(self.request.GET.get('next'))
                return redirect('home')
            else:
                messages.error(self.request, 'Akun sudah tidak aktif!')
        else:
            messages.error(self.request, 'Kombinasi pengguna tidak dapat ditemukan!')
        context = super(SignInPage, self).get_context_data()
        context['form'] = form
        return render(self.request, self.template_name, context)


class ContactPage(FormMixin, TemplateView):
    """
    Contact page to let User communicate to the kuliahkita.com admin
    """
    template_name = "core/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy('home')

    def post(self, request):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(ContactPage, self).get_context_data(**kwargs)
        form_class = self.get_form_class()
        context['form'] = self.get_form(form_class)
        return context

    def form_valid(self, form):
        form.save()
        return super(ContactPage, self).form_valid(form)
