from .enhanced_exception import EnhancedException


class PermissionDeniedException(EnhancedException):
    def _get_error_details(self, detail, message):
        detail = detail['detail']
        return super()._get_error_details(detail, message)
