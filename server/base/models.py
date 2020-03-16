from django.db import models


class BaseModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __repr__(self):
        fields = " ".join(
            ["{}={}".format(f.name, getattr(self, f.name)) for f in self._meta.fields]
        )

        return f"<{type(self).__name__}: {fields} >"
