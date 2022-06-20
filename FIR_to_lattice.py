import numpy as np

def fir_to_lattice(fir):  
    length = len(fir)
    lattice = np.zeros(length-1)

    for i in range(0,length-1):

        lattice[-i-1] = fir[-1]                         # Latest element of k = last element of A
        img = np.flip(fir)                              # Make image polynomial
        fir = (1/(1-((lattice[-i-1])**2)))*(fir - lattice[-i-1]*img)    # Apply the recursive lattice equation
        fir = np.delete(fir,len(fir)-1)                   # Trim zero element at end of new array
    
    return lattice


z = []  #enter normalized (highest order coefficient must be 1) FIR filter coefficients here 
k = fir_to_lattice(z)
print(k)