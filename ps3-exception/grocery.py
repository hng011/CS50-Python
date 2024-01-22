def grocery_lists() -> any:
    l_g = {}
    try:
        while True:
            inp = input().upper()
            if(inp in l_g.keys()):
                l_g[inp] += 1
            else:
                l_g.__setitem__(inp,1)
    except EOFError:
        return 0
    except Exception as e:
        print(e)
    finally:
        for k, v in sorted(l_g.items()):
            print(f"{v} {k}")
    
grocery_lists()