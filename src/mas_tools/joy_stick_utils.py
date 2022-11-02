from enum import IntEnum


class LT_BUTTONS_MAP(IntEnum):
    """
    Button mappings for the Logitech Wireless Gamepad F710 as produced by the [`joy`](http://wiki.ros.org/joy)
    ROS package. Similar mappings to the  Microsoft Xbox 360 Wireless Controller.
    """
    A = 0
    B = 1
    X = 2
    Y = 3
    LB = 4
    RB = 5
    BACK = 6
    START = 7
    POWER = 8
    LEFT_STICK = 9
    RIGHT_STICK = 10


class LT_AXES_MAP(IntEnum):
    """
    Axes mappings for the Logitech Wireless Gamepad F710 as produced by the [`joy`](http://wiki.ros.org/joy)
    ROS package.
    """
    STICK_LEFT_LR = 0       # fully left: 1.0, fully right: -1.0
    STICK_LEFT_UD = 1       # fully up: 1.0, fully down: -1.0
    LT = 2                  # released: 1.0, fully pressed: -1.0
    STICK_RIGHT_LR = 3      # similar to STICK_LEFT_LR
    STICK_RIGHT_UD = 4      # similar to STICK_LEFT_UD
    RT = 5                  # similar to LT
    CROSS_KEY_LR = 6        # left: 1.0, right: -1.0
    CROSS_KEY_UD = 7        # up: 1.0, down: -1.0

