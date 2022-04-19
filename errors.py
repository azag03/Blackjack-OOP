class CallError(Exception):
    """Raised when player tries to complete an invalid command."""

    def __init__(self, message='Cannot process command'):
        self.message = message

    def __str__(self):
        return f'{self.message}'
