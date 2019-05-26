import os
from rospkg import RosPack



def get_package_path(package_name, *paths):
    """
    return the system path of a file or folder in a ROS package
    Example: get_package_path('mas_perception_libs', 'ros', 'src', 'mas_perception_libs')

    :type package_name: str
    :param paths: chunks of the file path relative to the package
    :return: file or directory full path
    """
    rp = RosPack()
    pkg_path = rp.get_path(package_name)
    return os.path.join(pkg_path, *paths)
