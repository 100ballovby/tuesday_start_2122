''' чтобы научить функцию принимать данные,
нужно указать параметры в скобках при ее определении'''


def say_hello(u_name):  # <- параметр
    """Приветствует пользователя"""
    msg = f'Hello, {u_name}!'
    return msg

users = ['Mary', 'John', 'Alice', 'Max']
for user in users:
    print(say_hello(user))
