import typing as t


def handle_args(arg: t.Any, args: t.Sequence = None, *args_: tuple):
    args = args or tuple()

    try:
        len(arg)
        iter(arg)
        if not isinstance(arg, (str, dict)):
            return tuple(arg)
    except TypeError:
        pass

    if not isinstance(args, tuple):
        args = (args,)

    return (arg,) + args + args_
