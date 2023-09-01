from django.http import JsonResponse
from django.shortcuts import render , redirect
from django.contrib import messages
from books.models import Books 
from users.models import Profile
from comments.models import Comments
from django.contrib.auth.decorators import login_required

# # @login_required()
def comments(request,slug ):
    book = Books.objects.filter(slug=slug)
    comments = Comments.objects.filter(book=book)
    return render(request, 'comments/comments.html', {'comments': comments})

def add_comment(request ,slug):
    if request.method == "POST":
        book_id = request.POST.get('book')
        text = request.POST.get('text')
        if request.user.is_authenticated:
            user = request.user.id
            profile = Profile.objects.get(user=user)
            book = Books.objects.get(slug=slug)
            new_comment = Comments.objects.create(user=profile, book=book, text=text)
            new_comment.save()
            
            comments = Comments.objects.filter(book=book)
            # comments = Comments.objects.all()
            messages.info(request, "your Comment submited successfully ... ")
            # return render(request, 'comments/add_comment.html', {'comments': comments, "messages": messages})
            return render(request, 'comments/add_comment.html', {'comments': comments, })

            # return JsonResponse({'html': html, "status": "Comment Send successfuly ! ..."})
        
        else:
            messages.info(request, "Login To contnu ...")
            return JsonResponse({"status":"Login To Continu"})
    return redirect('/')


def delete_comment(request, pk):
    if request.user.is_authenticated:

        try:
            item = Comments.objects.get(id=pk)
            item.delete()
            return JsonResponse({'success': True})
        except Comments.DoesNotExist:
            return JsonResponse({'success': False})
        
    else:
            messages.info(request, "Login To contnu ...")
            return JsonResponse({"status":"Login To Continu"})
        
        