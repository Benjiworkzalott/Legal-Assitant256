from pathlib import Path

from fedlexqa.ingestion.chunking import chunk_articles

FIXTURE = Path(__file__).parent / "fixtures" / "sample_law.xml"


def test_one_chunk_per_non_empty_article() -> None:
    chunks = chunk_articles(FIXTURE.read_text(encoding="utf-8"), "SR 235.1", "fr")
    assert [c.article_num for c in chunks] == ["Art. 1", "Art. 2"]


def test_chunk_metadata_and_text() -> None:
    chunks = chunk_articles(FIXTURE.read_text(encoding="utf-8"), "SR 235.1", "fr")
    art2 = chunks[1]
    assert art2.heading == "Champ d'application"
    assert art2.language == "fr"
    assert "personnes privées" in art2.text
    assert "délibérations publiques" in art2.text
    assert art2.citation == "SR 235.1 Art. 2"
