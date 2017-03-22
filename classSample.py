def scope_test():
    def do_local():
        spam = "local"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal"

    def do_global():
        global spam
        spam = "global"

    spam = "test spam"
    do_local()
    print("After local asignment:", spam)
    do_nonlocal()
    print("After nonlocal asignment:", spam)
    do_global()
    print("After global asignment:", spam)


scope_test()