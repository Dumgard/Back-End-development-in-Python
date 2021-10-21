# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


class CustomMeta(type):

    @staticmethod
    def wrapper(func):
        def wrap(self, *args, **kwargs):
            func(self, *args, **kwargs)
            new_dict = {}
            for key, val in self.__dict__.items():
                new_dict['custom_' + key] = val
            self.__dict__ = new_dict

        return wrap

    def __new__(cls, name, bases, dct):
        new_dct = {}
        for key, val in dct.items():
            if key[:2] == '__' and key[-2:] == '__':
                new_dct[key] = val
                continue
            new_dct['custom_' + key] = val
        new_class = super().__new__(cls, name, bases, new_dct)
        setattr(new_class, '__init__', CustomMeta.wrapper(new_class.__dict__['__init__']))
        return new_class
