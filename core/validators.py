from django.core import exceptions
from django.core.exceptions import ValidationError


def validate_only_letters(string):
    for ch in string:
        if not ch.isalpha():
            raise exceptions.ValidationError('Please use only letters')


def validate_file_less_than_5mb(image):
    filesize = image.file.size
    megabyte_limit = 5.0
    if filesize > megabyte_limit * 1024 * 1024:
        raise ValidationError(f"Max file size is {megabyte_limit}MB")
