# BaysianTest

Author: Hannah Nelson
Date: June 23, 2024

This repository contains several tests which numerically verify that cascading baysian probabilities according to the prior conditional probabilities matches up to reality.

The operation of cascading probabilities through baysian can be viewed as splitting possibility space into multiple parts, finding out about each of those parts by cutting off possibilities, and adding those parts back together in a weighted way!

Cascading baysian updates is essential for performing statistical inference on any complex system.

## test1.py

Test 1 serves as a simple test that propagating baysian updates backwards performs as expected. It compares: explicit baysian, cascading baysian, and empirical random sample.

Results: Test Passed

This indicates that we can safely propagate baysian updates backwards!

## test2.py

Test 2 serves as a mode advanced test that baysean probability updates may also be propagated forwards! This is more difficult to wrap one's head around explicitly. It compares, cascading baysean and empirical random sample.

Results: Test Passed

This indicates we can safely propagate baysian updates both forwards and backwards!
