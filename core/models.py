from django.db import models


# Create your models here.

KubokChoice = (
    ('1/8', '1/8'),
    ('1/4', '1/4'),
    ('1/2', '1/2'),
    ('champion', 'champion'),

)

class Seasson(models.Model):
    chempionat = models.IntegerField()
    kubok = models.CharField(max_length=200, choices=KubokChoice)
    # def __str__(self):
    #     return self.chempionat

class Trophey(models.Model):
    name = models.CharField(max_length=200, null=True)
    seasson = models.ForeignKey(Seasson, models.CASCADE)
    
    def __str__(self):
        return self.name

class Club(models.Model):
    name = models.CharField(max_length=50, verbose_name='Клуб')
    icon = models.ImageField(upload_to='club-images/', null=True, blank=True)
    trophey = models.ForeignKey(Trophey, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клуб'
        verbose_name_plural = 'Клубы'
        ordering = ['name', ]


class Player(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='palyer_club')
    first_name = models.CharField(max_length=70, verbose_name='Имя игрока')
    last_name = models.CharField(max_length=70, verbose_name='Фамилия игрока')
    numb = models.PositiveSmallIntegerField(verbose_name='Номер игрока')
    gif = models.FileField(null=True,blank=True, upload_to='media/gif', verbose_name='Gif игрока')
    image = models.ImageField( upload_to='media/image', verbose_name='Фото игрока')

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
    home = models.ForeignKey(Club, on_delete=models.CASCADE, verbose_name='Хозяева', related_name='home')
    guest = models.ForeignKey(Club, on_delete=models.CASCADE, verbose_name="Гости")
    date = models.DateField(blank=True, null=True, verbose_name="Дата")
    finished = models.CharField(max_length=30, choices=Holat, verbose_name='Завершено')

    def __str__(self):
        return f'{self.home } vs { self.guest}'
    
    class Meta:
        verbose_name = 'Матч'
        verbose_name_plural = 'Матчи'
        ordering = ['date']



class Game(models.Model):
    tour = models.ForeignKey(Matches, on_delete=models.CASCADE, related_name='details')
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

class AboutPlayer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    age = models.PositiveSmallIntegerField(verbose_name='Возраст игрока')
    yellow_cards = models.PositiveSmallIntegerField(verbose_name='Желтая карточка')
    red_cards = models.PositiveSmallIntegerField(verbose_name='Красная карточка')
    goals = models.PositiveBigIntegerField(verbose_name='Количество голов')
    force = models.PositiveIntegerField(verbose_name='Сила')
    technique = models.PositiveIntegerField(verbose_name='Техника')
    pas = models.PositiveIntegerField(verbose_name='Пас')

    likes_count = models.PositiveIntegerField(null=True, blank=True, default=1)
    # dislikes_count = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.player.first_name

    class Meta:
        verbose_name = 'Об игроке'
        verbose_name_plural = 'Об игроке'

class Like(models.Model):
    aboutplayer = models.ForeignKey(AboutPlayer, on_delete=models.CASCADE, related_name='likes')
    is_like = models.BooleanField(null=True, blank=True)




class GoalsPlayer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='plager_goal')
    counts = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
            player = self.player
            about_player = AboutPlayer.objects.get(player=player)
            about_player.goals = self.counts
            about_player.save()
            super().save(*args, **kwargs)

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
    
    def save(self, *args, **kwargs):
        player = self.player
        about_player = AboutPlayer.objects.get(player=player)
        about_player.red_cards = self.counts
        about_player.save()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Красные карточки'
        verbose_name_plural = 'Красные карточки'

class YellowCardsPlayer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='yellow_cards')
    counts = models.IntegerField(null=True, blank=True)
    
    def save(self, *args, **kwargs):
        player = self.player
        about_player = AboutPlayer.objects.get(player=player)
        about_player.yellow_cards = self.counts
        about_player.save()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.player.first_name

    class Meta:
        verbose_name = 'Желтые карточки'
        verbose_name_plural = 'Желтые карточки'











# from django.db import models
# from django.utils.translation import gettext_lazy as _
# from django.contrib.auth import get_user_model
# from django.utils.text import slugify

# User = get_user_model()


# class Subject(models.Model):
#     name = models.CharField(max_length=255, verbose_name=_("Subject name"))
#     slug = models.SlugField(max_length=255, verbose_name=_("Slug"), unique=True)
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
#     updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))

