REST_SCHEMA = {
    'login': '/auth/login',
    'logout': '/auth/logout',
    'status': '/status',
    'list_templates': '/templates'
}

class UnlServer(RestServer):
    def __init__(self,address):

