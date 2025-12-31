from django.shortcuts import render, redirect
from adminpanel.models import RequiredItem
from .models import Donation

def donor_home(request):
    items = RequiredItem.objects.all()
    
    if request.method == 'POST':
        donor_name = request.POST.get('donor_name')
        item_id = request.POST.get('item_id')
        quantity = int(request.POST.get('quantity'))
        donation_method = request.POST.get('donation_method')
        
        # Get the required item
        item = RequiredItem.objects.get(id=item_id)
        
        # Save donation
        Donation.objects.create(
            donor_name=donor_name,
            item=item,
            quantity=quantity,
            donation_method=donation_method,
            status='Pending'
        )
        
        # Update received quantity in RequiredItem
        item.received_quantity += quantity
        item.save()
        
        return redirect('donor_home')
    
    return render(request, 'donor/donor_home.html', {'items': items})