#     class Meta:
#         verbose_name = _("Subject")
#         verbose_name_plural = _("Subjects")

#     def __str__(self):
#         return self.name

#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.name_uz) + "-" + str(self.id)
#         super().save(*args, **kwargs)


# class TestLanguage(models.TextChoices):
#     UZ = "uz", _("Uzbek")
#     RU = "ru", _("Russian")
#     EN = "en", _("English")


# class TestBought(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_tests")
#     test = models.ForeignKey("Test", on_delete=models.CASCADE, related_name="bought_by")
#     date_bought = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         verbose_name = _("Test Bought")
#         verbose_name_plural = _("Tests Bought")

#     def __str__(self):
#         return f"{self.user} bought {self.test} on {self.date_bought}"


# class Test(models.Model):
#     name = models.CharField(max_length=255, verbose_name=_("Test name"))
#     subject = models.ForeignKey(
#         Subject, on_delete=models.CASCADE, verbose_name=_("Subject")
#     )
#     price = models.DecimalField(
#         max_digits=10, decimal_places=2, verbose_name=_("Price")
#     )
#     language = models.CharField(
#         max_length=7, choices=TestLanguage.choices, verbose_name=_("Language")
#     )
#     bought = models.ManyToManyField(
#         User,
#         through="TestBought",
#         related_name="bought_tests",
#         verbose_name=_("Bought"),
#     )
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
#     updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))
#     slug = models.SlugField(max_length=255, verbose_name=_("Slug"), unique=True)

#     class Meta:
#         verbose_name = _("Test")
#         verbose_name_plural = _("Tests")
#         ordering = ("-created_at",)

#     def __str__(self):
#         return self.name

#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.name_uz) + "-" + str(self.id)
#         super().save(*args, **kwargs)
    
#     @property
#     def get_questions(self):
#         return self.question_set.all()


# class AnswerOptions(models.TextChoices):
#     OPT1 = "opt1", _("Option 1")
#     OPT2 = "opt2", _("Option 2")
#     OPT3 = "opt3", _("Option 3")
#     OPT4 = "opt4", _("Option 4")


# class Question(models.Model):
#     test = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name=_("Test"))
#     text = models.TextField(verbose_name=_("Question text"))
#     question_number = models.PositiveIntegerField(verbose_name=_("Question number"))
#     opt1 = models.CharField(max_length=255, verbose_name=_("Option 1"))
#     opt2 = models.CharField(max_length=255, verbose_name=_("Option 2"))
#     opt3 = models.CharField(max_length=255, verbose_name=_("Option 3"))
#     opt4 = models.CharField(max_length=255, verbose_name=_("Option 4"))
#     correct_answer = models.CharField(max_length=255, verbose_name=_("Correct option"), choices=AnswerOptions.choices)
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
#     updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))

#     class Meta:
#         verbose_name = _("Question")
#         verbose_name_plural = _("Questions")
#         ordering = ("question_number",)

#     def __str__(self):
#         return self.text


# class UserAnswer(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("User"))
#     question = models.ForeignKey(
#         Question, on_delete=models.CASCADE, verbose_name=_("Question")
#     )
#     answer = models.CharField(max_length=255, verbose_name=_("Answer"), choices=AnswerOptions.choices)
#     is_correct = models.BooleanField(default=False, verbose_name=_("Is correct"))
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
#     updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))

#     class Meta:
#         verbose_name = _("User Answer")
#         verbose_name_plural = _("User Answers")

#     def __str__(self):
#         return f"{self.user} answered {self.answer} to {self.question}"


# class TestResult(models.Model):
#     test = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name=_("Test"))
#     user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("User"))
#     correct_answers = models.PositiveIntegerField(verbose_name=_("Correct answers"), default=0)
#     incorrect_answers = models.PositiveIntegerField(verbose_name=_("Incorrect answers"), default=0)
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
#     updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))

#     class Meta:
#         verbose_name = _("Test Result")
#         verbose_name_plural = _("Test Results")

#     def __str__(self):
#         return f"{self.user} got {self.result} on {self.test}"

#     def save(self, *args, **kwargs):
#         self.correct_answers = self.user_answers.filter(is_correct=True).filter(test=self.test).count()
#         self.incorrect_answers = self.user_answers.filter(is_correct=False).filter(test=self.test).count()
#         super().save(*args, **kwargs)


