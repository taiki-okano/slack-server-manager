# coding: utf-8


class InitializationException(Exception):
    """
    Base class of exception in initialization.
    """


class InitializationNotAllowed(InitializationException):
    """
    Exception in case that initialization is not allowed
    because initialization has been done.
    """
    pass


class InitializationUnable(InitializationException):
    """
    Exception in case that initialization failed.
    """
    pass


class ExecutionException(Exception):
    """
    Base class of exception in execution.
    """
    pass


class ExecutionPermissionDenied(ExecutionException):
    """
    Excption in case that a user which try to execute a command
    is not registered.
    """
    pass


class ExecutionTimeout(ExecutionException):
    """
    Exception in case that an execution does not finish in time.
    """
    pass


class ExecutionFailure(ExecutionException):
    """
    Exception in case that an execution fail.
    """
    pass


class GrantException(Exception):
    """
    Base class of exception in grant.
    """
    pass


class GrantPermissionDenied(GrantException):
    """
    Exception in case that a user
    who try to grant another is not 'admin'.
    """
    pass


class GrantNoSuchLevel(GrantException):
    """
    Exception in case that a specified level
    which is granted is not suitable.
    """
    pass
