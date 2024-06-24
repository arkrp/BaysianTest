import numpy as np
random = np.random.default_rng()
def main():
    """ #  
    This test represents a scenario when both B and C are fully dependent on A. How do we obtain information about B by observing C?
    A -> B
    A -> C
    """
    # 
    #  define our connections!
    PB_A = random.uniform(0,1)
    PB_NA = random.uniform(0,1)
    PC_A = random.uniform(0,1)
    PC_NA = random.uniform(0,1)
    #  calculate our dependent connections
    PNB_A = 1 - PB_A
    PNB_NA = 1 - PB_NA
    PNC_A = 1 - PC_A
    PNC_NA = 1 - PC_NA
    # 
    # 
    #  define our priors
    PA = 0.5
    PNA = 1 - PA
    PB = PB_A * PA + PB_NA * PNA
    PNB = 1 - PB
    PC = PC_A * PA + PC_NA * PNA
    PNC = 1 - PC
    # 
    #  try three methods to find our A probability when C is observed
    #  method 1: direct baysian
    PA_B = (PB_A * PA) / (PB_A * PA + PB_NA * PNA)
    PNA_B = 1 - PA_B
    PA_NB = (PNB_A * PA) / (PNB_A * PA + PNB_NA * PNA)
    PNA_NB = 1 - PA_NB
    PC_B = PC_A * PA_B + PC_NA * PNA_B
    PC_NB = PC_A * PA_NB + PC_NA * PNA_NB
    PB_C_1 = (PC_B * PB) / (PC_B * PB + PC_NB * PNB)
    print(f'method 1: P( B|C)={PB_C_1:.9f} : direct baysian')
    #print(f'          P(~A|C)={1 - PA_C_1:.4f}')
    # 
    #  method 2: cascade
    PA_C = (PC_A * PA) / (PC_A * PA + PC_NA * PNA)
    PNA_C = 1 - PA_C
    PB_C_2 = PB_A * PA_C + PB_NA * PNA_C
    print(f'method 2: P( B|C)={PB_C_2:.9f} : cascade')
    #print(f'          P(~A|C)={PNA_C_2:.4f}')
    # 
    #  method 3: random sample
    def get_random_abc():
        A = True if PA > random.uniform(0, 1) else False
        if A == True:
            B = True if PB_A > random.uniform(0, 1) else False
            C = True if PC_A > random.uniform(0, 1) else False
        else:
            B = True if PB_NA > random.uniform(0, 1) else False
            C = True if PC_NA > random.uniform(0, 1) else False
        return (A, B, C)
    distributions =\
            list(map(np.array, zip(*[get_random_abc() for i in range(100000)])))
    A_distribution, B_distribution, C_distribution = distributions
    B_C_distribution = B_distribution[C_distribution==True]
    PA_C_3 = sum(B_C_distribution)/len(B_C_distribution)
    print(f'method 3: P( B|C)={PA_C_3:.9f} : random sample')
    #print(f'          P(~A|C)={1 - PA_C_3:.4f}')
    # 
    # 
if __name__ == '__main__':
    main()
