from django.shortcuts import render

from .forms import SignUpForm
from .member_handler import MemberHandler


# Create your views here.
def sign_up_view(request):
    message = ''
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['repeat_password']:
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                member_handler = MemberHandler(username=username, password=password)
                result, message = member_handler.sign_up()
            else:
                message = 'Password and repeat password fields should be the same.'
    else:
        form = SignUpForm()

    return render(request, 'member_area/sign_up_form.html', {'form': form, 'message': message})
