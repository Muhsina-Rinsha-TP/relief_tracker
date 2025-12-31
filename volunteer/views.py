from django.shortcuts import render, redirect
from adminpanel.models import RequiredItem
from .models import Delivery

def volunteer_home(request):
    # Show all required items
    items = RequiredItem.objects.all()
    return render(request, 'volunteer/volunteer_home.html', {'items': items})

def update_delivery(request, item_id):
    item = RequiredItem.objects.get(id=item_id)
    
    if request.method == 'POST':
        status = request.POST.get('status')
        quantity = int(request.POST.get('quantity'))
        
        # Save delivery record
        Delivery.objects.create(item=item, quantity=quantity, status=status)
        
        # Update received quantity in RequiredItem
        if status == 'Collected':
            item.received_quantity += quantity
            item.save()
        
        return redirect('volunteer_home')
    
    return render(request, 'volunteer/update_delivery.html', {'item': item})
