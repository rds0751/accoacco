from django.shortcuts import render
from dholera.models import ExpenseTransaction as DE
from forex.models import ExpenseTransaction as FE
from ipaymatics.models import ExpenseTransaction as IE
from general.models import ExpenseTransaction as GE
from general.models import NewExpenseTransaction as NE
from crm.models import Customer

# Create your views here.
# forex, general, dholera, ipaymatics
# according to account, according to txn types


def accountp(request):
	if request.method == 'POST':
	    d = DE.objects.filter(customer__icontains=request.POST.get('q'))
	    f = FE.objects.filter(customer__icontains=request.POST.get('q'))
	    i = IE.objects.filter(customer__icontains=request.POST.get('q'))
	    g = GE.objects.filter(customer__icontains=request.POST.get('q'))
	    n = NE.objects.filter(customer__icontains=request.POST.get('q'))
	    try:
		    c = Customer.objects.get(title__icontains=request.POST.get('q'))
	    except Exception as e:
	    	c = None
	    results = []
	    for x in d:
	    	results.append(x)
	    for x in f:
	    	results.append(x)
	    for x in i:
	    	results.append(x)
	    for x in g:
	    	results.append(x)
	    for x in n:
	    	results.append(x)
	    total = len(results)
	    credit = 0
	    debit = 0
	    other = 0
	    for result in results:
	    	if result.type == 'credit':
	    		credit += result.value
	    	elif result.type == 'debit':
	    		debit += result.value
	    	else:
	    		other += result.value
	    return render(request, 'reports/accountp.html', {'w': results, 'c': c, 't': total, 'cr': credit, 'db': debit, 'ot': other})
	return render(request, 'reports/accountp.html', {})

def txntype(request):
    return render(request, 'reports/type.html', {})

def validate_username(request):
    username = request.GET.get('username', None)
    u = User.objects.filter(username=username)
    data = {
        'is_taken': u
    }
    return JsonResponse(data)