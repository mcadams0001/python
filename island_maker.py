def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)
    return wrap

class Trace:
    def __init__(self) -> None:
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print('Calling {}'.format(f))
            return f(*args,**kwargs)
        return wrap

tracer = Trace()

class IslandMaker:
    def __init__(self,suffix) -> None:
        self.suffix=suffix

    @tracer
    def make_island(self, name):
        return name + self.suffix