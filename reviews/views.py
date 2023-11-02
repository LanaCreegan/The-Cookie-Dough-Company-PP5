from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from .models import Review
from .forms import ReviewForm


def edit_reviews(request, review_id):
    """ Edit a review for a product """
    review = get_object_or_404(Review, pk=review_id)
    if request.user.id != review.user.user.id:
        messages.error(request, 'Sorry, you do not have access to that.')
        return redirect(
            reverse('product_detail', args=[review.product.id])
            )
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated review!')
            return redirect(reverse('product_detail', args=[review.product.id]))
        else:
            messages.error(
                request,
                'Failed to update review. Please ensure the form is valid.')
    else:
        form = ReviewForm(instance=review)

    template = 'reviews/edit_reviews.html'
    context = {
        'form': form,
        'review': review,
    }

    return render(request, template, context)