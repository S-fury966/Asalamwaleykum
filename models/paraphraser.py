from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "google/flan-t5-base"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def generate_paraphrase(text):

    prompt = "paraphrase: " + text

    inputs = tokenizer(prompt, return_tensors="pt")

    outputs = model.generate(
        **inputs,
        max_length=64,
        num_beams=5,
        num_return_sequences=3
    )

    paraphrases = []

    for o in outputs:

        sentence = tokenizer.decode(o, skip_special_tokens=True)

        paraphrases.append(sentence)

    return paraphrases