alphabet = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
nums = ('0','1','2','3','4','5','6','7','8','9')

def is_valid(s:str) -> bool:
    s=s.upper()
    mix = alphabet + nums
    s_len = len(s)
    
    if s_len > 6 or s_len < 2:
        return False

    f = 0
    for i in range(s_len):
        if s[i] not in mix:
            return False
        
        if i < 2 and s[i] in nums:
            return False
        
        if i >= 2:
            if s[i] in nums and s[i] == '0' and f==0:
                return False
            elif s[i] in nums:
                f += 1

        if f > 0 and s[i] in alphabet:
            return False

    return True

def main():
    print("Valid") if is_valid(input("Plate: ")) else print("Invalid")

if __name__ == "__main__":
    main()