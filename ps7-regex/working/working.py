import re

def main():
    print(convert(input("Hours: ")))

def conv_h_m(h:int, m:int) -> list:
    if h < 10:
        h = f"0{h}"
    if m < 10:
        m = f"0{m}"

    return h,m

def conv_time(time:str, code:str) -> str:
    if ":" in time:
        h, m = time.split(":")
        m = int(m)
    else:
        h = time
        m = 0
    
    h = int(h)
    
    if code == "AM":
        if h == 12: 
            h = 0
        h, m = conv_h_m(h,m)
    else: # pm
        if h == 12:
            h = 12
        else:
            h = 12+h # 9pm = 12+9=>21pm
        h, m = conv_h_m(h,m)

    return f"{h}:{m}"

def convert(s:str) -> str:
    w_t = []

    # "12 AM to 12 PM" | "12:00 AM to 11:59 PM"
    # 12 PM: Midday | 12 AM: Midnight
    #     first format (1 to 12) | second format (00:00 to 12:00) g1| g2
    pattern = r"((?:[1-9]|1[0-2])|(?:0?[0-9]|1[0-2]):(?:[0-5][0-9])) (AM|PM)"

    if match := re.search(r"^" + pattern + " to " + pattern + r"$", s, flags=re.IGNORECASE):
        for i in range(1,5):
            w_t.append(match.group(i).upper())
    else:
        raise ValueError("Invalid Format::expected => [(0-12) | (00:00-12:00)] (AM|PM) [to] ... :D")

    left_t = w_t[0]
    left_code = w_t[1]
    right_t = w_t[2]
    right_code = w_t[3]
    
    res_left = conv_time(left_t, left_code) 
    res_right = conv_time(right_t, right_code) 

    return f"{res_left} to {res_right}"

if __name__ == "__main__":
    main()