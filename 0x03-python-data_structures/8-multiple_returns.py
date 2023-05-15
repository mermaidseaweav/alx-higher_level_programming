#!/usr/bin/python3
def nultiple_returns(sentence):
    len_sen = len(sentence)

    if (len_sen == 0):
        new_tuple = (len_sen, None)
        return new_tuple
    else:
        new_tuple = (len_sen, sentence[0:1])
    return (new_tuple)
