def e_formula(m:int) -> int:
    """
    E = mc^2

    E = Energy (J)\n
    m = mass (Kg)\n
    c = 300000000/s
    """
    return m*(300000000**2)

print("E:",e_formula(int(input("m: "))))