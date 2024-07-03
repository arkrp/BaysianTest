""" #  
Bayes Framework

This module is allows simple Bayesian modeling of conditionally connected catagorical distributions. It models a causal chain of random variables which are related by markov/emission matricies. This can be used for things which are not markov chains!

To utilize this library to find conditional probability follow the following procedure:
    create an initial root node via the constructor
    create the connections to that node via Node.add_connection()
    mark down observations for known nodes using Node.observe()
    initialize the prior of the root node with Node.solve_probabilities(<prior of the root node>)
    retrieve desired distributions from desired node using the Node.distribution attribute
    
Notes: initialize_prior is only intended to be used on the root node, all other nodes will automatically initialize when needed based on the prior given to the root, or updates made.

"""
#TODO implement viturbi's algorithm so we can also find the most likely hidden states.
# 
import numpy as np
from dataclasses import dataclass, field
@dataclass
class Node(): #  
    #  attributes!
    effects: list['Effect'] = field(init=False, default_factory=list)
    distribution: np.array = field(init=False, default=None)
    observation: int = field(init=False, default=None)
    number_of_catagories = field(kw_only=True, default=None)
    # 
    def add_connection(self, emission_matrix: np.array) -> 'Node': #  
        """ #  
        Creates a new branch off from the existing causal tree. Returns the created node.

        emission_matrix: np.array
            - the emission matrix which relates the cause to the effect
        """
        # 
        #  validate emission matrix
        if emission_matrix.ndim != 2:
            raise ValueError('Emission matricies must have a dimensionality of 2')
        # 
        #   deal with number of catagories not being set
        if self.number_of_catagories == None:
            self.number_of_catagories = emission_matrix.shape[1]
        # 
        #  deal with number of catagories not matching up
        if self.number_of_catagories != emission_matrix.shape[1]:
            raise ValueError('Emission matrix is of incompatible size. Emission matrix has input size of {} but node has {} catagories'.format(emission_matrix.shape[1], self.number of catagories))
        # 
        #  create the connection
        new_node = Node(number_of_catagories=emission_matrix.shape[0])
        effects.append(Effect(new_node, emission_matrix, None))
        # 
        #  return the new node
        return new_node
        # 
    # 
    def solve_probabilities(self, prior: np.array) #  
        """ #  
        Finds the conditional probability of every state of every node given the observations
        """
        # 
        #  propagate the probability in two swoops!
        self.distribution = prior
        self.__bayes_propagate_up()
        self.__bayes_propagate_down()
        # 
    # 
    def __bayes_propagate_up(self): #  
        """
        Propagates probability such that every causal node has the correct probability for all nodes which are its effects
        """
        for effect in effects:
            effect.joint_matrix = effect.emission_matrix * self.distribution[None,:]
            initial_effect_distribution = np.sum(effect.joint_matrix, axis=1)
            effect.node.distribution = initial_effect_distribution
            effect.node.__bayes_propagate_up()
            effect.joint_matrix = effect.joint_matrix *\
                    (effect.node.distribution/initial_effect_distribution)[:,None]
            self.distribution = np.sum(effect.joint_distribution, axis=0)
    # 
    def __bayes_propagate_down(self): #  
        """
        propagates probability such that every node's probability becomes consistent with the changes which may have occured above it due to other branches!
        """
        for effect in effects: 
            joint_cause_distribution = np.sum(effect.joint_matrix, axis=0)
            effect.joint_matrix = effect.joint_matrix *\
                    (self.distribution/joint_cause_distribution)[None,:]
            effect.node.distribution = np.sum(effect.joint_matrix, axis=1)
            effect.node.__bayes_propagate_down()
    # 
    def observe(self, observation: int): #  
        """
        mark down an observed outcome for a particular 
        """
        self.observation = observation
    # 
    def clear_observations(self): #  
        """
        Clears all observations. This is usefull when you want to find the result for something with the same causal layout but different emission probabilities
        """
        self.observation = None
        for node in effect_node:
            effect_node.clear_observations
    # 
# 
@dataclass #  
class Effect():
    node: 'Node'
    emission_matrix: np.array
    joint_matrix: np.array
# 
