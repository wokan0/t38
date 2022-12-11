# importing spacy and loading the model
import spacy

nlp = spacy.load('en_core_web_md')

# Description of "Planet Hulk" and its nlp model
desc_to_compare = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar whare he is sold into slavery and trained as a gladiator."
model_desc = nlp(desc_to_compare)

# Dict to store similarities to model_desc
similarity_dict = {}

# opening file and calculating similarities
with open('movies.txt', 'r') as f:
    for line in f:
        title = line[:8]
        desc = line[9:]
        similarity_dict[title] = nlp(desc).similarity(model_desc)

# Finding maximum similarity and suggesting the movie
print("After watching 'Planet Hulk' the user should watch {}".format(
    max(similarity_dict, key=similarity_dict.get)))
