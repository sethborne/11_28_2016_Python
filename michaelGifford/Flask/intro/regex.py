import re

def get_matching_words(regex):
    words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]

    return [word for word in words if re.search(regex, word)]




# All words that contain a “v”
# print(get_matching_words(r'v'))
# # All words that contain a double-“s”
# print(get_matching_words(r'ss'))
# # All words that end with an “e”
# print(get_matching_words(r'e$'))
# # All words that contain an “b”, any character, then another “b”
# print(get_matching_words(r'b\wb'))
# # All words that contain an “b”, at least one character, then another “b”
# print(get_matching_words(r'b\w+b'))
# # All words that contain an “b”, any number of characters (includign zero), then another “b”
# print(get_matching_words(r'b[a-z,A-Z,0]+b'))
# # All words that include all five vowels in order
# print(get_matching_words(r'a\w*e\w*i\w*o\w*u\w*'))
# # All words that only use the letters in “regular expression” (each letter can appear any number of times)
print(get_matching_words(r'^[regularexpression]+$'))
# All words that contain a double letter
print(get_matching_words(r'(\w)\1'))
