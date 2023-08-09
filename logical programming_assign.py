#TASK 1

p = True
q = False
r = True

# Question (p∨¬q) and q

var_1 = p or not q # True
ans_1 = var_1 and q #False
print(ans_1)

# Question (p or q) not (¬q and ¬p)

var_2 = p or q #True
var_3 = not (not q and not p) #True

ans_2 = var_2 and var_3
print(ans_2)

#Question (p ∨ q) ∧ (p or  ¬ q)

var_4 = p or q # True
var_5 = p or not q #True
ans_3 = var_4 and var_5
print(ans_3)

#Question p ∨ (q ∧ r)

var_6 = q and r #False
ans_4 = p or var_6 #True

print(ans_4)

#Question ¬(p ∧ q) ∨ (p ∨ q) 

var_7 = not(p and q) #True
var_8 = p or q       #True
ans_5 = var_7 or var_8

print(ans_5)

#TASK 2
a = True
b = False
c = True

# Question a and  b ∧ ¬c =  a or (b ∧ (¬c))
var_x = a and b and not c # False
var_y = a or b  and not c # False

ans_6 = var_x = var_y

print(ans_6)

#Question (p ∧ q) ∨ (¬p ∧ q) ∨ (¬p ∧ ¬q)
var_s = p and q # False
var_t = not p and q #False
var_u = not p and not q #False

ans_7 = var_s or var_t or var_u
print(ans_7)






