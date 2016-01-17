from restunl import RestServer

def application():
    server = RestServer('192.168.63.146')
    server.get_object('/status')

if __name__ == '__main__':
    application()
