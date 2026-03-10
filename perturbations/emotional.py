from models.paraphraser import tokenizer, model

def emotional_variations(text):

    prompts = [

        "Rewrite this question in an aggressive tone: ",
        "Rewrite this question in a worried tone: ",
        "Rewrite this question in a skeptical tone: "

    ]

    outputs = []

    for p in prompts:

        inputs = tokenizer(p + text, return_tensors="pt")

        out = model.generate(**inputs, max_length=64)

        sentence = tokenizer.decode(out[0], skip_special_tokens=True)

        outputs.append(sentence)

    return outputs