import os
from rospkg import RosPack
from actionlib_msgs.msg import GoalStatus


ACTIONLIB_STATUS_NAMES = {
    GoalStatus.PENDING:    'PENDING',
    GoalStatus.ACTIVE:     'ACTIVE',
    GoalStatus.PREEMPTED:  'PREEMPTED',
    GoalStatus.SUCCEEDED:  'SUCCEEDED',
    GoalStatus.ABORTED:    'ABORTED',
    GoalStatus.REJECTED:   'REJECTED',
    GoalStatus.PREEMPTING: 'PREEMPTING',
    GoalStatus.RECALLING:  'RECALLING',
    GoalStatus.RECALLED:   'RECALLED',
    GoalStatus.LOST:       'LOST'
}


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
