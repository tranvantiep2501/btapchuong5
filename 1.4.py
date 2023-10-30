import math
  
  a = float(input("gia tri a: "))
  b = float(input("gia tri b: "))
  c = float(input("gia tri c: "))
  p = (a + b + c) / 2
  s = math.sqrt(p * (p - a) * (p - b) * (p - c))
  print(s,"là dien tich tam giac co canh abc")
