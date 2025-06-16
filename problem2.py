
def log_execution(func):
    def wrapper(a,b):
        print("starting function")
        func(a,b)
        print("function finished")
    return wrapper

@log_execution

def calculate_sum(a,b):
    print(a+b)


calculate_sum(5,6)
