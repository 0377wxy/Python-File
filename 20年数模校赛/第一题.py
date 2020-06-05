from pulp import LpProblem, LpVariable, LpConstraint, LpConstraintLE, LpConstraintGE, LpMaximize, LpBinary, LpStatus, LpMinimize
import pandas as pd
import numpy as np
from scipy.optimize import linprog

df1 = pd.read_excel(
    'D:\\Program_file\\Python-File\\20年数模校赛\\data.xlsx', sheet_name='运动鞋')
df1['双鞋后的宽'] = df1['高度（cm）'] * 2 - df1['两只鞋共用空间（cm）']
df1['双鞋的面积'] = (df1['长度（cm）']+1) * (df1['双鞋后的宽']+1)


df2 = pd.read_excel(
    'D:\\Program_file\\Python-File\\20年数模校赛\\data.xlsx', sheet_name='鞋盒')
df2['盒子的面积'] = df2['长度（cm）'] * df2['宽度（cm）']


judge = []
for i in range(15):
    li = []
    s = []
    for j in range(23):
        if float(df1.iloc[i][1]) + 1 <= float(df2.iloc[j][1]) and \
                float(df1.iloc[i][5]) + 1 <= float(df2.iloc[j][2]) and \
                float(df1.iloc[i][3]) + 1 <= float(df2.iloc[j][3]) and \
                float(df1.iloc[i][6]) >= float(df2.iloc[j][4]) * 0.7:
            li.append(1)
            s.append(j+1)
        else:
            li.append(0)
    judge.append(li)
# x = np.array(df1)
'''
for i in range(15):
    print(judge[i])
    print(select[i])

# xn = pd.DataFrame(judge)
# xn.to_csv('D:\\Program_file\\Python-File\\20年数模校赛\\第一题.csv')



aa = []
for i in range(23):
    aa.append(1)
bb = []
for i in range(15):
    bb.append(1)

c = np.array(aa)
A_ub = np.array(judge)  # 不等式约束
b_ub = np.array(bb)
# A_eq = np.array(select)                # 等式约束
# b_eq = np.array(aa)
r = linprog(c, A_ub=-A_ub, b_ub=-b_ub, bounds=(
    (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1)))
print(r)
'''

# Create a new model
m = LpProblem(name="MIP Model", sense=LpMinimize)

# Create variables
name_list = ['x1', 'x2', 'x3', 'x4', 'x5',
             'x6', 'x7', 'x8', 'x9', 'x10', 'x11', 'x12', 'x13', 'x14', 'x15', 'x16', 'x17', 'x18', 'x19', 'x20', 'x21', 'x22', 'x23', ]
x3 = LpVariable(cat=LpBinary, name="x1")
for i in range(23):
    exec('{} = LpVariable(cat=LpBinary, name="{}")'.format(
        name_list[i], name_list[i]))
'''
x = LpVariable(cat=LpBinary, name="x")
y = LpVariable(cat=LpBinary, name="y")
z = LpVariable(cat=LpBinary, name="z")
'''

m += x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x10 + x11 + x12 + \
    x13 + x14 + x15 + x16 + x17 + x18 + x19 + x20 + x21 + x22 + x23
for i in range(15):
    li = []
    for j in range(23):
        li.append('{}*{}'.format(judge[i][j], name_list[j]))
    temp = "+".join(li)
    exec('m +='+temp+'>=1')
'''
# Add constraint: x + 2 y + 3 z <= 4
m += LpConstraint(e=(x + 2 * y + 3 * z),
                  sense=LpConstraintLE, rhs=4, name='c0')

# Add constraint: x + y >= 1
m += LpConstraint(e=(x + y), sense=LpConstraintGE, rhs=1, name='c1')

# Set objective
m.setObjective(x + y + 2 * z)
'''
# Calculate with the default CBC optimizer
status = m.solve()

if LpStatus[status] == 'Optimal':

    for v in m.variables():
        print('%s %g' % (v.name, v.varValue))

    print('Obj: %g' % m.objective.value())
