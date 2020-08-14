# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()
        #print('----------------')
        #print(legalMoves)
        
        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        #import time
        #time.sleep(2)
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"
        #print("选择了",legalMoves[chosenIndex])

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        #print('----------------')
        #print("行动方向",action)
        #for ghostState in newGhostStates:
        #    print(ghostState.getPosition())
            
        # 吃豆人当前的位置
        pacman_state = currentGameState.getPacmanState().getPosition()
        # 吃豆人的下一个位置
        pacman_next = newPos
        # 吃豆人在下一个位置能得到的分数
        pacman_score = successorGameState.getScore()
        # 得到食物列表 newFood.asList()

        ## 计算食物的权重，离食物越近权重越大
        # 计算曼哈顿距离 util.manhattanDistance(state1,state2)
        # 遍历食物列表，看下一个位置能到达的最近的食物是多近
        food_scores = [1/util.manhattanDistance(pacman_next, food) for food in newFood.asList()]
        # 得到在下一个位置能得到的最大分数
        bestScore = max(food_scores)
        #print(food_scores,max(food_scores))

        ##计算鬼的权重，离鬼越远权重越大
        gost_scores = [util.manhattanDistance(pacman_next, ghostState.getPosition()) for ghostState in newGhostStates]
        gostscore = sum(gost_scores)
        #print(gost_scores,sum(gost_scores))
        return successorGameState.getScore()
        #return bestScore+pacman_score*gostscore

def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        # 评价函数
        #print('深度',self.depth)
        #while self.depth != 0 :
        #    self.depth -= 1
        #print(self.evaluationFunction(gameState))
        # 得到吃豆人的移动选项
        #print(gameState.getLegalActions(0))
        # 得到按照某选项移动后的下一状态
        #state2 = gameState.generateSuccessor(0,gameState.getLegalActions(0)[0]) 
        #state3 = gameState.generateSuccessor(0,gameState.getLegalActions(0)[1]) 

        #print(state2.getLegalActions(0))
        #state3 = state2.generateSuccessor(0,state2.getLegalActions(0)[0])
        #print(self.evaluationFunction(state2))
        # 得到智能体总数量
        #print(gameState.getNumAgents())
        # 得到当前状态是什么状态
        #print(gameState.isWin())
        #print(gameState.isLose())

        ## MINIMAX函数，返回的是行为
        def MINIMAX(state):
            # 得到吃豆人的可移动action
            actions = state.getLegalActions(0)
            # 得到MAX列表
            MAX_list = [MINI(state.generateSuccessor(0,action),0,1) for action in actions ]
            # 得到最好分数的下标 
            bestLocation = MAX_list.index(max(MAX_list))
            # 返回该下标对应的行动
            return actions[bestLocation]

        ## MINI函数    
        def MINI(state,depth,depth_ghost):
            # 得到鬼的行为
            actions = state.getLegalActions(depth_ghost)
            # 如果有更多鬼，先套MINI
            if depth_ghost != state.getNumAgents()-1:
                MINI_list = [MINI(state.generateSuccessor(depth_ghost,action),depth,depth_ghost+1) for action in actions]
            # 否则套MAX
            else:
                MINI_list = [MAX(state.generateSuccessor(depth_ghost,action),depth) for action in actions]
            
            if len(MINI_list) == 0:
                return self.evaluationFunction(state)
            
            return min(MINI_list)
 
        ## MAX函数
        def MAX(state,depth):
            depth+=1
            # 到达最深的时候
            if depth >= self.depth:
                #print('终点',self.evaluationFunction(state))
                return self.evaluationFunction(state)
            
            # 得到吃豆人的行为
            actions = state.getLegalActions(0)
            MAX_list = [MINI(state.generateSuccessor(0,action),depth,1) for action in actions]
           
            if len(MAX_list) == 0:
                return self.evaluationFunction(state)
            
            return max(MAX_list)
            
        return MINIMAX(gameState)

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction
