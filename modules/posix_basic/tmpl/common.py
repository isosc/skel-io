def to_fp_name(path, prefix='fp'):

    if path == 'stdout':
        return 'stdout'
    if path == 'stderr':
        return 'stderr'
    if path == 'stdin':
        return 'stdin'

    # For now, just construct a fd variable name by taking objectionable chars out of the path
    cleaned = path.replace('.', '_').replace ('/', '_').replace ('-', '_').replace ('+', 'x')
    return "{}_{}".format(prefix, cleaned) 

def doinatest():
    return "YO"

