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
        ordering = ['name', ]


class Player(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=70, verbose_name='Имя игрока')
    last_name = models.CharField(max_length=70, verbose_name='Фамилия игрока')
    numb = models.PositiveSmallIntegerField(verbose_name='Номер игрока')
    gif = models.FileField(null=True,blank=True, upload_to='media/gif', verbose_name='Gif игрока')
    image = models.ImageField( upload_to='media/image', blank=True, null=True, verbose_name='Фото игрока')
    like = models.BooleanField(null=True, blank=True)
    dislike = models.BooleanField(null=True, blank=True)



    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'
        unique_together = [['club', 'numb']]

Natijalar = (
    ('Win', 'win'),
    ('Draw', 'draw'),
    ('Lose', 'lose'),

)

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
    oxirgi_1 = models.CharField(choices=Natijalar, default='Draw', max_length=15)
    oxirgi_2 = models.CharField(choices=Natijalar, default='Draw', max_length=15)
    oxirgi_3 = models.CharField(choices=Natijalar, default='Draw', max_length=15)
    oxirgi_4 = models.CharField(choices=Natijalar, default='Draw', max_length=15)
    oxirgi_5 = models.CharField(choices=Natijalar, default='Draw', max_length=15)

    def __str__(self):
        return self.club.name

    class Meta:
        verbose_name = 'Турнирная таблица'
        verbose_name_plural = 'Турнирная таблица'
        ordering = ['-point']

Holat = (
    ('да', 'да'),
    ('нет', 'нет'),

)
class Matches(models.Model):
    tour = models.PositiveSmallIntegerField(verbose_name='Тур', null=True)
    home = models.ForeignKey(Club, on_delete=models.CASCADE,null=True,blank=True, verbose_name='Хозяева', related_name='home')
    guest = models.ForeignKey(Club, on_delete=models.CASCADE,null=True,blank=True, verbose_name="Гости")
    date = models.DateField(blank=True, null=True, verbose_name="Дата")
    finished = models.CharField(max_length=30, choices=Holat, verbose_name='Завершено')

    def __str__(self):
        return f'{self.home } vs { self.guest}'
    
    class Meta:
        verbose_name = 'Матч'
        verbose_name_plural = 'Матчи'
        ordering = ['date']



class Game(models.Model):
    tour = models.ForeignKey(Matches, on_delete=models.CASCADE, null=True, related_name='details')
    home_point = models.PositiveSmallIntegerField(default=0, verbose_name='Счет хозяев')
    guest_point = models.PositiveSmallIntegerField(default=0, verbose_name='Счет гостей')
    link = models.CharField(max_length=255, blank=True, null=True)
    home_red_card = models.PositiveSmallIntegerField(default=0)
    guest_red_card = models.PositiveSmallIntegerField(default=0)
    home_yellow_card = models.PositiveSmallIntegerField(default=0)
    guest_yellow_card = models.PositiveSmallIntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.tour.home.name } vs {self.tour.guest.name}'
    class Meta:
        verbose_name = 'Отчет о матче'
        verbose_name_plural = 'Отчет о матчи'


# class InfoMatch(models.Model):
#     game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='infomatch_game')
#     player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='infomatch_player')
#     date = models.DateField(verbose_name='Время гола')
#     goal_point = models.IntegerField(null=True, blank=True)
#     red_card = models.IntegerField(null=True, blank=True)
#     yellow_card = models.IntegerField(null=True, blank=True)
#     player_command = models.ForeignKey(Club, on_delete=models.CASCADE)
      
#     def __str__(self):
#         return f'{self.game.tour.home.name } vs {self.game.tour.guest.name}'


class AboutPlayer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    age = models.PositiveSmallIntegerField(verbose_name='Возраст игрока')
    yellow_cards = models.PositiveSmallIntegerField(verbose_name='Желтая карточка')
    red_cards = models.PositiveSmallIntegerField(verbose_name='Красная карточка')
    goals = models.PositiveBigIntegerField(verbose_name='Количество голов')
    force = models.PositiveIntegerField(verbose_name='Сила')
    technique = models.PositiveIntegerField(verbose_name='Техника')
    pas = models.PositiveIntegerField(verbose_name='Пас')

    def __str__(self):
        return self.player.first_name

    class Meta:
        verbose_name = 'Об игроке'
        verbose_name_plural = 'Об игроке'

class News(models.Model):
    image = models.ImageField(upload_to='media/images/')
    title = models.CharField(max_length=500)
    info = models.TextField()
    interview_author = models.CharField(max_length=300)
    date = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'


class GoalsPlayer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='plager_goal')
    goals = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.player.first_name
    
    class Meta:
        verbose_name = 'Бомбордиры'
        verbose_name_plural = 'Бомбордиры'


class RedCardsPlayer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='red_cards')
    counts = models.IntegerField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.player.first_name
    class Meta:
        verbose_name = 'Красные карточки'
        verbose_name_plural = 'Красные карточки'

class YellowCardsPlayer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='yellow_cards')
    counts = models.IntegerField(null=True, blank=True)
    

    def __str__(self) -> str:
        return self.player.first_name

    class Meta:
        verbose_name = 'Желтые карточки'
        verbose_name_plural = 'Желтые карточки'

