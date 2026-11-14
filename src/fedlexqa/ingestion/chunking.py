"""Split an Akoma Ntoso law document into one chunk per article.

Fedlex publishes legislation as Akoma Ntoso XML. We parse namespace-agnostically
so the code does not break if the namespace URI differs between document versions.
"""

import xml.etree.ElementTree as ET

from fedlexqa.ingestion.models import Chunk


def _local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def _clean(text: str) -> str:
    return " ".join(text.split())


def chunk_articles(xml_text: str, law_id: str, language: str) -> list[Chunk]:
    """Return one Chunk per <article> element, skipping empty ones."""
    root = ET.fromstring(xml_text)
    chunks: list[Chunk] = []
    for elem in root.iter():
        if _local(elem.tag) != "article":
            continue
        num = heading = ""
        body_parts: list[str] = []
        for child in elem:
            name = _local(child.tag)
            if name == "num":
                num = _clean("".join(child.itertext()))
            elif name == "heading":
                heading = _clean("".join(child.itertext()))
            else:
                body_parts.append(_clean("".join(child.itertext())))
        text = _clean(" ".join(body_parts))
        if not text:
            continue
        chunks.append(
            Chunk(
                law_id=law_id,
                language=language,
                article_id=elem.get("eId", ""),
                article_num=num,
                heading=heading,
                text=text,
            )
        )
    return chunks
