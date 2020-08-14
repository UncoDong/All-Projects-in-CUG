# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    print(problem.walls[0][0]) # 判断是否能走路
    print(problem.goal) # 得到目标
    print(problem.getStartState())
    from game import Directions
    s = Directions.SOUTH  # 下
    w = Directions.WEST   # 左
    n = Directions.NORTH  # 上
    e = Directions.EAST   # 右
    """
    "*** YOUR CODE HERE ***"
    import util
    vis = util.Counter()       # 已经走过的地方
    # 起始点已经走过了
    vis[problem.getStartState()]+=1
    
    answer_queue = util.Stack()# 结果队列
    dfs_stack = util.Stack()   # dfs遍历栈
    for each in problem.getSuccessors(problem.getStartState()):
        dfs_stack.push(each)


    # DFS循环 栈不为空
    while dfs_stack.isEmpty() == False:
        # 位置 方向 还有一个不知道是啥的
        state,direction,_ = dfs_stack.pop()
        vis[state]+=1
        if vis[state] == 1:
            dfs_stack.push((state,direction,_))
        # print("添加",state,direction,_ )

        # 添加路径
        if vis[state] <= 1:
            answer_queue.push(direction)
        else:
            answer_queue.pop()
        
        # 如果到了终点
        if problem.isGoalState(state):
            # print(answer_queue.list)
            return answer_queue.list
        
        # 扩展节点
        append_point = problem.getSuccessors(state)
        for each in append_point:
            state,_,__ = each
            # 如果这个点没有走过
            if vis[state] == 0:
                dfs_stack.push(each)
                #print("扩展",each)
                # cal+=1
        
            

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    import util
    vis = util.Counter()       # 已经走过的地方
    # 起始点已经走过了
    vis[problem.getStartState()]+=1
    
    answer_queue = util.Queue()# 结果队列
    bfs_stack = util.Queue()   # bfs遍历栈
    
    father = {}     # 父节点字典
    # my_dection = {} # 方向字典
    for each in problem.getSuccessors(problem.getStartState()):
        bfs_stack.push(each)
        father[each[0]] = problem.getStartState()
        # my_dection[each[0]] = each[1]
    
    # BFS循环 栈不为空
    while bfs_stack.isEmpty() == False:
        # 位置 方向 还有一个不知道是啥的
        state_father,direction_father,_ = bfs_stack.pop()
        vis[state_father]+=1
        # 如果到了终点
        if problem.isGoalState(state_father):
            while state_father != problem.getStartState():
                state = father[state_father]
                for each in problem.getSuccessors(state):
                    state2,direction2,__ = each
                    if state_father == state2:
                       answer_queue.push(direction2)
                state_father = state
            del bfs_stack
            return answer_queue.list
                
        # 扩展节点
        append_point = problem.getSuccessors(state_father)
        for each in append_point:
            state2,direction2,__ = each
            try:
                father[state2]
            except:
                father[state2] = state_father
            # print("填入",state2,direction_father)
            # 如果这个点没有走过
            if vis[state2] == 0:
                bfs_stack.push(each)
                # print("扩展",each)

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
