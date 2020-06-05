from pulp import LpProblem, LpVariable, LpConstraint, LpConstraintLE, LpConstraintGE, LpMaximize, LpBinary, LpStatus

# Create a new model
m = LpProblem(name="MIP Model", sense=LpMaximize)

# Create variables
x = LpVariable(cat=LpBinary, name="x")
y = LpVariable(cat=LpBinary, name="y")
z = LpVariable(cat=LpBinary, name="z")

# Add constraint: x + 2 y + 3 z <= 4
m += LpConstraint(e=(x + 2 * y + 3 * z),
                  sense=LpConstraintLE, rhs=4, name='c0')

# Add constraint: x + y >= 1
m += LpConstraint(e=(x + y), sense=LpConstraintGE, rhs=1, name='c1')

# Set objective
m.setObjective(x + y + 2 * z)

# Calculate with the default CBC optimizer
status = m.solve()

if LpStatus[status] == 'Optimal':

    for v in m.variables():
        print('%s %g' % (v.name, v.varValue))

    print('Obj: %g' % m.objective.value())
