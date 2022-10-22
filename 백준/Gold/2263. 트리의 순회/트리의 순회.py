import sys
sys.setrecursionlimit(10 ** 9)

def daq(in_start, in_end, post_start, post_end):
	if (in_start > in_end) or (post_start > post_end):
		return

	root = postorder[post_end]
	size = pos[root] - in_start
	preorder.append(root)

	daq(in_start, pos[root] - 1, post_start, post_start + size - 1)
	daq(pos[root] + 1, in_end, post_start + size, post_end - 1)

n = int(input())
inorder = [-1] + list(map(int, input().split()))
postorder = [-1] + list(map(int, input().split()))

pos = [-1 for _ in range(n + 1)]
for i in range(n + 1):
	pos[inorder[i]] = i
    
preorder = []
daq(1, n, 1, n)
print(*preorder)