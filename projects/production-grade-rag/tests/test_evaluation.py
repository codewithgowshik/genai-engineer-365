import json
import time
from pathlib import Path

from src.retrieval import retrieve_and_rerank

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATASET_PATH = PROJECT_ROOT / "tests" / "evaluation_dataset.json"


def load_dataset():
    with DATASET_PATH.open(encoding="utf-8") as file:
        return json.load(file)


def test_retrieval_returns_results():
    dataset = load_dataset()

    for item in dataset:
        results = retrieve_and_rerank(item["question"])

        assert results, (
            f"No passages retrieved for: {item['question']}"
        )


def test_retrieval_includes_source_metadata():
    dataset = load_dataset()

    for item in dataset:
        results = retrieve_and_rerank(item["question"])

        assert results, f"No results for: {item['question']}"

        for result in results:
            assert "text" in result
            assert "source" in result
            assert "citation_id" in result


def test_retrieval_latency():
    dataset = load_dataset()
    durations = []

    for item in dataset:
        start = time.perf_counter()

        retrieve_and_rerank(item["question"])

        durations.append(time.perf_counter() - start)

    average_latency = sum(durations) / len(durations)

    print(f"\nAverage retrieval + reranking latency: "
          f"{average_latency:.3f} seconds")

    assert average_latency > 0
