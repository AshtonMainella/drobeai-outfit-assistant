from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import ClothingItem, Outfit
from .forms import ClothingItemForm
import random
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfilePictureForm


# Home Page
def home(request):
    return render(request, 'home.html')  # Render the home page template

# User Registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def settings(request):
    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('settings')  # Redirect to settings page after saving
    else:
        form = ProfilePictureForm(instance=request.user.profile)
    
    return render(request, 'settings.html', {'form': form})

# User Login
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('wardrobe')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password.'})
    return render(request, 'login.html')

# Wardrobe - List All Clothes
@login_required
def wardrobe(request):
    clothes = ClothingItem.objects.filter(user=request.user)
    return render(request, 'wardrobe.html', {'clothes': clothes})

# Add a New Clothing Item
@login_required
def add_clothing(request):
    if request.method == 'POST':
        form = ClothingItemForm(request.POST, request.FILES)
        if form.is_valid():
            clothing_item = form.save(commit=False)
            clothing_item.user = request.user
            clothing_item.save()
            return redirect('wardrobe')
    else:
        form = ClothingItemForm()
    return render(request, 'wardrobe/add_clothing.html', {'form': form})

# Edit a Clothing Item
@login_required
def edit_clothing(request, item_id):
    clothing_item = get_object_or_404(ClothingItem, id=item_id, user=request.user)
    if request.method == 'POST':
        form = ClothingItemForm(request.POST, request.FILES, instance=clothing_item)
        if form.is_valid():
            form.save()
            return redirect('wardrobe')
    else:
        form = ClothingItemForm(instance=clothing_item)
    return render(request, 'edit_clothing.html', {'form': form})

# Delete a Clothing Item
@login_required
def delete_clothing(request, item_id):
    clothing_item = get_object_or_404(ClothingItem, id=item_id, user=request.user)
    clothing_item.delete()
    return redirect('wardrobe')

# Generate an Outfit
@login_required
def generate_outfit(request):
    tops = ClothingItem.objects.filter(user=request.user, category='top')
    bottoms = ClothingItem.objects.filter(user=request.user, category='bottom')
    shoes = ClothingItem.objects.filter(user=request.user, category='shoes')

    if tops.exists() and bottoms.exists() and shoes.exists():
        selected_top = random.choice(tops)
        selected_bottom = random.choice(bottoms)
        selected_shoes = random.choice(shoes)

        # Creating the outfit and saving it
        outfit = Outfit.objects.create(user=request.user)
        outfit.items.add(selected_top, selected_bottom, selected_shoes)
        outfit.save()

        # Pass the selected items explicitly to ensure the order
        return render(request, 'outfit.html', {
            'outfit': outfit,
            'top': selected_top,
            'bottom': selected_bottom,
            'shoes': selected_shoes
        })
    else:
        return render(request, 'outfit.html', {'error': 'Not enough clothing items to create an outfit.'})

def settings(request):
    return render(request, 'settings.html')

@login_required
def profile_settings(request):
    profile = request.user.profile  # Access the profile of the logged-in user
    
    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_settings')  # Redirect after successful upload
    else:
        form = ProfilePictureForm(instance=profile)
    
    return render(request, 'settings.html', {'form': form, 'profile': profile})