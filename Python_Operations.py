a= 10
b = 5

#Addition
c = a + b
#print(c)

#Subtraction
d = a - b
#print(d)

#Multiplication
e = a * b
#print(e)

#Division
f = a / b
#print(b)

#Modulus
g = a % b
#print(g)

#Division floor
h = a // b
#print(h)

#Power
i = a ** b
#print(i)


#LOGICAL OPERATIONS
#Question 1 : ((P ∨ Q) ∧ R) v ((P ∧ R) ∨ (Q ∧ R))

P= True
Q = True
R = False

var_1 = P and Q      #(P v Q) - True

var_2 = var_1 and R  #((P ∨ Q) ∧ R))  - False

var_3 = P and R      #(P ∧ R) - False

var_4 = Q and R      # (Q ∧ R) - False

ans_1 = var_2 or var_3 and var_4

print("Answer is", ans_1)


#Question 2 : (-P ^ - Q) v (Q ^ -R)

var_a = not(P and Q)   # (-P ^ - Q) #False
var_b = Q and not R    # (Q ^ -R) #True

ans_2 = var_a or var_b # True

print("Answer is", ans_2)


