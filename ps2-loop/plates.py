def main():
    print("Valid") if is_valid(input("Plate: ")) else print("Invalid")

def is_valid(s:str) -> bool:
    s=s.upper()
    alphabet = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
    nums = ('0','1','2','3','4','5','6','7','8','9')
    mix = alphabet + nums
    s_len = len(s)
    
    # MAX 6 MIN 2
    if s_len > 6 or s_len < 2:
        print("Length")
        return False

    f = 0
    for i in range(s_len):
        # Check any symbols 
        if s[i] not in mix:
            return False
        
        # First 2 char cannot be num
        if i < 2 and s[i] in nums:
            print("First two num")
            return False
        
        if i >= 2:
            # First num cannot be 0
            if s[i] in nums and s[i] == '0' and f==0:
                print("first num 0")
                return False
            elif s[i] in nums:
                f += 1

        # Cannot have numbers in the middle of plate num
        if f > 0 and s[i] in alphabet:
            print("Num in mid")
            return False

    return True

main()