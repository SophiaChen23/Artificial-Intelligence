############################################################
# CMPSC 442: Homework 1
############################################################

student_name = "Zhihe Chen"

############################################################
# Section 1: Python Concepts
############################################################

python_concepts_question_1 = """
Strong typing means that the type of a value doesn't suddenly change. Every change of type requires an explicit conversion.
Dynamic typing means that runtime objects (values) have a type, as opposed to static typing where variables have a type.
Example: a="apple"
a+1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: must be str, not int
Example: employeeName = 9
employeeName = "Steve Ferg"

"""

python_concepts_question_2 = """
TypeError                                 Traceback (most recent call last)
<ipython-input-3-9c967c03e560> in <module>()
----> 1 points_to_names = {[0, 0]: "home", [1, 2]: "school", [-1, 1]: "market"}

TypeError: unhashable type: 'list'

unhashable type: 'list',dictionary keys must be immutable types 
(if key can change, there will be problems), and list is a mutable type.
you'll have to change your list into tuples

points_to_names = {(0, 0): "home", (1, 2): "school", (-1, 1): "market"} 

"""

python_concepts_question_3 = """
Second function is faster, On the first function each concatenation a new copy of the string is created, so that the overall complexity is O(n^2).
While for the second function, it is O(n), second is faster.
"""

############################################################
# Section 2: Working with Lists
############################################################

def extract_and_apply(l, p, f):
    return [f(x) for x in l if p(x)]

def concatenate(seqs):
    return [x for y in seqs for x in y]

def transpose(matrix):
    if not matrix: return []
    row, column = len(matrix), len(matrix[0])

    res = [[[] for i in range(row)] for i in range(column)]

    for x in range(row):
        for y in range(column):
            res[y][x] = matrix[x][y]

    return res

############################################################
# Section 3: Sequence Slicing
############################################################

def copy(seq):
    return x[:]

def all_but_last(seq):
    if not seq:
        return seq
    else:
        return seq[:-1]

def every_other(seq):
    return x[::2]

############################################################
# Section 4: Combinatorial Algorithms
############################################################

def prefixes(seq):
    for x in range(len(seq) + 1):
        yield (seq[0:x])

def suffixes(seq):
    for x in range(len(seq) + 1):
        yield (seq[x:len(seq) + 1])

def slices(seq):
    length = len(seq)
    for x in range(length):
        for y in range(x + 1, length + 1):
            yield (seq[x:y])

############################################################
# Section 5: Text Processing
############################################################

def normalize(text):
    return " ".join(text.lower().split())

def no_vowels(text):
    return text.translate(None, "aeiouAEIOU")

def digits_to_words(text):
    alist = ""
    num = [int(x) for x in text if x.isdigit()]
    dict = {1: "one ", 2: "two ", 3: "three ", 4: "four ", 5: "five ", 6: "six ", 7: "seven ", 8: "eight ", 9: "nine ",
            0: "zero "}
    for x in num:
        alist += dict[x]
    return alist[:-1]

def to_mixed_case(name):
    temp, res = name.split("_"), ""
    temp = [x for x in temp if x]

    for pos, value in enumerate(temp):
        if pos == 0:
            res += value.lower()
        else:
            res += value.capitalize()
    return res

############################################################
# Section 6: Polynomials
############################################################

class Polynomial(object):
    def __init__(self, polynomial):
        self.polynomial = polynomial

    def get_polynomial(self):
        return tuple(self.polynomial)

    def __neg__(self):
        x = [(-x[0], x[1]) for x in self.polynomial]
        return Polynomial(x)

    def __add__(self, other):
        x = self.polynomial + other.polynomial
        return Polynomial(x)

    def __sub__(self, other):
        x = [(-x[0], x[1]) for x in other.polynomial]
        return Polynomial(self.polynomial + x)

    def __mul__(self, other):
        xx = []
        for x in self.polynomial:
            for y in other.polynomial:
                xx.append((x[0] * y[0], x[1] + y[1]))
        return Polynomial(xx)

    def __call__(self, x):
        res = 0
        for val in self.polynomial:
            res += (x ** val[1]) * val[0]
        return res

    def simplify(self):
        dic, rest = {}, []
        for x in self.polynomial:
            if x[1] in dic.keys():
                dic[x[1]] += x[0]
            else:
                dic[x[1]] = x[0]
        for key, value in dic.items():
            if value != 0: rest.append((value, key))
        if len(rest) == 0:
            self.polynomial = [(0, 0)]
        else:
            self.polynomial = sorted(rest, key=lambda x: x[1], reverse=True)

    def __str__(self):
        astr = ""
        for x in self.polynomial:
            if x[0] == 1 and x[1] == 0:
                temp = "+ 1 "
            elif x[0] == -1 and x[1] == 0:
                temp = "- 1 "
            else:

                if x[0] == 1:
                    temp = '+ '
                elif x[0] == -1:
                    temp = "- "
                elif x[0] < 0:
                    temp = "- " + str(abs(x[0]))
                else:
                    temp = "+ " + str(x[0])

                if x[1] == 1:
                    temp += "x "
                elif x[1] == 0:
                    temp += " "
                else:
                    temp += "x" + "^" + str(x[1]) + " "
            astr += temp

        if astr[0] == "+":
            return (astr[2:-1])
        else:
            return ("-" + astr[2:-1])


############################################################
# Section 7: Feedback
############################################################

feedback_question_1 = """
2 hours
"""

feedback_question_2 = """
polynomial 8
they are not diffcult, just trouble, need to consider mutiple situation
"""

feedback_question_3 = """
polynomial part, there are several underscore function which can let you to define
Nope
"""
