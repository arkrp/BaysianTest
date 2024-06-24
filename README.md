# BaysianTest

Author: Hannah Nelson
Date: June 23, 2024

This repository contains several tests which numerically verify that cascading baysian probabilities according to the prior conditional probabilities matches up to reality.

The operation of cascading probabilities through baysian can be viewed as splitting possibility space into multiple parts, finding out about each of those parts by cutting off possibilities, and adding those parts back together in a weighted way!

Cascading baysian updates is essential for performing statistical inference on any complex system.

## test1.py

Test 1 serves as a simple test that propagating baysian updates backwards performs as expected. It compares: explicit baysian, cascading baysian, and empirical random sample.

Structure A -> B -> C

Procedure:
    Propagate Prior from A
    Observe C as true.
    Measure the posterior probability of A.

Results: Test Passed

This indicates that we can safely propagate baysian updates backwards!

## test2.py

Test 2 serves as a mode advanced test that baysean probability updates may also be propagated forwards! This is more difficult to wrap one's head around explicitly. It compares, cascading baysean and empirical random sample.

Structure: A -> B + A -> C

Procedure: 
    Propagate prior from A
    Observe C as true.
    Measure the posterior probability of B.

Results: Test Passed

This indicates we can safely propagate baysian updates both forwards and backwards!

## test3.py WIP

Test 3 serves as a mirror of test 2 on a more general framework. Test 3 works with catagorical distributions rather than true false probabilities. The priors are now catagorical vectors, the conditional probabilities are now markov matricies. This model should allow for simple generalization of more difficult discreet probability problems!

Structure A -> B + A -> C

A has two states A_1 and A_2
B has three states B_1, B_2, and B_3
C has three states C_1 and C_2, C_3

Procedure:
    Propagate prior from A
    observe C as state C_2
    measure posterior distrubuton of B

## test4.py WIP

Test 4 serves as a basic test of the capability of the system to act rationally under observations which fundementally alter the conditional distributions via their operation. This test demonstrates the neccessity of updating the conditional probabilities.

Structure A -> B -> C + A -> D

A has two states A_1 and A_2
B has three states B_1, B_2, and B_3
C has three states C_1 and C_2, C_3
D has two states D_1 and D_2

Procedure:
    Propagate prior from A
    observe C as state C_2
    observe D as state D_2
    measure posterior distrubuton of B
