import os
import yaml

ALLOWED_YAML_EXTENSIONS = ['.yaml', '.yml']

def load_yaml_file(yaml_path):
    """Loads the given YAML file and returns the loaded dictionary.
    Raises an OSError if the provided path is not a file, and
    a ValueError if the file does not have a .yaml or .yml extension.

    Keyword arguments:
    yaml_path: str -- path to the YAML file to be loaded

    """
    if not os.path.isfile(yaml_path):
        raise OSError('{0} is not a valid file'.format(yaml_path))

    filename, file_extension = os.path.splitext(yaml_path)
    if not file_extension:
        raise ValueError('Could not determine the file extension of {0}'.format(yaml_path))
    if file_extension not in ALLOWED_YAML_EXTENSIONS:
        raise ValueError('Only extensions {0} are allowed'.format(ALLOWED_YAML_EXTENSIONS))

    file_contents = None
    with open(yaml_path, 'r') as yaml_file:
        file_contents = yaml.safe_load(yaml_file)
    return file_contents
