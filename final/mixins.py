from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect


class PassRequestMixin(object):
    # Mixin which puts the request into the form's kwargs.
    def get_form_kwargs(self):
        kwargs = super(PassRequestMixin, self).get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs


class PopRequestMixin(object):
    # Mixin which pops request out of the kwargs and attaches it to the form's instance.
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(PopRequestMixin, self).__init__(*args, **kwargs)


class CreateUpdateAjaxMixin(object):
    # Mixin which passes or saves object based on request type.
    def save(self, commit=True):
        # if not self.request.is_ajax() or self.request.POST.get('closeOnSubmit') == 'False':
        if not self.request.is_ajax() or self.request.POST.get('asyncUpdate') == 'True':
            instance = super(CreateUpdateAjaxMixin, self).save(commit=commit)
        else:
            instance = super(CreateUpdateAjaxMixin, self).save(commit=False)
        return instance


class DeleteMessageMixin(object):
    # Mixin which adds message to BSModalDeleteView.
    def post(self, request, *args, **kwargs):
        messages.success(request, self.success_message)
        return super(DeleteMessageMixin, self).delete(request, *args, **kwargs)


class LoginAjaxMixin(object):
    # Mixin which authenticates user if request is not ajax request.
    def form_valid(self, form):
        if not self.request.is_ajax():
            auth_login(self.request, form.get_user())
            messages.success(self.request, self.success_message)
        return HttpResponseRedirect(self.get_success_url())
