from django.shortcuts import render, redirect, get_object_or_404
from .models import Transaction
from .forms import TransactionForm
from django.core.paginator import Paginator
from django.shortcuts import render

def transaction_list(request):
    transactions = Transaction.objects.all().order_by('-payment_date')
    return render(request, 'cashFlow/transaction_list.html', {'transactions': transactions})

def transaction_create(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm()
    return render(request, 'cashFlow/transaction_form.html', {'form': form})

def transaction_edit(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'cashFlow/transaction_form.html', {'form': form})

def transaction_delete(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        transaction.delete()
        return redirect('transaction_list')
    return render(request, 'cashFlow/transaction_confirm_delete.html', {'transaction': transaction})

def transaction_list(request):
    transaction_list = Transaction.objects.all().order_by('-payment_date')
    paginator = Paginator(transaction_list, 10)  # Show 10 transactions per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'cashFlow/transaction_list.html', {'page_obj': page_obj})