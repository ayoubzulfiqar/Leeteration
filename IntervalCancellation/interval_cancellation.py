import time
import threading

output = []

def cancellable(fn, args, t):
    cancel_event = threading.Event()
    start_time_real = time.time()
    
    def _interval_worker():
        call_count = 0
        while not cancel_event.is_set():
            expected_call_time_ms = call_count * t
            
            result = fn(*args)
            output.append({"time": expected_call_time_ms, "returned": result})
            
            call_count += 1
            
            actual_elapsed_ms = int((time.time() - start_time_real) * 1000)
            
            time_to_sleep_ms = (call_count * t) - actual_elapsed_ms
            
            if time_to_sleep_ms > 0:
                cancel_event.wait(time_to_sleep_ms / 1000.0)
            else:
                pass
    
    thread = threading.Thread(target=_interval_worker, daemon=True)
    thread.start()

    def cancel_fn():
        cancel_event.set()
        
    return cancel_fn