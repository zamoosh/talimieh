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
        return f'{self.title} status: {self.status}'


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
        return f'{self.degree_field_study.title}'


class EducationalRequest(models.Model):
    REQUEST_STEPS = [
        (1, 'must be approved by a register expert'),
        (2, 'must be approved by an educational expert'),
        (3, 'must be approved by a financial expert'),
        (4, 'must be re-approved by the educational expert'),
        (5, 'must be re-approved by the financial expert'),
        (6, 'educational expert must approved final submit'),
        (7, 'request is submitted'),
        (0, 'request is rejected')
    ]
    step = models.CharField(default=REQUEST_STEPS[0], max_length=1, choices=REQUEST_STEPS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    average = models.CharField(max_length=10, blank=True, null=True)
    former_field_study = models.CharField(max_length=25, blank=True, null=True)
    former_university = models.CharField(max_length=25, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    request_expert_register = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True,
                                                related_name='request_expert_register')
    request_expert_financial = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True,
                                                 related_name='request_expert_financial')
    request_expert_educational = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True,
                                                   related_name='request_expert_educational')
    final_status = models.BooleanField(default=False)
    reject = models.BooleanField(default=False)
    tracking_code = models.CharField(max_length=20, blank=True, null=True)
    paid = models.BooleanField(default=False)
    total_coast = models.PositiveIntegerField(default=0, blank=True, null=True)

    class Meta:
        permissions = [
            ('can_see_educational_request', 'can see educational request'),
            ('can_see_financial_request', 'can see financial request'),
            ('can_see_register_request', 'can see register request')
        ]

    def get_step(self):
        index = int(self.step[1]) - 1
        if int(self.REQUEST_STEPS[index][0]) == 1:
            return 'باید توسط کارشناس ثبت‌نام تائید شود'
        elif int(self.REQUEST_STEPS[index][0]) == 2:
            return 'باید توسط کارشناس آموزشی تائید شود'
        elif int(self.REQUEST_STEPS[index][0]) == 3:
            return 'باید توسط کارشناس مالی تائید شود'
        elif int(self.REQUEST_STEPS[index][0]) == 4:
            return 'باید دوباره توسط کارشناس آموزشی تائید شود'
        elif int(self.REQUEST_STEPS[index][0]) == 5:
            return 'باید دوباره توسط کارشناس مالی تائید شود'
        elif int(self.REQUEST_STEPS[index][0]) == 6:
            return 'کارشناس آموزشی باید آخرین تائید را انجام دهد'
        elif int(self.REQUEST_STEPS[index][0]) == 7:
            return 'درخواست به طور کامل تائید شده است'
        elif int(self.REQUEST_STEPS[index][0]) == 0:
            return 'درخواست شما رد شده است'

    def __str__(self):
        return f'{self.id} {self.user}'


class StudentCard(models.Model):
    educational_request = models.OneToOneField(EducationalRequest, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.educational_request.user}'


class Option(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(null=True, blank=True, auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'


class SelectedOption(models.Model):
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    request = models.ForeignKey(EducationalRequest, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.option.name}'


class SelectedSemester(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    educational_request = models.ForeignKey(EducationalRequest, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.semester}'


def owner_image(instance, filename):
    return "%s/%s/%s" % ('document', instance.id, filename)


class OwnerDocument(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    image = models.ImageField(blank=True, null=True)
    educational_request = models.ManyToManyField(EducationalRequest)
    eof = models.IntegerField(default=0)
    document_pattern = models.ForeignKey(DocumentPattern, on_delete=models.SET_NULL, null=True)

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
    educational_request = models.ForeignKey(EducationalRequest, on_delete=models.CASCADE, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    message_expert = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='message_expert')
    user_seen = models.BooleanField(default=False, blank=True, null=True)
    user_seen_date = models.DateTimeField(default=None, blank=True, null=True)
    expert_seen = models.BooleanField(default=False, blank=True, null=True)
    expert_seen_date = models.DateTimeField(default=None, blank=True, null=True)

    def __str__(self):
        return f'message: owner: {self.owner} expert: {self.message_expert}'
