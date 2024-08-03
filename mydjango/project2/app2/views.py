from django.shortcuts import render
from .models import Bank
from .forms import BankForm
# Create your views here.
def ba(req):
    if(req.method == "POST"):
        form=BankForm(req.POST)
        people=Bank.objects.all()
        if form.is_valid():
            form.save()
            return render(req,'success.html',{'people':people,'form':form})
    else:
        form=BankForm()
        return render(req,'bank.html',{'form':form})        