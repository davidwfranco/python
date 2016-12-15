# To get value use raw_input() and convert after if needed
# also the prompt can be put inside the brackets

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()

weight = raw_input("How much do you weigh?")

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)
