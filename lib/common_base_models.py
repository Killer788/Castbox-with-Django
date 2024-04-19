from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created At'
    )

    class Meta:
        abstract = True

    def __str__(self):
        raise NotImplementedError('Please implement __str__ method.')


class BaseModelWithUpdatedAt(BaseModel):
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Updated At'
    )

    class Meta:
        abstract = True

    def __str__(self):
        raise NotImplementedError('Please implement __str__ method.')


class BaseModelWithIsActive(BaseModelWithUpdatedAt):
    is_active = models.BooleanField(
        default=True,
        verbose_name='Is Active'
    )

    class Meta:
        abstract = True

    def __str__(self):
        raise NotImplementedError('Please implement __str__ method.')


class BaseModelWithTitleAndDescription(BaseModelWithIsActive):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name="Title", unique=True)
    description = models.TextField(null=False, blank=False, verbose_name="Description")

    class Meta:
        abstract = True

    def __str__(self):
        raise NotImplementedError('Please implement __str__ method.')
