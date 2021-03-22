from django.db import models

class Sale(models.Model):
    comment = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    number_of_kegs = models.PositiveIntegerField(unique=False)
    beer = models.ForeignKey(
        'beers.Beer',
        related_name='sales',
        on_delete=models.PROTECT
    )
    # user = models.ForeignKey(
    #     'users.User',
    #     related_name='sales',
    #     on_delete=models.PROTECT
    # )

    def __str__(self):
        return f'Sale {self.id} - {self.number_of_kegs} kegs of {self.beer}'
