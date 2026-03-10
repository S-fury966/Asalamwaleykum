from models.paraphraser import tokenizer, model

def structural_variation(text):

    instruction = "Rewrite this question using a very different structure but same meaning: "

    inputs = tokenizer(instruction + text, return_tensors="pt")

    out = model.generate(**inputs, max_length=64)

    return tokenizer.decode(out[0], skip_special_tokens=True)