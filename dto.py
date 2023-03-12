from dataclasses import dataclass
from typing import Union, List, Optional
from pydantic import BaseModel


@dataclass(frozen=False)
class RedisScheme(BaseModel):
    document: List[str] = None
    prompt: str = None
    summarized: dict = None


class TextSummarizeRequestParams(BaseModel):
    text: Union[str, List[str]]
    model: str = 'text-davinci-003'
    temperature: float = 0.5
