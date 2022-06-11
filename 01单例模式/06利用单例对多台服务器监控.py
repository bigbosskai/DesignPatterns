class HealthCheck():
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not HealthCheck._instance:
            HealthCheck._instance = super(HealthCheck, cls).__new__(cls, *args, **kwargs)
        return HealthCheck._instance

    def __init__(self):
        self._servers = []

    def addServer(self):
        self._servers.append('server 1')
        self._servers.append('server 2')
        self._servers.append('server 3')
        self._servers.append('server 4')

    def changeServer(self):
        self._servers.pop()
        self._servers.append('server 5')


hc1 = HealthCheck()
hc2 = HealthCheck()

hc1.addServer()

for i in range(4):
    print(hc1._servers[i])

hc2.changeServer()

for i in range(4):
    print(hc1._servers[i])
