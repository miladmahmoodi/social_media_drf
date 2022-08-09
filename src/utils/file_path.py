import os
from uuid import uuid4


def get_file_path(instance, file_name, category):
    """
    return new file path with special path
    """
    ext = file_name.split('.')[-1]
    file_name = '{}.{}'.format(uuid4(), ext)
    return os.path.join(f'user/{instance.user.id}/{category}/', file_name)

    class Meta:
        abstract = True
