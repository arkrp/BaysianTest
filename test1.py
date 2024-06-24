import numpy as np
random = np.random.default_rng()
def main():
    #  define our connections!
    PB_A = random.uniform(0,1)
    PB_NA = random.uniform(0,1)
    PC_B = random.uniform(0,1)
    PC_NB = random.uniform(0,1)
    #  calculate our dependent connections
    PNB_A = 1 - PB_A
    PNB_NA = 1 - PB_NA
    PNC_B = 1 - PC_B
    PNC_NB = 1 - PC_NB
    # 
    # 
    #  define our priors
    PA = 0.5
    PNA = 1 - PA
    PB = PB_A * PA + PB_NA * PNA
    PNB = 1 - PB
    # 
    #  try three methods to find our A probability when C is observed
    #  method 1: direct baysian
    PC_A = PC_B * PB_A + PC_NB * PNB_A
    PC_NA = PC_B * PB_NA + PC_NB * PNB_NA
    PA_C_1 = (PC_A * PA) / (PC_A * PA + PC_NA * PNA)
    print(f'method 1: P( A|C)={PA_C_1:.9f} : direct baysian')
    #print(f'          P(~A|C)={1 - PA_C_1:.4f}')
    # 
    #  method 2: cascade
    PB_C = (PC_B * PB) / (PC_B * PB + PC_NB * PNB)
    PNB_C = 1 - PB_C
    PA_B = (PB_A * PA) / (PB_A * PA + PB_NA * PNA)
    PNA_B = (PB_NA * PNA) / (PB_NA * PNA + PB_A * PA)
    # fun fact, on the line directly below, I typoed a + instead of a *. Took me 2 hours to find the error.
    PA_NB = (PNB_A * PA) / (PNB_A * PA + PNB_NA * PNA)
    PNA_NB = (PNB_NA * PNA) / (PNB_NA * PNA + PNB_A * PA)
    # print(f'{PB_C=:.3f}\n{PNB_C=:.3f}\n{PA_B=:.3f}\n{PNA_B=:.3f}\n{PA_NB=:.3f}\n{PNA_NB=:.3f}\n')
    PA_C_2 = PA_B * PB_C + PA_NB * PNB_C
    PNA_C_2 = PNA_B * PB_C + PNA_NB * PNB_C
    print(f'method 2: P( A|C)={PA_C_2:.9f} : cascade')
    #print(f'          P(~A|C)={PNA_C_2:.4f}')
    # 
    #  method 3: random sample
    def get_random_abc():
        A = True if PA > random.uniform(0, 1) else False
        if A == True:
            B = True if PB_A > random.uniform(0, 1) else False
        else:
            B = True if PB_NA > random.uniform(0, 1) else False
        if B == True:
            C = True if PC_B > random.uniform(0, 1) else False
        else:
            C = True if PC_NB > random.uniform(0, 1) else False
        return (A, B, C)
    distributions =\
            list(map(np.array, zip(*[get_random_abc() for i in range(100000)])))
    A_distribution, B_distribution, C_distribution = distributions
    #print(f'{A_distribution}')
    #print(f'{C_distribution}')
    A_distribution = A_distribution[C_distribution==True]
    PA_C_3 = sum(A_distribution)/len(A_distribution)
    print(f'method 3: P( A|C)={PA_C_3:.9f} : random sample')
    #print(f'          P(~A|C)={1 - PA_C_3:.4f}')
    # 
    # 
if __name__ == '__main__':
    main()
