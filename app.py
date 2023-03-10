import math

def area_of_circle(r):
  a = math.pi * r**2
  return a

def volume_of_sphere(r):
  v = (4*(math.pi * r**3))/3
  return v

def pythag(a, b):
  c = math.sqrt(a**2 + b**2)
  return c

def summation():
  result = 0

  for n in range(1, 21):
    result += math.sqrt(((n + 5)**5)/2)
  
  return result


print(area_of_circle(5))
print(volume_of_sphere(56))
print(pythag(2,3))
print(summation())