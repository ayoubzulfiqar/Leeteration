import threading

def cancellable(fn, args, t):
    cancelled = [False]

    def _execute_fn():
        if not cancelled[0]:
            fn(*args)

    timer = threading.Timer(t / 1000.0, _execute_fn)
    timer.start()

    def cancelFn():
        if not cancelled[0]:
            cancelled[0] = True
            timer.cancel()

    return cancelFn