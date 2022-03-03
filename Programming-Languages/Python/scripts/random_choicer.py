def choicer(path, itype="png", sample_size=3):
    from glob import glob
    import random
    dict_samples = {}
    
    
    path = path + "/"if path[-1] != "/" else path
    main_dirs = glob(path + "*[!A-z.]")

    
    for main_dir in main_dirs:
        main_dir = main_dir + "/" if main_dir[-1] != "/" else main_dir
        sub_dirs = glob(f"{main_dir}*.{itype}")
        _key = main_dir[:-1].split("/")[-1]
        print(_key)
        dict_samples[_key] = random.sample(sub_dirs, k=sample_size)
        
    return dict_samples.items() 
