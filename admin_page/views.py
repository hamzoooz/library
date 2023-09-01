from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse
from books.models import Books

@login_required()
def manage(request):
    if request.user.is_staff:
        all_books = Books.objects.all()
        all_publised = Books.objects.filter(available='publised')
        all_wiating = Books.objects.filter(available='wiating')
        all_draft = Books.objects.filter(available='draft')
        all_deleted = Books.objects.filter(available='deleted')
        all_abrov = Books.objects.filter(abrov=True)
        all_not_abrov = Books.objects.filter(abrov=False)

        return render(request, 'manage/manage.html', {
        'all_books': all_books,
        'all_publised': all_publised,
        'all_wiating': all_wiating,
        'all_draft': all_draft,
        'all_deleted': all_deleted,
        'all_abrov': all_abrov,
        'all_not_abrov': all_not_abrov,
        })
    else:
        return redirect('my_store')

def move_to_published(request, pk):
    if request.method == 'POST':
        if request.user.is_authenticated:
            if (request.user.is_staff):
                book = Books.objects.get(pk=pk)
                book.available = 'publised'
                book.save()
                return JsonResponse({"status": f'The Book - { book.name } -  Was Moved to publised sucssessfuly '})
            else:
                return JsonResponse({"status": 'You not have access to publised this book '})
                # return redirect(request.META.get("HTTP_REFERER"))
        else:
            return redirect('my_store')
    return redirect('/')

def move_to_delete(request, pk):
    if (request.user.is_staff):
        book = Books.objects.get(pk=pk)
        book.available = 'deleted'
        book.save()
        return JsonResponse({"status": f'The Book - { book.name } -  Was Moved to deleted sucssessfuly '})
    else:
        return JsonResponse({"status": 'You not have access to deleted this book '})
    
    if request.META.get('HTTP_REFERER'):
        return redirect(request.META.get("HTTP_REFERER"))
    else:
        return redirect('my_store')

def move_to_draft(request, pk):
    if (request.user.is_staff):
        book = Books.objects.get(pk=pk)
        book.available = 'draft'
        book.save()
        return JsonResponse({"status": f'The Book - { book.name } -  Was Moved to draft sucssessfuly '})
    else:
        return JsonResponse({"status": 'You not have access to draft this book '})
    
    if request.META.get('HTTP_REFERER'):
        return redirect(request.META.get("HTTP_REFERER"))
    else:
        return redirect('my_store')

def move_to_delete(request, pk):
    if (request.user.is_staff):
        book = Books.objects.get(pk=pk)
        book.available = 'deleted'
        book.save()
        return JsonResponse({"status": f'The Book - { book.name } -  Was Moved to deleted sucssessfuly '})
    else:
        return JsonResponse({"status": 'You not have access to deleted this book '})
    
    if request.META.get('HTTP_REFERER'):
        return redirect(request.META.get("HTTP_REFERER"))
    else:
        return redirect('my_store')

def move_to_waiting(request, pk):
    if (request.user.is_staff):
        book = Books.objects.get(pk=pk)
        book.available = 'wiating'
        book.save()
        return JsonResponse({"status": f'The Book - { book.name } -  Was Moved to Waiting list  sucssessfuly '})
    else:
        return JsonResponse({"status": 'You not have access to move this book to wiate list '})
    
    if request.META.get('HTTP_REFERER'):
        return redirect(request.META.get("HTTP_REFERER"))
    else:
        return redirect('my_store')

def move_to_abrov(request, pk):
    if (request.user.is_staff):
        book = Books.objects.get(pk=pk)
        book.abrov = True
        book.save()
        return JsonResponse({"status": f'The Book - { book.name } -  Was Moved to Abrove sucssessfuly '})
    else:
        return JsonResponse({"status": 'You not have access to abrove  this book '})
    
    if request.META.get('HTTP_REFERER'):
        return redirect(request.META.get("HTTP_REFERER"))
    else:
        return redirect('my_store')

def move_to_not_abrov(request, pk):
    if (request.user.is_staff):
        book = Books.objects.get(pk=pk)
        book.abrov = False
        book.save()
        return JsonResponse({"status": f'The Book - { book.name } -  Was Moved From  Aborov list sucssessfuly '})
    else:
        return JsonResponse({"status": 'You not have access to aremove this book from abrove list '})
    
    if request.META.get('HTTP_REFERER'):
        return redirect(request.META.get("HTTP_REFERER"))
    else:
        return redirect('my_store')
