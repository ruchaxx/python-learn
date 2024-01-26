def new_decorator(original_func):
    def wrap_func():
        print("before original func")
        original_func()
        print("after original func")
    return wrap_func

@new_decorator            # ---> decor_func = new_decorator(func_need_decorator)
def func_need_decorator():
    print("want to be decorator")

func_need_decorator()    # ----> decor_func()