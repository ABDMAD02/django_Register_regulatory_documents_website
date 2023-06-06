from django.core.exceptions import ValidationError


def validate_file_size(value):
    filesize= value.size
    
    if filesize > 10485760:
        raise ValidationError("РАЗМЕР ФАЙЛА НЕ ДОЛЖЕН ПРЕВЫШАТЬ 10мб")
    else:
        return value
