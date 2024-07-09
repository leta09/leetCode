class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        w = 0
        waiting = []
        chef_finish = 0
        for i in range(len(customers)):
                if customers[i][0] >= chef_finish:
                        chef_finish = sum(customers[i])
                        w = chef_finish - customers[i][0]
                        waiting.append(w)
                elif customers[i][0] < chef_finish:
                        chef_finish = chef_finish + customers[i][1]
                        w = chef_finish - customers[i][0]
                        waiting.append(w)
        return sum(waiting)/len(customers)