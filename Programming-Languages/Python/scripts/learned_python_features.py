from dataclasses import dataclass


a = 0

##
def second():
    global a
    a = 0
    for _ in range(1_000_000):
        a = 0
        
def first():
    global a
    a = 0
    for _ in range(100_000):
        a = 0
        
def third():
    global a
    a = 0
    for _ in range(10_000_000):
        a = 0
        
def matry():
    first()
    second()
    third()

def main():
    import cProfile
    import pstats
    
    with cProfile.Profile() as pr:
        # some_function()
        pass
        
    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()
    stats.dump_stats(filename="profile.prof")
    """
    if uncomment the above, use snakeviz with the .prof file
    --$ snakeviz *.prof
    """
    
if __name__ == "__main__":
    import cProfile
    import pstats
    
    with cProfile.Profile() as pr:
        main()
        pass
        
    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()
    stats.dump_stats(filename="profile.prof")
    """
    if uncomment the above, use snakeviz with the .prof file
    --$ snakeviz *.prof
    """
    main()