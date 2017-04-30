
def gettingNegativeWords(verbose=1):
    try:
        file = open("NEGATIVE_opinion_words")
        # lines = file.readlines()
        lines = file.read().splitlines()
        NEGATIVE_opinion_words = set(lines)
        # containsNegatie = NEGATIVE_opinion_words & text_set
        if verbose:
            print lines
            print len(NEGATIVE_opinion_words)
            # print containsNegatie
            print NEGATIVE_opinion_words
            # print text_set
            # if
            #     # return True
            # print type(lines)
        return NEGATIVE_opinion_words

    finally:
        file.close()