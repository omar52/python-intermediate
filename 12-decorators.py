# def My_decorator(func):
#     def warpper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return warpper

# @My_decorator
# def say_hello():
#     print(f"Hello, World!")
    
# say_hello()

# timer decorator
# import time

# def timer_decorator(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         elapsed_time = end_time - start_time
#         print(f"Function '{func.__name__}' took {elapsed_time:.5f} seconds to complete.")
#         return result
#     return wrapper

# @timer_decorator
# def long_task():
#     time.sleep(1.225699)
#     print("Task completed.")
    
# long_task()



# Authentication decorator

# user1 = {"name": "Omar", "logged_in": True}
# user2 = {"name": "Ali", "logged_in": False}

# def require_login(func):
#     def wrapper(user, *args, **kwargs):
#         if user.get('logged_in'):
#             return func(user, *args, **kwargs)
#         else:
#             print("Access denied. Please log in.")
#     return wrapper


# @require_login
# def view_dashboard(user):
#     print(f"Welcome to the dashboard, {user['name']}!")
# view_dashboard(user1)  # Should print the welcome message
# view_dashboard(user2)  # Should print "Access denied. Please log in." 


# decorator that accepts arguments

def require_role(role):
    def decorator(func):
        def wrapper(user):
            if user.get("role") != role:
                print(f"Access denied. {user['name']} is not a {role}.")
                return
            return func(user)
        return wrapper
    return decorator

@require_role("admin")
def delete_user(user):
    print(f"User deleted by {user['name']}.")

admin = {"name": "Omar", "role": "admin"}
guest = {"name": "Ali", "role": "guest"}

delete_user(admin)  # Allowed
delete_user(guest)  # Denied