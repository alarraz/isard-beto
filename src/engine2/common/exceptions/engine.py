import pprint

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class NotFoundError(Error):
    def __init__(self, id, message):
        self.id = id
        self.message = message

class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message

class UnAcceptedValueConnectionHypParameters(Error):
    """Raised a connection to hypervisor if parameters are invalid.

    Attributes:
    """
    def __init__(self, data=None):
        self.data = data

    def __str__(self):
        return repr(f"Connection parameters are not well formatted. {self.data}")


class UnAcceptedEngineAction(Error):
    """ Raised a unaccepted Engine Action"""
    def __init__(self,msg,action,l_options=[]):
        self.action = action
        self.options = l_options

    def __str__(self):
        s_options = ','.join(self.options)
        return repr(f"Engine Action not valid. {self.msg}. Action:{self.action}. Options: {s_options}")


class ActionWaitTimeout(Error):
    """ Raised when an action has timeout error"""
    def __init__(self,timeout,action,d_options):
        self.action = action
        self.timeout = timeout
        self.d_options = d_options

    def __str__(self):
        s_options = pprint.pformat(self.d_options)
        return repr(f"Engine Action Timeout. Timeout: {self.timeout} seconds. Action:{self.action}. Options: {s_options}")

class ActionQueueFull(Error):
    def __init__(self,e):
        self.e = e

    def __str__(self):
        return repr(f"ActionQueueFull: {self.e}")