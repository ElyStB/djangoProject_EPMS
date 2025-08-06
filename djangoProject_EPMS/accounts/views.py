
from django.contrib.auth import views as auth_views, login
from django.views import generic as views
from django.contrib import messages
from django.urls import reverse, reverse_lazy

from djangoProject_EPMS.accounts.forms import RegisterUserCreationForm


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True


class RegisterUserView(views.CreateView):
    template_name = 'accounts/register.html'
    form_class = RegisterUserCreationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, form.instance)
        return result


class LogoutUserView(auth_views.LogoutView):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.success(request, "Logged out!")
        return super().dispatch(request, *args, **kwargs)


class UserProfileView(views.DetailView):
    queryset = Profile.objects.prefetch_related('user').all()
    template_name = 'accounts/profile-details.html'


class UserProfileEditView(views.UpdateView):
    queryset = Profile.objects.all()
    template_name = 'accounts/profile-edit.html'
    fields = ('first_name', 'last_name', 'email', 'profile_picture')

    def get_success_url(self):
        return reverse('edit_profile', kwargs={'pk': self.object.pk})


class  DeleteUserProfileView(views.DeleteView):
    queryset = Profile.objects.all()
    template_name = 'accounts/profile-delete.html'

    def get_success_url(self):
        messages.success(self.request, "Profile deleted successfully.")
        return reverse('home')  # Redirect to home or another page after deletionqueryset