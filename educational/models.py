from .imports import *


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
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
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
    REQUEST_STEPS = [
        (1, 'باید توسط کارشناس ثبت‌نام تائید شود'),
        (2, 'باید توسط کارشناس مالی تائید شود'),
        (3, 'باید توسط کارشناس آموزشی تائید شود')
    ]
    step = models.CharField(default=REQUEST_STEPS[1], max_length=1, choices=REQUEST_STEPS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=50, blank=False)
    average = models.CharField(max_length=10, blank=True, null=True)
    former_field_study = models.CharField(max_length=25, blank=True, null=True)
    former_university = models.CharField(max_length=25, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    request_expert = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True,
                                       related_name='request_expert')
    paid = models.BooleanField(default=False)
    status = models.BooleanField(default=False)
    sent = models.BooleanField(default=False)
    tracking_code = models.CharField(max_length=20, blank=True, null=True)

    def get_step(self):
        index = int(self.step[1])
        return self.REQUEST_STEPS[index][1]

    def __str__(self):
        return f'{self.id} {self.title} {self.user}'


class SelectedSemester(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    educational_request = models.ForeignKey(EducationalRequest, on_delete=models.CASCADE)

    def __str__(self):
        return f'selected semester: {self.semester} {self.educational_request.title}'


def owner_image(instance, filename):
    return "%s/%s/%s" % ('document', instance.id, filename)


class OwnerDocument(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    image = models.ImageField(blank=True, null=True, upload_to=owner_image)
    educational_request = models.ManyToManyField(EducationalRequest)

    class Meta:
        permissions = [
            ('can_accept_primary', 'can accept the primary document?'),
            ('can_accept_after_primary', 'can accept other document after primaries?')
        ]

    def save(self, *args, **kwargs):
        if self.image:
            if not self.id:
                img = self.image
                self.image = None
                super(OwnerDocument, self).save()
                self.image = img
            super(OwnerDocument, self).save()

    def __str__(self):
        return f' {str(self.id)} {self.title} {self.user.first_name} {self.user.last_name} {str(self.user.id)}'

    def delete(self, using=None, keep_parents=False):
        if self.image:
            self.image.delete(self.image.name)
        super(OwnerDocument, self).delete()


class Message(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    educational_request = models.ForeignKey(EducationalRequest, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    message_expert = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='message_expert')
    user_seen = models.BooleanField(default=False, blank=True, null=True)
    user_seen_date = models.DateTimeField(default=None, blank=True, null=True)
    expert_seen = models.BooleanField(default=False, blank=True, null=True)
    expert_seen_date = models.DateTimeField(default=None, blank=True, null=True)

    def __str__(self):
        return f'message: owner: {self.owner} expert: {self.message_expert}'
