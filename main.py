from typing import List


class Solution:

  def countComponents(self, n: int, edges: List[List[int]]) -> int:
    # How to solve it: we construct a disjoint-set.  While constructing it, we maintain a
    # count of the number of sets.  We can do this by starting with n (since each node starts
    # in its own set) and then decrementing by 1 each time we successfully perform a union.

    # Each node starts as its own parent.
    parents = {i: i for i in range(n)}
    ranks = [0 for i in range(n)]
    res = n

    def find(i):
      while parents[i] != i:
        parents[i] = parents[parents[i]]
        i = parents[i]
      return i

    def union(a, b):
      pa = find(a)
      pb = find(b)
      if pa == pb:
        return False
      
      if ranks[pa] > ranks[pb]:
        parents[pb] = pa
        ranks[pa] = ranks[pa] + ranks[pb]
      else:
        parents[pa] = pb
        ranks[pb] = ranks[pa] + ranks[pb]

      return True

    for a, b in edges:
      if union(a, b):
        res -= 1
    
    return res


if __name__ == '__main__':
  from test_runner import run_tests
  run_tests()
