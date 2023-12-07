## Advanced Python Decorator Functions

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
        else:
            print(f"User {args[0].name} not authenticated!")
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

new_user = User("Raúl")
new_user.is_logged_in = True
new_user2 = User("Pedro")
create_blog_post(new_user)
create_blog_post(new_user2)

