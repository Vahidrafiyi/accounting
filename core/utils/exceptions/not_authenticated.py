from .enhanced_exception import EnhancedException


class NotAuthenticatedException(EnhancedException):
    default_detail = ('Authentication credentials were not provided.')
    default_code = 'not_authenticated'