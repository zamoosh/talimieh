from .imports import *
from client.models import *


class Universities(models.Model):
    uni_name = models.CharField(max_length=50, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    document = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.uni_name


class YearSemester(models.Model):
    title = models.CharField(max_length=4)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    status = models.BooleanField(default=False)

    def get_status(self):
        return self.status

    def __str__(self):
        return f'{self.title} -> {self.status}'


class DegreeFieldStudy(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    document = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Semester(models.Model):
    university = models.ForeignKey(Universities, on_delete=models.CASCADE)
    degree_field_study = models.ForeignKey(DegreeFieldStudy, on_delete=models.CASCADE)
    year_semester = models.ForeignKey(YearSemester, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    scholarship = models.BooleanField(default=False)
    expert_price = models.CharField(max_length=25)
    entrance_price = models.CharField(max_length=25)

    def __str__(self):
        return self.degree_field_study.title + '  ' + self.university.uni_name


class EducationalRequest(models.Model):
    average = models.CharField(max_length=10, blank=True, null=True)
    field_study = models.CharField(max_length=25, blank=True, null=True)
    former_university = models.CharField(max_length=25, blank=True, null=True)
    college = models.ForeignKey(Semester, on_delete=models.CASCADE)
    document = models.ForeignKey(Owner_document, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    sent = models.BooleanField(default=False)
