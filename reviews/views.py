
from django.shortcuts import render
from reviews.forms import ReviewForm
from django.shortcuts import redirect
from reviews.models import Review

def reviews(request):
    if request.method == 'GET':
        form = ReviewForm()
        return render(request, 'reviews.html',{'form': form})
    elif request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            name = data.get('name')
            email= data.get('email')
            review= data.get('review')
            rating = data.get('rating')
            Review.objects.create(name = name, email = email, review = review, rating = rating)
            ##with open('data.csv','a') as file:
            ##   file.write(f'{name}|{email}|{review}|{rating}\n')
            return redirect('reviews')
        else:
            form = ReviewForm()
            return render(request, 'reviews.html',{'form': form})
            review_1 = Review_objects.get(id=1)
            print(review_1.name)
    form = ReviewForm()
    review_1 = Review.objects.get(id=1)
    print(review_1.name)
    ##name_1 = request.GET.get('name')
    ##email_1= request.GET.get('email')
    ##review_1= request.GET.get('review')
    ##rating_1 = request.GET.get('rating')

    return render (request,'reviews.html',{'review_1':review_1,'form':form})

