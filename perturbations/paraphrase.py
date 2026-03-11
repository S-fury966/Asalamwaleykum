def paraphrase(prompt):

    prompts = [

        prompt,

        "Explain " + prompt,

        "Describe " + prompt,

        "Give an explanation of " + prompt,

        "What is " + prompt + "?"

    ]

    return prompts