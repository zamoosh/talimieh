from django.db import models


def document_pattern_image(instance, filename):
    return "%s/%s/%s" % ('document_pattern', instance.id, filename)


class DocumentPattern(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    size = models.IntegerField(default=16)
    sample = models.FileField(upload_to=document_pattern_image, null=True)
    types = models.JSONField(default=dict)
    extra = models.JSONField(default=dict)
    status = models.BooleanField(default=True)

    def get_types(self):
        types = ' '
        return types.join(self.types['types'])

    @staticmethod
    def split_types(types):
        t = []
        for item in types:
            if not (item.isspace() or item == ''):
                t.append(item)
        return t
