from django.db import models
from django.utils import timezone
import datetime
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models import Count, Sum, Avg

class Tb_test_kategori(models.Model):
    kategori_answer = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    def __str__(self):
        return self.kategori_answer

    class Meta:
        db_table = 'Tb_test_kategori'

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
class Tb_answer(models.Model):
    test_kategori = models.ForeignKey(Tb_test_kategori, on_delete=models.CASCADE, default=None, blank=True, null=True)
    answer = models.CharField(max_length=200)
    score = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.answer
    class Meta:
        db_table = 'Tb_answer'

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
class Tb_kategori_soal(models.Model):
    test = models.ForeignKey(Tb_test_kategori, on_delete=models.CASCADE, default=None, blank=True, null=True)
    kat_lvl_kepuasan = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    def __str__(self):
        return self.kat_lvl_kepuasan
    class Meta:
        db_table = 'Tb_kategori_soal'

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    

class Tb_soal_kepuasan_umum(models.Model):
    test = models.ForeignKey(Tb_test_kategori, on_delete=models.CASCADE, default=None, blank=True, null=True)
    pertanyaan = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return self.pertanyaan

    class Meta:
        db_table = 'Tb_soal_kepuasan_umum'

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Tb_soal_kepentingan(models.Model):
    test = models.ForeignKey(Tb_test_kategori, on_delete=models.CASCADE, default=None, blank=True, null=True)
    lvl_kepuasan = models.ForeignKey(Tb_kategori_soal, on_delete=models.CASCADE, default=None, blank=True, null=True)
    pertanyaan = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    def __str__(self):
        return self.pertanyaan
    class Meta:
        db_table = 'Tb_soal_kepentingan'

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Tb_soal_kepuasan(models.Model):
    test = models.ForeignKey(Tb_test_kategori, on_delete=models.CASCADE, default=None, blank=True, null=True)
    lvl_kepuasan = models.ForeignKey(Tb_kategori_soal, on_delete=models.CASCADE, default=None, blank=True, null=True)
    pertanyaan = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    def __str__(self):
        return self.pertanyaan
    class Meta:
        db_table = 'Tb_soal_kepuasan'

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class m_position(models.Model):
    position = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    def __str__(self):
        return self.position
    class Meta:
        db_table = 'm_position'

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
class m_location(models.Model):
    location = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    def __str__(self):
        return self.location
    class Meta:
        db_table = 'm_location'
        
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class m_gender(models.Model):
    gender = models.CharField(max_length=10)
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return self.gender

    class Meta:
        db_table = 'm_gender'

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
class m_education(models.Model):
    education = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return self.education

    class Meta:
        db_table = 'm_education'

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
class m_korsa(models.Model):
    korsa = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return self.korsa

    class Meta:
        db_table = 'm_korsa'

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
class m_jenis_jabatan(models.Model):
    jenis_jabatan = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return self.jenis_jabatan

    class Meta:
        db_table = 'm_jenis_jabatan'

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        
class user_data(models.Model):
    id_auth_user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    position=models.ForeignKey(m_position, on_delete=models.SET_NULL, null=True, blank=True)
    location=models.ForeignKey(m_location, on_delete=models.SET_NULL, null=True, blank=True)
    phone_number=models.CharField(max_length=200)
    birthday=models.DateField(null=True)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    profile_picture = models.ImageField(upload_to='kuesioner/static/kuesioner/assets/img/illustrations/profile_pictures/', blank=True, null=True)
    gender = models.ForeignKey(m_gender, on_delete=models.SET_NULL, null=True, blank=True)
    education = models.ForeignKey(m_education, on_delete=models.SET_NULL, null=True, blank=True)
    korsa = models.ForeignKey(m_korsa, on_delete=models.SET_NULL, null=True, blank=True)
    jenis_jabatan = models.ForeignKey(m_jenis_jabatan, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.phone_number
    
    class Meta:
        db_table = 'user_data'

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class UserResponse(models.Model):
    question = models.ForeignKey(Tb_soal_kepuasan_umum, on_delete=models.CASCADE)
    answer = models.ForeignKey(Tb_answer, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=150, blank=True, null=True)
    score = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.answer:
            self.score = self.answer.score
        if self.user:
            self.username = self.user.username
        super().save(*args, **kwargs)

        self.update_user_counts()

    @classmethod
    def update_user_counts(cls):

        # Perform the count and group by the question
        counts = cls.objects.values('question').annotate(
        user_count=Count('user'),
        total_score=Sum('answer__score')
    )

        # Update the QuestionUserCount table with the counts
        for count in counts:
            question_id = count['question']
            user_count = count['user_count']
            total_score = count['total_score']
            question_user_count, created = count_user_umum.objects.get_or_create(
                question_id=question_id
            )
            question_user_count.user_count = user_count
            question_user_count.total_score = total_score
            question_user_count.save()

    class Meta:
        db_table = 'UserResponse'

class UserResponse1(models.Model):
    question = models.ForeignKey(Tb_soal_kepentingan, on_delete=models.CASCADE)
    lvl_kepuasan = models.ForeignKey(Tb_kategori_soal, on_delete=models.CASCADE)
    answer = models.ForeignKey(Tb_answer, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=150, blank=True, null=True)
    score = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.answer:
            self.score = self.answer.score
        if self.user:
            self.username = self.user.username
        super().save(*args, **kwargs)

        self.update_user_counts()

    @classmethod
    def update_user_counts(cls):
        from django.db.models import Count, Sum

        # Perform the count and group by the question
        counts = cls.objects.values('question').annotate(
        user_count=Count('user'),
        total_score=Sum('answer__score')
    )

        # Update the QuestionUserCount table with the counts
        for count in counts:
            question_id = count['question']
            user_count = count['user_count']
            total_score = count['total_score']
            question_user_count, created = count_user_kepentingan.objects.get_or_create(
                question_id=question_id
            )
            question_user_count.user_count = user_count
            question_user_count.total_score = total_score
            question_user_count.save()




    @classmethod
    def update_score_sums(cls):

        # Aggregate the sum of scores for each unique lvl_kepuasan value
        score_sums = cls.objects.values('lvl_kepuasan').annotate(total_score=Sum('score'))

        # Update the QuestionUserCount table with the aggregated data
        for score_sum in score_sums:
            lvl_kepuasan = score_sum['lvl_kepuasan']
            total_score = score_sum['total_score']

            question_user_count, created = score_lvl_kepentingan.objects.get_or_create(
                lvl_kepuasan=lvl_kepuasan
            )
            question_user_count.total_score = total_score
            question_user_count.save()

    class Meta:
        db_table = 'UserResponse1'

class UserResponse2(models.Model):
    question = models.ForeignKey(Tb_soal_kepuasan, on_delete=models.CASCADE)
    lvl_kepuasan = models.ForeignKey(Tb_kategori_soal, on_delete=models.CASCADE)
    answer = models.ForeignKey(Tb_answer, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=150, blank=True, null=True)
    score = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.answer:
            self.score = self.answer.score
        if self.user:
            self.username = self.user.username
        super().save(*args, **kwargs)

        self.update_user_counts()

    @classmethod
    def update_user_counts(cls):
        from django.db.models import Count, Sum

        # Perform the count and group by the question
        counts = cls.objects.values('question').annotate(
        user_count=Count('user'),
        total_score=Sum('answer__score')
    )

        # Update the QuestionUserCount table with the counts
        for count in counts:
            question_id = count['question']
            user_count = count['user_count']
            total_score = count['total_score']
            question_user_count, created = count_user_kepuasan.objects.get_or_create(
                question_id=question_id
            )
            question_user_count.user_count = user_count
            question_user_count.total_score = total_score
            question_user_count.save()


    @classmethod
    def update_score_sums(cls):

        # Aggregate the sum of scores for each unique lvl_kepuasan value
        score_sums = cls.objects.values('lvl_kepuasan').annotate(total_score=Sum('score'))

        # Update the QuestionUserCount table with the aggregated data
        for score_sum in score_sums:
            lvl_kepuasan = score_sum['lvl_kepuasan']
            total_score = score_sum['total_score']

            question_user_count, created = score_lvl_kepuasan.objects.get_or_create(
                lvl_kepuasan=lvl_kepuasan
            )
            question_user_count.total_score = total_score
            question_user_count.save()

    class Meta:
        db_table = 'UserResponse2'

class count_user_umum(models.Model):
    question = models.ForeignKey(Tb_soal_kepuasan_umum, on_delete=models.CASCADE)
    user_count = models.IntegerField()
    total_score = models.IntegerField(default=0)
    

    def __str__(self):
        return f"Question: {self.question}, User Count: {self.user_count}"
    class Meta:
        db_table = 'count_user_umum'

class count_user_kepentingan(models.Model):
    question = models.ForeignKey(Tb_soal_kepentingan, on_delete=models.CASCADE)
    user_count = models.IntegerField(default=0)
    total_score = models.IntegerField(default=0)

    def __str__(self):
        return f"Question: {self.question}, User Count: {self.user_count}"
    class Meta:
        db_table = 'count_user_kepentingan'

class count_user_kepuasan(models.Model):
    question = models.ForeignKey(Tb_soal_kepuasan, on_delete=models.CASCADE)
    user_count = models.IntegerField(default=0)
    total_score = models.IntegerField(default=0)

    def __str__(self):
        return f"Question: {self.question}, User Count: {self.user_count}"
    class Meta:
        db_table = 'count_user_kepuasan'

class tb_dimensi(models.Model):
    kat_dimensi = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    def __str__(self):
        return self.kat_dimensi
    class Meta:
        db_table = 'tb_dimensi'

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
class dimensi_kepentingan(models.Model):
    test = models.ForeignKey(Tb_test_kategori, on_delete=models.CASCADE, default=None, blank=True, null=True)
    dimensi = models.ForeignKey(tb_dimensi, on_delete=models.CASCADE, default=None, blank=True, null=True)
    question = models.ForeignKey(Tb_soal_kepentingan, on_delete=models.CASCADE, default=None, blank=True, null=True)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    total_score = models.IntegerField(default=0)

    def __str__(self):
        return str(self.question)
    class Meta:
        db_table = 'tb_dimensi_kepentingan'
        unique_together = ['test', 'dimensi', 'question']

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
class dimensi_kepuasan(models.Model):
    test = models.ForeignKey(Tb_test_kategori, on_delete=models.CASCADE, default=None, blank=True, null=True)
    dimensi = models.ForeignKey(tb_dimensi, on_delete=models.CASCADE, default=None, blank=True, null=True)
    question = models.ForeignKey(Tb_soal_kepuasan, on_delete=models.CASCADE, default=None, blank=True, null=True)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    total_score = models.IntegerField(default=0)

    def __str__(self):
        return str(self.soal)
    class Meta:
        db_table = 'tb_dimensi_kepuasan'
        unique_together = ['test', 'dimensi', 'question']

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
class score_lvl_kepentingan(models.Model):
    test_kategori = models.ForeignKey(Tb_test_kategori, on_delete=models.CASCADE, default=None, blank=True, null=True)
    lvl_kepuasan = models.ForeignKey(Tb_kategori_soal, on_delete=models.CASCADE)
    total_score = models.IntegerField(default=0)

    class Meta:
        db_table = 'tb_score_lvl_kepentingan'

class score_lvl_kepuasan(models.Model):
    test_kategori = models.ForeignKey(Tb_test_kategori, on_delete=models.CASCADE, default=None, blank=True, null=True)
    lvl_kepuasan = models.ForeignKey(Tb_kategori_soal, on_delete=models.CASCADE)
    total_score = models.IntegerField(default=0)

    class Meta:
        db_table = 'tb_score_lvl_kepuasan'

class score_dimensi(models.Model):
    dimensi = models.ForeignKey(tb_dimensi, on_delete=models.CASCADE, default=None, blank=True, null=True)
    question_id = models.IntegerField()
    score_difference = models.IntegerField()
    average_score_difference = models.FloatField(null=True, blank=True)

    @classmethod
    def calculate_score_difference(cls):
        scores = []
        kepentingan_scores = dimensi_kepentingan.objects.all()
        for kepuasan_score in dimensi_kepuasan.objects.all():
            kepentingan_scores_filtered = kepentingan_scores.filter(question_id=kepuasan_score.question_id)
            if kepentingan_scores_filtered.exists():
                score_difference = kepuasan_score.total_score - kepentingan_scores_filtered.first().total_score

                # Update or create the record based on the unique identifier
                obj, created = cls.objects.update_or_create(
                    dimensi=kepuasan_score.dimensi,
                    question_id=kepuasan_score.question_id,
                    defaults={
                        'score_difference': score_difference,
                        'average_score_difference': None,  # Since we are calculating score_difference here
                    }
                )
                scores.append(obj)

        # Perform a bulk update if needed (existing records)
        if scores:
            cls.objects.bulk_update(scores, ['score_difference', 'average_score_difference'])

    @classmethod
    def update_average_score_difference(cls):
        averages = cls.objects.values('dimensi').annotate(average_score_difference=Avg('score_difference'))
        for average in averages:
            dimensi = average['dimensi']
            avg_score_difference = average['average_score_difference']
            cls.objects.filter(dimensi=dimensi).update(average_score_difference=avg_score_difference)

    class Meta:
        db_table = 'tb_score_dimensi'

class count_user_umum(models.Model):
    question = models.ForeignKey(Tb_soal_kepuasan_umum, on_delete=models.CASCADE)
    user_count = models.IntegerField(default=0)  # Set a default value for user_count

    def save(self, *args, **kwargs):
        if self.user_count is None:
            self.user_count = 0  # Set a default value if user_count is None
        super().save(*args, **kwargs)

class tb_score_lvl(models.Model):
    lvl_kepuasan = models.ForeignKey(Tb_kategori_soal, on_delete=models.CASCADE)
    total_score_lvl_kepentingan = models.IntegerField(default=0)
    total_score_lvl_kepuasan = models.IntegerField(default=0)
    score_difference = models.IntegerField(default=0)  # New field for storing the score difference

    def __str__(self):
        return self.lvl_kepuasan.name
    
    @classmethod
    def calculate_score_difference(cls):
        scores = []
        kepentingan_scores = score_lvl_kepentingan.objects.all()
        for kepuasan_score in score_lvl_kepuasan.objects.all():
            kepentingan_score = kepentingan_scores.filter(lvl_kepuasan=kepuasan_score.lvl_kepuasan).first()
            if kepentingan_score:
                score_difference = kepuasan_score.total_score - kepentingan_score.total_score

                # Update or create the record based on the unique identifier
                obj, created = cls.objects.update_or_create(
                    lvl_kepuasan=kepuasan_score.lvl_kepuasan,
                    defaults={
                        'total_score_lvl_kepuasan': kepuasan_score.total_score,
                        'total_score_lvl_kepentingan': kepentingan_score.total_score,
                        'score_difference': score_difference,
                    }
                )
                scores.append(obj)

        # Perform a bulk update if needed (existing records)
        if scores:
            cls.objects.bulk_update(scores, ['total_score_lvl_kepuasan', 'total_score_lvl_kepentingan', 'score_difference'])

    class Meta:
        db_table = 'tb_score_lvl'

class UserComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    saran = models.TextField()
    komentar = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)  # Default to current timestamp
    sentiment = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.pub_date}"
    
    class Meta:
        db_table = 'user_comment'