class Model:
    services = {
        'email': {'number': 1000, 'price': 2},
        'sms': {'number': 1000, 'price': 10},
        'voice': {'number': 1000, 'price': 15}
    }


class View:
    def list_services(self, services):
        for svc in services:
            print(svc, ' ')

    def list_prices(self, services):
        for svc in services:
            print("For", Model.services[svc]['number'], svc, "message you pay $", Model.services[svc]['price'])


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def get_service(self):
        services = self.model.services.keys()
        return (self.view.list_services(services))

    def get_pricing(self):
        services = self.model.services.keys()
        return (self.view.list_prices(services))


if __name__ == '__main__':
    controller = Controller()
    controller.get_service()
    controller.get_pricing()
