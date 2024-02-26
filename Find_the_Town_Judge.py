'''
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

1.  The town judge trusts nobody.
2.  Everybody (except for the town judge) trusts the town judge.
3.  There is exactly one person that satisfies properties 1 and 2.

You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.
If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
'''

def get_judge_id(n, trust):
    judge_id = -1
    if len(trust) == 0 and n == 1:
        judge_id = 1
    b_a_dict = {}
    for t in trust:
        if t[1] not in b_a_dict:
            b_a_dict[t[1]] = []
        b_a_dict[t[1]].append(t[0])
        if len(b_a_dict[t[1]]) == n - 1:
            judge_id = t[1]
    for b in b_a_dict:
        if judge_id in b_a_dict[b]:
            judge_id = -1
    return judge_id
        

# n = 2
# trust = [[1,2]]
# # Output: 2

# n = 3
# trust = [[1,3],[2,3]]
# # Output: 3

# n = 3
# trust = [[1,3],[2,3],[3,1]]
# # Output: -1

# n = 4
# trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
# # Expected 3

n = 1
# n = 2
trust = []

ans = get_judge_id(n, trust)
print(ans)