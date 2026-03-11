from models.llm_interface import LLMInterface
from models.similarity_model import SimilarityModel

from perturbations.paraphrase import paraphrase
from perturbations.emotional import emotional
from perturbations.structural import structural
from perturbations.logical_flip import logical_flip

from analysis.graph_analyzer import GraphAnalyzer
from analysis.hallucination_detector import HallucinationDetector
from analysis.confidence_estimator import ConfidenceEstimator
from analysis.stability_analyzer import StabilityAnalyzer

from visualization.heatmap import plot_heatmap


# -------------------------------------------------
# Helper function to interpret metric performance
# -------------------------------------------------
def interpret_score(score):

    if score >= 0.8:
        return "Excellent"

    elif score >= 0.6:
        return "Good"

    elif score >= 0.4:
        return "Moderate"

    else:
        return "Poor"


# -------------------------------------------------
# Special interpretation for hallucination risk
# -------------------------------------------------
def interpret_hallucination(score):

    if score == 0:
        return "No hallucination detected"

    elif score < 0.2:
        return "Low hallucination risk"

    elif score < 0.5:
        return "Moderate hallucination risk"

    else:
        return "High hallucination risk"


def main():

    # -------------------------------------------------
    # Original Prompt
    # -------------------------------------------------
    prompt = "Explain blockchain technology"

    print("\n==============================")
    print("Original Prompt:")
    print(prompt)
    print("==============================\n")

    # -------------------------------------------------
    # Prompt Perturbation
    # -------------------------------------------------
    prompts = []

    prompts.extend(paraphrase(prompt))
    prompts.extend(emotional(prompt))
    prompts.extend(structural(prompt))
    prompts.extend(logical_flip(prompt))

    prompts = list(set(prompts))

    prompts = prompts[:8]

    print("Generated Perturbed Prompts:\n")

    for i, p in enumerate(prompts):
        print(f"{i+1}. {p}")

    print("\nTotal perturbed prompts:", len(prompts))

    # -------------------------------------------------
    # LLM Generation
    # -------------------------------------------------
    llm = LLMInterface()

    responses = []

    for p in prompts:

        outputs = llm.generate(p, n=1)

        responses.extend(outputs)

    print("\n==============================")
    print("Generated Responses")
    print("==============================\n")

    for i, r in enumerate(responses):
        print(f"Response {i+1}:")
        print(r)
        print()

    print("Total generated responses:", len(responses))

    # -------------------------------------------------
    # Embedding + Similarity
    # -------------------------------------------------
    similarity_model = SimilarityModel()

    embeddings = similarity_model.embed(responses)

    similarity_score, similarity_matrix = similarity_model.similarity_score(
        embeddings
    )

    # -------------------------------------------------
    # Graph Stability
    # -------------------------------------------------
    graph_analyzer = GraphAnalyzer()

    graph = graph_analyzer.build_graph(prompt, responses)

    graph_score = graph_analyzer.graph_stability(graph)

    # -------------------------------------------------
    # Hallucination Detection
    # -------------------------------------------------
    hallucination_detector = HallucinationDetector()

    hallucination_risk = hallucination_detector.detect(responses)

    # -------------------------------------------------
    # Confidence Estimation
    # -------------------------------------------------
    confidence_estimator = ConfidenceEstimator()

    confidence_score = confidence_estimator.compute(
        similarity_score,
        graph_score,
        hallucination_risk
    )

    # -------------------------------------------------
    # Final Stability Score
    # -------------------------------------------------
    stability_analyzer = StabilityAnalyzer()

    final_score = stability_analyzer.final_score(
        similarity_score,
        graph_score,
        hallucination_risk
    )

    # -------------------------------------------------
    # Print Results
    # -------------------------------------------------
    print("\n==============================")
    print("MODEL PERFORMANCE REPORT")
    print("==============================\n")

    print("Similarity Score:", round(similarity_score, 3))
    print("Performance:", interpret_score(similarity_score), "\n")

    print("Graph Stability Score:", round(graph_score, 3))
    print("Performance:", interpret_score(graph_score), "\n")

    print("Hallucination Risk:", round(hallucination_risk, 3))
    print("Assessment:", interpret_hallucination(hallucination_risk), "\n")

    print("Confidence Score:", round(confidence_score, 3))
    print("Performance:", interpret_score(confidence_score), "\n")

    print("Final Stability Score:", round(final_score, 3))
    print("Overall Model Stability:", interpret_score(final_score))

    # -------------------------------------------------
    # Visualization
    # -------------------------------------------------
    print("\nOpening similarity heatmap...\n")

    plot_heatmap(similarity_matrix)


if __name__ == "__main__":
    main()