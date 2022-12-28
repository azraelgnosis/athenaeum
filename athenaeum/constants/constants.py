from abc import ABCMeta


class MetaConstant(type, metaclass=ABCMeta):
    def __new__(mcs, name: str, bases: tuple[type], attrs: dict):
        if name != "Constant":
            attrs['__consts__'] = {
                key: val for key, val in attrs.items()
                if isinstance(val, str) and key not in ('__module__', '__qualname__')}

            return super().__new__(mcs, name, bases, attrs)()
        return super().__new__(mcs, name, bases, attrs)

    def __init__(cls, name: str, bases: tuple[type], attrs: dict):
        super().__init__(name, bases, attrs)


class Constant(object, metaclass=MetaConstant):
    __consts__: dict

    def __len__(self):
        return len(self.__consts__)

    def __iter__(self):
        return iter(self.__consts__)

    def keys(self):
        return self.__consts__.keys()

    def values(self):
        return self.__consts__.values()

    def items(self):
        return self.__consts__.items()
