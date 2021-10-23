class CustomMeta(type):
    def foo(self, key, value):
        return object.__setattr__(self, 'custom_' + key, value)

    def __new__(cls, name, bases, dct):
        temp = dict()
        for key, value in dct.items():
            if not key.startswith('__'):
                temp['custom_' + key] = value
            else:
                temp[key] = value
        temp['__setattr__'] = CustomMeta.foo
        return super().__new__(cls, name, bases, temp)
