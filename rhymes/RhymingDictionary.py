import itertools


# return a list of words that rhyme with the input word
def find_rhymes(filename, word):
    return_list = list()
    word_sounds_list = get_sounds(filename, word.upper())
    with open(filename, encoding="ISO-8859-1", errors='ignore') as f: # 'ISO-8859-1'
        for line in itertools.islice(f, 56, None):
            if is_rhyme_sound(word_sounds_list, line.split("  ")[1].split()):
                return_list.append(line.split("  ")[0])
    return return_list


# return true if words rhyme, false otherwise
def is_rhyme_sound(sound_list1, sound_list2):
    bool_is_rhyme = False
    for (sound1, sound2) in zip(reversed(sound_list1), reversed(sound_list2)):
        if ''.join(i for i in sound1 if not i.isdigit()) == ''.join(i for i in sound2 if not i.isdigit()):
            if len(sound1) == 3:
                bool_is_rhyme = True
        else:
            break
    return bool_is_rhyme


# return a list of strings that are the sound of that word
def get_sounds(filename, word):
    sound_list = []
    with open(filename, encoding="ISO-8859-1", errors='ignore') as f:  # 'ISO-8859-1'
        for line in itertools.islice(f, 56, None):
            if line.split("  ")[0] == word.upper():
                for sound in line.split("  ")[1].split():
                    sound_list.append(sound)
    return sound_list


# return true if words rhyme, false otherwise
# return false if either word is not in dictionary
def is_rhyme(filename, word1, word2):
    return is_rhyme_sound(get_sounds(filename, word1), get_sounds(filename, word2))


print(find_rhymes("../data/cmudict-0.7b", "PARty"))
