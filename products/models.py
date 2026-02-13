from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    parent = models.ForeignKey('self', verbose_name=_('parent'), blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(_('title'),max_length=50)
    description = models.TextField(_('description'), blank=True)
    avatar = models.ImageField(_('avatar'), blank=True, upload_to='categories/')
    is_enable = models.BooleanField(_('is enable'), default=True)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)

    class Meta:
        db_table = 'categories' #Имя таблицы в базе данных - The name of the table in the database
        verbose_name = _('category') #Единственное название в админ-панеле - The singular name in admin panel
        verbose_name_plural = _('Categories') #Множественное название в админ-панеле - The plural name in admin panel

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(_('title'), max_length=50)
    description = models.TextField(_('description'), blank=True)
    avatar = models.ImageField(_('avatar'), blank=True, upload_to='products/')
    is_enable = models.BooleanField(_('is enable'), default=True)
    categories = models.ManyToManyField('Category', verbose_name=_('categories'), blank=True)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)

    class Meta:
        db_table = 'products' #название таблицы в базе данных - The name of the table in the database
        verbose_name = _('product') #Единственное название в админ-панеле - The singular name in admin panel
        verbose_name_plural = _('products') #Множественное название в админ-панеле - The plural name in admin panel


    def __str__(self):
        return self.title

class File(models.Model):
    FILE_PHOTO = 1
    FILE_AUDIO = 2
    FILE_VIDEO = 3
    FILE_PDF = 4
    FILE_TYPES = (
        (FILE_PHOTO, _('photo')),
        (FILE_AUDIO, _('audio')),
        (FILE_VIDEO, _('video')),
        (FILE_PDF, _('pdf'))
    )


    product = models.ForeignKey('Product', verbose_name=_('product'), on_delete=models.CASCADE, related_name='files')
    title = models.CharField(_('title'), max_length=50)
    file_type = models.PositiveSmallIntegerField(_('file type'), choices=FILE_TYPES, default=FILE_PHOTO)
    file = models.FileField(_('file'), upload_to='files/%Y/%m/%d/')
    is_enable = models.BooleanField(_('is enable'), default=True)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)

    class Meta:
        db_table = 'files' #название таблицы в базе данных - The name of the table in the database
        verbose_name = _('file') #Единственное название в админ-панеле - The singular name in admin panel
        verbose_name_plural = _('files') #Множественное название в админ-панеле - The plural name in admin panel


    def __str__(self):
        return self.title