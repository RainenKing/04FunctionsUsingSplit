def math_equasion(equasion):
  n1, op, n2 = equasion.split(" ")

  n1 = int(n1)
  n2 = int(n2)
  
  if op == "+":
    return n1 + n2
  elif op == "-":
    return n1 - n2
  elif op == "*":
    return n1 * n2
  elif op == "/":
    return n1 / n2

print("enter math equasion:")
equasion = input()
print("result:", math_equasion(equasion))

