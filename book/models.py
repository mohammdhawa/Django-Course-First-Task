from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    birography = models.TextField(max_length=2000)


    def __str__(self) -> str:
        return self.name



class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ManyToManyField(Author, related_name='book_author')
    publication_date = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=3, decimal_places=2)

    
    def __str__(self) -> str:
        return self.title



class Review(models.Model):
    NUMBER_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    book = models.ForeignKey(Book, related_name='book_reviews', on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=100)
    content = models.TextField(max_length=2500)
    rating = models.IntegerField(choices=NUMBER_CHOICES)


    def __str__(self) -> str:
        return str(self.book)