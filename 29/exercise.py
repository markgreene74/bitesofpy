def get_index_different_char(chars):
    alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    d_alpha = {}
    d_non_alpha = {}
    # sort alpha from non alpha
    for x in chars:
        if x and str(x) in alpha:
            d_alpha[x] = chars.index(x)
        else:
            d_non_alpha[x] = chars.index(x)
    # find the odd one
    if len(d_alpha) == 1:
        return list(d_alpha.values())[0]
    else:
        return list(d_non_alpha.values())[0]