def solution(id_list, report, k):
    #print(id_list, report)
    if len(id_list) < k:
        res = [0 for _ in range(len(id_list))]
        #print(res)
        return res
    
    id_set = {}
    for id in id_list:
        id_set[id] = []
    
    mail = []
    for id in id_list:
        mail += [[id, 0]]
    
    #print(mail)
    
    for data in report:
        shingohanID, badID = data.split()
        #print(shingohanID, badID)
        #print((id_set[badID]))
        if not(shingohanID in id_set[badID]):
            id_set[badID] = id_set[badID] + [shingohanID]
    
    #print(id_set)
    for i in id_set:
        #print(id_set[i])
        if len(id_set[i]) >= k:
            for i in id_set[i]:
                for id in mail:
                    if id[0] == i:
                        id[1] += 1
                        continue
    
    #print(mail)
    res = [i[1] for i in mail]
    #print(res)
    return res