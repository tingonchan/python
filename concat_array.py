a = np.array([]).reshape(0,2)


for i in range(0,11,1):
    a = np.vstack((a,np.array([i, i**2])))
    
print a

print a.shape

#------------------------------------------------------
# or the following
#------------------------------------------------------


a = np.array([])

x = 1
y = 2
z = 3

b = np.array([x, y, z])

#first, a horz cat with b
a = np.hstack((a, b))

for i in range(0,10)
    a = np.vstack((a, b))  # vertical concat
    
