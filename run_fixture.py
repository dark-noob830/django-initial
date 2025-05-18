import os
import django
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()
from book_actions.models import Rating
from book.models import Book

fixtures = ['user', 'user_info', 'book', 'persian_chapters', 'sample1', 'sample2', 'sample3', 'sample4', 'sample5',
            'sample6', 'sample7', 'reviews', 'comments', 'book_actions', 'tag']
for fixture in fixtures:
    print(f'{fixture}...')
    call_command('loaddata', fixture)


def update_all_book_ratings():
    for book in Book.objects.all():
        ratings = Rating.objects.filter(book=book)
        book.rating_count = ratings.count()
        book.rating_sum = sum(float(r.rating) for r in ratings)
        book.save()


update_all_book_ratings()
