from django.db import models

class SynthesisedSpeech(models.Model):

    pitch = models.SmallIntegerField(null=True, blank=True)
    voice = models.CharField(max_length=20, null=True, blank=True)
    emotion = models.CharField(max_length=20, null=True, blank=True)
    text = models.CharField(max_length=500, null=True, blank=True)
    visemes = models.CharField(max_length=10000, blank=True, null=True)
    url = models.CharField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)

