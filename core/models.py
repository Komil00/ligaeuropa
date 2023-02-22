from django.db import models


# Create your models here.
class Club(models.Model):
    name = models.CharField(max_length=50, verbose_name='Клуб')
    icon = models.ImageField(upload_to='club-images/', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клуб'
        verbose_name_plural = 'Клубы'


class Team(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    name = models.CharField(max_length=70, verbose_name='Имя игрока')
    numb = models.PositiveSmallIntegerField(verbose_name='Номер игрока', unique=True)
    position = models.CharField(max_length=50, verbose_name='Позиция игрока')

    def __str__(self):
        return self.club

    class Meta:
        verbose_name = 'Состав'
        verbose_name_plural = 'Составы'
        unique_together = [['club', 'numb']]


class TournamentTable(models.Model):
    club = models.OneToOneField(Club, on_delete=models.CASCADE, verbose_name='Клуб')
    game = models.PositiveSmallIntegerField(default=0, verbose_name='И')
    win = models.PositiveSmallIntegerField(default=0, verbose_name='В')
    draw = models.PositiveSmallIntegerField(default=0, verbose_name='Н')
    lose = models.PositiveSmallIntegerField(default=0, verbose_name='П')
    goals = models.PositiveSmallIntegerField(default=0, verbose_name='ЗМ')
    missed_goals = models.PositiveSmallIntegerField(default=0, verbose_name='ПМ')
    diff = models.PositiveSmallIntegerField(default=0, verbose_name='РМ')
    point = models.PositiveSmallIntegerField(default=0, verbose_name='О')

    def __str__(self):
        return self.club

    class Meta:
        verbose_name = 'Турнирная таблица'
        verbose_name_plural = 'Турнирная таблица'
        ordering = ['-point', 'club__name']


class Tour(models.Model):
    tour = models.PositiveSmallIntegerField(verbose_name='Тур', null=True)
    home = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True, verbose_name='Хозяева', related_name='home')
    guest = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True, verbose_name="Гости")
    date = models.DateTimeField(blank=True, null=True, verbose_name="Дата")
    finished = models.BooleanField(null=True, verbose_name='Завершено')

    def __str__(self):
        return f'{self.home} vs {self.guest}'

    class Meta:
        verbose_name = 'Матч'
        verbose_name_plural = 'Матчи'
        ordering = ['tour']


class Game(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, null=True, related_name='games')
    home_point = models.PositiveSmallIntegerField(default=0, verbose_name='Счет хозяев')
    guest_point = models.PositiveSmallIntegerField(default=0, verbose_name='Счет гостей')
    date = models.DateTimeField(null=True, blank=True, verbose_name='Дата')
    link = models.CharField(max_length=255, blank=True, null=True)
    red_card = models.PositiveSmallIntegerField(default=0)
    yellow_card = models.PositiveSmallIntegerField(default=0)


class PlayerGoal(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    name = models.CharField(max_length=70, verbose_name='Имя игрока')
    time = models.PositiveSmallIntegerField(default=0, verbose_name='Время гола')

    def __str__(self):
        return self.name