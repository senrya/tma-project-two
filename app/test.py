from numpy import sqrt
from math import sqrt, erfc 
from numpy.random import rand, randn
import matplotlib.pyplot as plt
         
EbN0_dB = 2
EbN0 = 10.^(EbN0_dB/10)
BER = 1/2.*erfc(sqrt(EbN0))
