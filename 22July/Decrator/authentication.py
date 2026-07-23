def authentication(func):
    def wrapper():
        print("Processing authentication")
        if logged_in:
            return func()
        else:
            print("Acces denied")

    return wrapper


logged_in = True


@authentication
def profile():
    print("Logged into profile")


profile()
