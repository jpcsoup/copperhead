from collections import defaultdict


class userinput:

    def __init__(self, var_dict):
        self.vars = var_dict
        self.default_message = 'Enter value'

    def keys(self):
        return len(self.vars.keys())

    def ask(self):
        r = defaultdict()
        for k in self.vars.keys():
            r[k] = input(self.default_message + ': ' + k)
        self.r = r


x = {'filepath':{'type':'text', 'value':'test', 'message':'Please enter the filepath for '},
     'filename':{'type':'text', 'value':'test'},
     'parameter':{'type':'int', 'value':20}}

u = userinput(x)

u.keys()
u.ask()

