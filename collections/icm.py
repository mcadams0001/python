class LoggingContextManager:
    def __enter__(self):
        print('LoggingContextManager.__enter__()')
        return 'You are in the block'

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
           print('LoggingContextManager.__exit__(): normal exit detected')
        else:
            print('LoggingContextManager.__exit__({},{},{})'.format(exc_type, exc_val, exc_tb))
        return

with LoggingContextManager() as x:
    print(x)


