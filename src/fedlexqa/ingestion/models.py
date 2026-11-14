from pydantic import BaseModel


class Chunk(BaseModel):
    """One retrievable unit: a single article of a law, with citation metadata."""

    law_id: str
    language: str
    article_id: str
    article_num: str
    heading: str
    text: str

    @property
    def citation(self) -> str:
        return f"{self.law_id} {self.article_num}".strip()
