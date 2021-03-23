""" module with all_prefixes function """


def all_prefixes(line: str):
    """ return set of ol sub-lines of given which starts with first char of
    given line """
    if not isinstance(line, str):
        raise TypeError('wrong type of line! it should be str!!')
    first_char = line[0]
    len_line = len(line)
    # vals = []
    vals = set()
    for i, char in enumerate(line):
        if char == first_char:
            for j in range(i+1, len_line+1):
                # vals.append(line[i:j])
                vals.add(line[i:j])
    return vals
