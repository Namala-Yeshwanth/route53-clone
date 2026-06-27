class HostedZoneNotFoundException(
    Exception
):
    pass

class DuplicateHostedZoneException(
    Exception
):
    pass

class InvalidDNSRecordException(
    Exception
):
    pass

class DNSRecordNotFoundException(
    Exception
):
    pass

class UserAlreadyExistsException(
    Exception
):
    pass


class InvalidCredentialsException(
    Exception
):
    pass