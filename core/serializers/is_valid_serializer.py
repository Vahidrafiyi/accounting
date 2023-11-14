from ..utils.exceptions.bad_request import BadRequestException


class IsValidSerializer:
    def is_valid(self, *, raise_exception = False):
        super().is_valid()
        # If validation errors occur and we intend to raise exceptions, we gather these errors to be included in the exception response.
        if self._errors and raise_exception:
            details = ''.join(f'{key}, ' for key in self.errors.keys())
            raise BadRequestException(details)

        # Finally, return the result of calling the `is_valid` method again, which should be True if there are no errors.
        return super().is_valid(raise_exception=raise_exception)
