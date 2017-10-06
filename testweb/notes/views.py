from django.views import generic
from .models import note
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserForm


class IndexView(generic.ListView):
    template_name = 'notes/index.html'
    context_object_name = 'all_notes'

    def get_queryset(self):
        return note.objects.all()


class DetailView(generic.DetailView):
    model = note
    # 'note' here is the variable you use to reference an individual note
    # in details.html
    template_name = 'notes/detail.html'


class NoteCreate(CreateView):
    model = note
    fields = [
        'title',
        'content'
    ]


class NoteUpdate(UpdateView):
    model = note
    fields = [
        'title',
        'content'
    ]


class NoteDelete(DeleteView):
    model = note
    success_url = reverse_lazy('notes:index')
    # reverse_lazy redirects to index.html upon note
    # deletion


class UserFormView(View):
    form_class = UserForm
    template_name = 'notes/signup.html'

    # blank form for new users
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # handle user signup data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            # create an object but do not
            # save it immediately
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            # passwords are hashed by django so cannot
            # be referenced directly as user.attribute
            # must use set method
            user.save()

            # if username/pass are accurate, return User object
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('notes:index')
                    # redirect to index upon succesful login

        return render(request, self.template_name, {'form': form})
        # render login form again if user is not valid