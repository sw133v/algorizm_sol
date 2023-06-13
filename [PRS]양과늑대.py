from collections import defaultdict

info = [0,1,0,1,1,0,1,0,0,1,0]
edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]

answer = 0

def solution(info, edges):
    
    def dfs (s, w, nodes):
        if s <= w:
            return
        else:
            global answer
            answer = max (answer, s)
            
            for next_node in nodes:
                next = graph[next_node]
                print(nodes, next)
                nodes |= next
                print(nodes)
                nodes -= set([next_node])
                
                if info[next_node]:
                    w += 1
                else:
                    s += 1
                
                dfs(s, w, nodes)
                
                nodes |= set([next_node])
                nodes -= next
                
                if info[next_node]:
                    w -= 1
                else:
                    s -= 1

    graph = defaultdict(set)
    for nod, des in edges:
        graph[nod].add(des)
    
    dfs(1, 0, graph[0])
    
    return answer

solution(info, edges)
















# answer = 0
# def solution(info, edges):

#     def dfs(s, w, nodes):
#         global answer
#         if s <= w:
#             return
#         else:
#             answer = max(answer, s)
#             for next in nodes:
#                 child = graph[next]
#                 nodes |= child
#                 nodes -= set([next])
#                 if info[next] == 0:
#                     s += 1
#                 else:
#                     w += 1
#                 dfs(s, w, nodes)
#                 # 원래대로 복원
#                 nodes |= set([next])
#                 nodes -= child
#                 if info[next] == 0:
#                     s -= 1
#                 else:
#                     w -= 1

#     graph = defaultdict(set)
#     for nod, des in edges:
#         graph[nod].add(des)

#     dfs(1, 0, graph[0])

#     return answer

print(solution(info, edges))