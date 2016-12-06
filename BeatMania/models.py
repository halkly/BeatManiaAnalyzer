from django.db import models


# Create your models here.
class PlayerInfomation(models.Model):
    iidx_id = models.IntegerField(primary_key=True, default=0)
    dj_name = models.CharField(max_length=6)
    single_class = models.CharField(max_length=4)
    double_class = models.CharField(max_length=4)
    prefectures = models.CharField(max_length=20)
    own_arcade = models.CharField(max_length=100)
    single_djpoint = models.FloatField(default=0.0)
    double_djpoint = models.FloatField(default=0.0)


class SubTitles(models.Model):
    title_number = models.IntegerField(primary_key=True, default=0)
    title_name = models.CharField(max_length=100)


class ClearType(models.Model):
    clear_type = models.IntegerField(primary_key=True)
    clear_type_name = models.CharField(max_length=20)


class Songs(models.Model):
    song_name = models.CharField(primary_key=True, max_length=100)
    artist_name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    subtitle = models.ForeignKey(SubTitles)
    difficulty = models.CharField(max_length=50)
    level = models.IntegerField(default=1)
    total_notes = models.IntegerField(default=0)
    scrach_notes = models.IntegerField(default=0)
    cn_notes = models.IntegerField(default=0)

    class Meta:
        unique_together = (("song_name", "artist_name", "genre", "difficulty"))


class Score(models.Model):
    song_name = models.CharField(primary_key=True, max_length=100)
    player_id = models.IntegerField(default=0)
    difficulty = models.CharField(max_length=50)
    ex_score = models.IntegerField(default=0)
    p_great = models.IntegerField(default=0)
    great = models.IntegerField(default=0)
    miss_count = models.IntegerField(default=0)
    clear_type = models.IntegerField(default=0)

    class Meta:
        unique_together = (("song_name", "player_id", "difficulty"))
