# Considering two expressions
# first_expr = 5 * (b + a)
# second_expr = 5 * b + a 

#1.first_expr = 3 * (b + a) tree represetation is;
#    *
#  /   \
# 5      +
#       /  \
#      b     a

#1.second_expr = 5 * b + a tree representation is;
#       +
#     /   \
#    *      a
#   /  \
# 5     b

#Note: Root is on top and leaves on bottom
#This case, syntax trees could be solved other ways eg strings but trees are more appropriate
#These are 1-dim structure representing a 2-dim data structure

#We are going to represent these trees as objects in python

#Defining a class Expressions and sub classes of expressions
class Expr:
    pass

#Sub classes of expressions are 1. operators(+, *, -), 2. numbers(Constants)
#3. variables
class Times(Expr):
    #method to create the Times tree
    #for times object we expect two expressions, one on l and another on r
    def __init__(self, left, right):
        self.left = left
        self.right = right

    #using dunder __str__ mtd to return representation of the obj as a string
    def __str__(self):
        return "(" + str(self.left) + "*" + str(self.right) + ")" #recursion since str calls __str__

    #now to evaluate our expressions
    def eval(self, env):
        return self.left.eval(env) * self.right.eval(env)

class Plus(Expr):
    #method to create the plus tree
    def __init__(self, left, right):
        self.left = left
        self.right = right

        #using dunder __str__ mtd to return representation of the obj as a string
    def __str__(self):
        return "(" + str(self.left) + "+" + str(self.right) + ")"

    #now to evaluate our expressions
    def eval(self, env):
        return self.left.eval(env) + self.right.eval(env)

class Const(Expr):
    def __init__(self, val):
        self.val = val

    #using dunder __str__ mtd to return representation of the obj as a string
    def __str__(self):
        return str(self.val)

    def eval(self, env):
        return self.val

class Var(Expr):
    def __init__(self, name):
        self.name = name

    #using dunder __str__ mtd to return representation of the obj as a string
    def __str__(self):
        return self.name

    def eval(self, env):
        return env[self.name]


first_expr = Times(Const(5), Plus(Var("b"), Var("a")))
#print(first_expr) #gives us string representation of expression 5 * (b + a)
#(5*(b+a))

second_expr = Plus(Times(Const(5), Var("b")), Var("a"))
#print(second_expr) #gives us string representation of expression 5 * b + a
#((5*b)+a)

#evaluating our mathematical expressions using variables from expr_vars dict
expr_vars = {"b" : 4, "a" : 2}

#print(first_expr.eval(expr_vars))
#30
#print(second_expr.eval(expr_vars))
#22
