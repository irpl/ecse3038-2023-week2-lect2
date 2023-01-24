import math

def area_of_circle(r):
  a = math.pi * r**2
  return a

def volume_of_sphere(r):
  v = (4*(math.pi * r**3))/3
  return v

print(area_of_circle(5))
print(volume_of_sphere(56))