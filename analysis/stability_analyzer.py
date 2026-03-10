from sentence_transformers import util
from models.similarity_model import model

def stability_score(responses):

    base = responses[0]

    base_emb = model.encode(base)

    scores = []

    for r in responses[1:]:

        emb = model.encode(r)

        score = util.cos_sim(base_emb, emb)

        scores.append(float(score))

    return scores