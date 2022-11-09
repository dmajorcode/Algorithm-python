import sys
input = sys.stdin.readline

tree={}
for _ in range(int(input())):
    root, left, right = input().split()
    tree[root] = [left, right]

# 전위순회
def pre(root):
  if root!='.':
    print(root,end="")
    pre(tree[root][0])
    pre(tree[root][1])    

    
# 중위순회
def mid(root):
  if root !='.':
    mid(tree[root][0])
    print(root, end="")
    mid(tree[root][1])

    

# 후위순회
def lat(root):
  if root !=".":
    lat(tree[root][0])
    lat(tree[root][1])
    print(root, end="")


pre('A')
print()
mid('A')
print()
lat('A')
print()
