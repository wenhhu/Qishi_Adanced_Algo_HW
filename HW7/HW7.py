class Tree: 
    def __init__(self, root): 
        self.root = root 
        
    def insert(self, node): 
        curr = self.root 
        cnt = 0
        while curr != None: 
            prev = curr 
            if node.val > curr.val: 
                cnt += (curr.eleCount+curr.lcount) 
                curr = curr.right 
            elif node.val < curr.val: 
                curr.lcount += 1
                curr = curr.left 
            else: 
                prev = curr 
                prev.eleCount += 1
                break
        if prev.val > node.val: 
            prev.left = node 
        elif prev.val < node.val: 
            prev.right = node 
        else: 
            return cnt+prev.lcount 
        return cnt

class Node: 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None
        self.eleCount = 1
        self.lcount = 0
    
class Solution:
    def constructArray(self, arr): 
        if len(arr) == 0:
            return []
        n = len(arr)
        t = Tree(Node(arr[-1])) 
        ans = [0] 
        for i in range(n-2,-1,-1): 
            ans.append(t.insert(Node(arr[i]))) 
        return reversed(ans)
    
    def countSmaller(self, nums: List[int]) -> List[int]:
        return self.constructArray(nums)