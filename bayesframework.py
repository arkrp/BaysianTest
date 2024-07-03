""" #  
Bayes Framework

This module is allows simple Bayesian modeling of conditionally connected catagorical distributions. It models a causal chain of random variables which are related by markov/emission matricies. This can be used for things which are not markov chains!

To utilize this library follow the following procedure:
    create a initial node,
    create the connections to that node via Node.add_connection()
    initialize the prior of the root node with Node.initialize_prior
    record observations using Node.observe
    retrieve desired distributions from desired node using Node.distribution
    
Notes: initialize_prior is only intended to be used on the root node, all other nodes will automatically initialize when needed based on the prior given to the root, or updates made.
"""
# 
import numpy as np
from dataclasses import dataclass, field
@dataclass
class Node(): #  
    #  attributes!
    __distribution: np.array = field(init=False)
    cause: 'Node' = field(default=None)
    cause_joint: 'Joint' = field(default=None)
    effect: list['Node'] = field(init=False, default_factory=list)
    effect_joint: list['Joint'] = field(init=False, default_factory=list)
    observed: bool = field(init=False, default=False)
    # 
    def add_connection(self, *, relation: np.array, relation_type ='emission') -> 'Node': #  
        """ #  
        Creates a new branch off from the existing causal tree.

        Returns the created node.

        relation: np.array
            - if relation type is \'emission\' this is an emission matrix which specified the relation between cause node and effect node
        relation_type
            \'emission\' - 
            \'joint\' - 
        """
        # 
        joint = None
        if relation_type='emission': #  
            joint = Joint(relation)
        # 
        elif relation_type='joint': #  
            joint = relation
        # 
        else: #  
            raise ValueError('Arguement \'relation_type\' provided with invalid input {}'.format(relation))
        # 
        new_node = Node(cause=self, cause_joint=Joint(emission_matrix))
        effect.append(new_node)
        pass #TODO
    # 
    def initialize_prior(self, prior: np.array): #  
        self.__distribution = prior
    # 
    @property #  
    def distribution(self):
        if self.__distribution == None:
            self.__distribution = cause[1]. @ cause[0]
        return self.__distribution
    # 
    def observe(self, distribution: np.array): #  
        pass #TODO
    # 
    @property #  
    def dim(self):
        return dim(distribution)
    # 
# 
class Joint(): #  
    """ #  
    This class represents a connection between two prior nodes. It represents the joint ditribution.

    for purposes of organization I am declaring cause the top and effect the side. Eg: the cause prior is the sum accross the columns, the effect prior is sum across the rows.

    emission matrix indicates an emmision matrix or a markov matrix, since all markov matricies are emisrion matricies
    """
    # 
    #  attributes
    cause_prior: np.array
    effect_prior: np.array
    emission_matrix: np.array
    joint_distribution: np.array
    # 
    def __init__(self, *, relation=None, relation_type='emission'): #  
        #  verify relation type!
        if relation_type='emission': #  
            joint = Joint(relation)
        # 
        elif relation_type='joint': #  
            joint = relation
        # 
        else: #  
            raise ValueError('Arguement \'relation_type\' provided with invalid input {}'.format(relation))
        # 
        # 
        """ #  
        Constructor for Joint class

        relation
            - if relation_type is \'emission\' then relation is the emission matrix which relates the cause to the effect
            - if relation type is \'joint\' then relation is the joint distribution between the cause and effect
        """
        # 
        #  initialize values
        self.cause_prior = None
        self.effect_prior = None
        self.emission_matrix = emission_matrix
        self.joint_distribution = joint_distribution
        # 
        #  if we are given a joint distribution initialize the priors at this time!
        if joint_distribution != None:
            pass #TODO
        # 
    # 
    def update_cause(self, new_cause_distribution: np.array): #  
        #  if the new cause prior matches the old one don't bother updating
        if np.all(new_cause_distribution==self.cause_prior):
            return effect_prior
        # 
        #  initialize the joint distribution if needed
        if self.joint_distribution == None:
            pass #TODO
        # 
        #TODO
    # 
    def update_effect(self, new_effect_distribution: np.array): #  
        if self.joint_distribution == None:
            raise RuntimeError('Upwards Bayesian propagation requested before joint distribution could be established')
        #TODO
    # 
# 
