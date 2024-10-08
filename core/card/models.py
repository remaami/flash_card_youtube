from django.db import models

class FlashCard (models.Model):
    question = models.TextField()
    answer = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.questio[0:10]}..."
