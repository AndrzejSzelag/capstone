from django.urls import reverse_lazy
from django.views import generic
from .models import Projects

# ================= MODAL forms ==================
from bootstrap_modal_forms.generic import (
    BSModalLoginView,
    BSModalCreateView,
    BSModalReadView,
    BSModalUpdateView,
    BSModalDeleteView,
    BSModalFormView,
)

from .forms import (
    ProjectModelForm,
    CustomUserCreationForm,
    CustomAuthenticationForm,
)


class Index(generic.ListView):
    model = Projects
    context_object_name = 'projects'
    template_name = 'examples/index.html'

    # Projekty wg ID od najnowszego do najstarszego
    def get_queryset(self):
        return Projects.objects.order_by("-id")


# ================= C R U D ==================

# Define a class-based view ProjectCreateView and inherit from built-in generic view BSModalCreateView.
# ProjectCreateView processes the form, uses the template and redirects to success_url showing success_message.

# Create
class ProjectCreateView(BSModalCreateView):
    template_name = 'examples/create.html'
    form_class = ProjectModelForm
    success_url = reverse_lazy('index')
    success_message = 'New Project was created successfully.'

# Read
class ProjectReadView(BSModalReadView):
    model = Projects
    context_object_name = 'projects'
    template_name = 'examples/read.html'

# Update
class ProjectUpdateView(BSModalUpdateView):
    model = Projects
    template_name = 'examples/update.html'
    form_class = ProjectModelForm
    success_url = reverse_lazy('index')
    success_message = 'Project was updated successfully.'

# Delete
class ProjectDeleteView(BSModalDeleteView):
    model = Projects
    context_object_name = 'projects'
    template_name = 'examples/delete.html'
    success_url = reverse_lazy('index')
    success_message = 'Project was deleted successfully.'


# ================ Login & Register ===============
# Register
class RegisterView(BSModalCreateView):
    form_class = CustomUserCreationForm
    template_name = 'examples/signup.html'
    success_url = reverse_lazy('index')
    success_message = 'Register was successfully. You can now Sign In.'

# Login
class LoginView(BSModalLoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'examples/login.html'
    success_url = reverse_lazy('index')
    success_message = 'You were successfully logged in.'
