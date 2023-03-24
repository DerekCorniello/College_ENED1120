def Springs(K1, K2, Ftot, Config):
    if K1 >= 0 or K2 >= 0:
        if Config == "Parallel":
            Keq = K1 + K2
            xtot = Ftot / Keq
            x1 = xtot
            x2 = xtot
            F1 = K1*x1
            F2 = K2*x2
            return Keq, F1, F2, x1, x2, xtot
            
        if Config == "Series":
            Keq = (K1*K2)/(K1+K2)
            F1 = Ftot
            F2 = Ftot
            xtot = Ftot/ Keq
            x1 = F1/K1
            x2 = F2/K2
            return Keq, F1, F2, x1, x2, xtot
            
        else:
            print("Invalid Input Requirements")
    else:
        print("Invalid Input Requirements")
