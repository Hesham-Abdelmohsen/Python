# code to demonstrate shortest route among multiple points in circular path to pass by all points


perimeter,n = map(int, input().split())
v =list(map(int, input().split()))      # values of each point away from northest point
diff = []

v.reverse()

for i in range(n-1):
    diff.append(v[i]-v[i+1])
    
diff.append(perimeter-(v[0]- v[n-1]))

print(perimeter - max(diff))

