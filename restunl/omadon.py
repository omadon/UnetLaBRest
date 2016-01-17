from restunl.server import RestServer

def app1():
    server = RestServer('192.168.63.148')
    result = server.get_object('/status')

    print "I got " + str(result.status_code) +" from the server. Here is the resault:\n"
    print result.text
    print "\n"
    print result.json()['message'] + "\n"
    print result.json()['data']['version']

if __name__ == '__main__':
    app1()
