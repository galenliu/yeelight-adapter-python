from gateway_addon import Action


class YeelightEffect(Action):

    def __init__(self, id_, device, name, input_):
        super().__init__(id_, device, name, input_)

    def start(self):
        print("input")
