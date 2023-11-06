#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence) if sentence else 0
    return length, sentence[:1] if sentence else None
