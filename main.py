from models.llm_interface import get_response
from perturbations.paraphrase import generate_paraphrase
from perturbations.emotional import emotional_variations
from perturbations.structural import structural_variation
from perturbations.logical_flip import logical_flip

from analysis.stability_analyzer import stability_score
from visualization.heatmap import plot_heatmap


def run_test(prompt):

    prompts = [prompt]

    prompts.extend(generate_paraphrase(prompt))

    prompts.extend(emotional_variations(prompt))

    prompts.append(structural_variation(prompt))

    prompts.append(logical_flip(prompt))

    responses = []

    for p in prompts:

        print("\nPrompt:", p)

        response = get_response(p)

        print("Response:", response)

        responses.append(response)

    scores = stability_score(responses)

    labels = [

        "Paraphrase1",
        "Paraphrase2",
        "Paraphrase3",
        "Aggressive",
        "Worried",
        "Skeptical",
        "Structural",
        "Logical Flip"

    ]

    plot_heatmap(scores, labels)

    print("\nAverage Stability:", sum(scores)/len(scores))


prompt = "Can cryptocurrencies NOT be trusted for financial transactions?"

run_test(prompt)