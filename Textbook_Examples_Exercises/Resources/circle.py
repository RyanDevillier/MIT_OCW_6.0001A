pi = 3.141592653589793238462643383279502884197169399375105820974944592307816406286208998

def area(radius):
    return (pi * (radius ** 2.0))

def circumference(radius):
    return (2.0 * pi * radius)

def sphere_surface(radius):
    return (4.0 * area(radius))

def sphere_volume(radius):
    return ((4.0/3.0) * pi * (radius ** 3))
