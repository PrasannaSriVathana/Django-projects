from django.shortcuts import render
from .models import Hostel
from .forms import HostelForm

# Create your views here.
def ht(req):
    if(req.method=="POST"):
        form=HostelForm(req.POST)
        people=Hostel.objects.all()
        room=req.POST.get("room")
        year=req.POST.get("year")
        id1=int(room)+int(year)
        data={'hostelid':id1}
        if form.is_valid():
            form.save()
            return render(req,'success.html',{'people':people,'form':form,'data':data})
    else:
        form=HostelForm()
        return render(req,'hostel.html',{'form':form})

    