from django.db import models

# Create your models here.
class AudioFile(models.Model):
    transcript = models.CharField(max_length=500, blank=True, null=True)
    words = models.CharField(max_length=5000, blank=True, null=True)
    audio = models.FileField(upload_to="recorded_speech/")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        string_sentence = ''
        if self.transcript != None:
            string_sentence = self.transcript
        return str(self.pk) + " " + string_sentence

class AudioAlteration(models.Model):
    audio_file = models.ForeignKey(AudioFile, on_delete=models.CASCADE)
    updated_words = models.CharField(max_length=5000, blank=True, null=True)
    transcript_deleted = models.CharField(max_length=500, blank=True, null=True)
    transcript_added = models.CharField(max_length=500, blank=True, null=True)
    relative_filename = models.CharField(max_length=200, blank=True, null=True)
    visemes = models.CharField(max_length=4000, blank=True, null=True)

    def __str__(self):
        return str(self.audio_file.pk) + ": " + str(self.relative_filename)

