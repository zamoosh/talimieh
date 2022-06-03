from django.db import models


class DocumentPattern(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    types = models.JSONField(default=dict)
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
