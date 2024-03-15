from django.shortcuts import render, redirect
from .forms import UserProfileForm
from .models import UserProfile

def captive_portal(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            auth_token = form.cleaned_data['auth_token']
            # Check if the token exists in tokens.txt
            if is_valid_token(auth_token):
                # Check if the token has been used before
                if not is_token_used(auth_token):
                    # Mark the token as used
                    mark_token_used(auth_token)
                    # Save form data
                    form.save()
                    return redirect('success')  # Redirect to success page
                else:
                    return render(request, 'portal/captiveportal.html', {'form': form, 'error_message': 'Token already used. Please try another.'})
            else:
                return render(request, 'portal/captiveportal.html', {'form': form, 'error_message': 'Invalid token. Please try another.'})
    else:
        form = UserProfileForm()
    return render(request, 'portal/captiveportal.html', {'form': form})

def is_valid_token(token):
    # Check if the token exists in tokens.txt
    with open('tokens.txt', 'r') as file:
        valid_tokens = file.readlines()
    valid_tokens = [t.strip() for t in valid_tokens]  # Strip whitespace characters
    return token in valid_tokens


def is_token_used(token):
    # Check if the token is in the used tokens file
    with open('used_tokens.txt', 'r') as file:
        used_tokens = file.readlines()
    return token + '\n' in used_tokens

def mark_token_used(token):
    # Append the used token to the used tokens file
    with open('used_tokens.txt', 'a') as file:
        file.write(token + '\n')
def success(request):
    return render(request, 'portal/success.html')

def view_profiles(request):
    profiles = UserProfile.objects.all()
    return render(request, 'portal/view_profiles.html', {'profiles': profiles})
