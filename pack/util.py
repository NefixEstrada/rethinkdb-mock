
def curry2(func):
    def out(x, *args):
        if len(args):
            return func(x, args[0])
        def out2(y):
            return func(x, y)
        return out2
    return out

def curry3(func):
    def out(x, *args):
        if len(args) == 2:
            return func(x, *args)
        def out2(y, *args):
            if len(args):
                return func(x, y, args[0])
            def out3(z):
                return func(x, y, z)
            return out3
        return out2
    return out

def extend(*dicts):
    out = {}
    for one_dict in dicts:
        out.update(one_dict)
    return out

@curry2
def extend_with(a_dict, to_extend):
    return extend(to_extend, a_dict)

@curry2
def map_with(fn, a_list):
    return map(fn, a_list)

@curry2
def maybe_map_with(fn, thing):
    if isinstance(thing, list):
        return map(fn, thing)
    return fn(thing)

def is_simple(x):
    return not (isinstance(x, (list, dict)))

@curry2
def nth(n, things):
    return things[n]

@curry2
def getter(key, thing):
    if isinstance(thing, dict):
        return thing.get(key, None)
    else:
        return getattr(thing, key, None)

@curry3
def match_attr(key, val, thing):
    return getter(key, thing) == val

@curry2
def match_attrs(to_match, to_test):
    match = True
    for k, v in to_match.iteritems():
        if getter(k)(to_test) != v:
            match = False
            break
    return match

@curry2
def filter_with(func, things):
    return filter(func, things)

@curry2
def find_first(pred, things):
    result = None
    for thing in things:
        if pred(thing):
            result = thing
            break
    return result

def pipeline(*funcs):
    def out(x):
        result = x
        for f in funcs:
            result = f(result)
        return result
    return out

def pluck_with(*attrs):
    def inner_pluck(thing):
        return {k: v for k,v in thing.iteritems() if k in attrs}
    return inner_pluck

def get_by_id(id):
    return find_first(match_attr('id', id))

def as_obj(pairs):
    return {p[0]: p[1] for p in pairs}

def clone_array(x):
    return [elem for elem in x]

@curry2
def without(bad_attrs, thing):
    return {k: v for k, v in thing.iteritems() if k not in bad_attrs}

def obj_clone(a_dict):
    return {k: v for k, v in a_dict.iteritems()}
