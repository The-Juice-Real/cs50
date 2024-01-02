def f(*args, **kwargs):
    print("Named:", kwargs)

f(galleons = 100, sickles=50, knuts=25)

#**kwargs is a automatically a dictionary key:value

#*args is automatically a tuple