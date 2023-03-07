import os
from fastapi import FastAPI, Body, HTTPException, status
from fastapi.responses import Response, JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId
from typing import Optional, List, Union,Tuple
import motor.motor_asyncio
import phrase_model
import optional_model

app = FastAPI()
client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGOdb1_URL"])
db1 = client.arxiv_LDA_MATRIX_copy


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class PhraseModel(BaseModel):
    field_id: int = Field(..., alias='_id')
    txt_id: int = Field(...)
    path: str = Field(...)
    phrase: str = Field(...)
    lenght: int = Field(...)
    section: str = Field(...)
    a_id: int = Field(...)
    match_word: List[str] = Field(...)
    topics: phrase_model.Topics = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "_id": 0,
                "txt_id": 6,
                "path": "./pdf/0001/0001008v3.tei.xml",
                "phrase": "this is the traditional machine learning problem.",
                "lenght": 49,
                "section": "text",
                "a_id": 885,
                "match_word": [
                    "machine learning"
                ],
                "topics": {
                    "5t_0,05a_0,005e": {
                        "number_of_topics": 5,
                        "alpha": 0.05,
                        "eta": 0.005,
                        "topics": [
                            {
                                "topic": 1,
                                "prob": 0.95294
                            }
                        ]
                    },
                    "10t_0,05a_0,005e": {
                        "number_of_topics": 10,
                        "alpha": 0.05,
                        "eta": 0.005,
                        "topics": [
                            {
                                "topic": 5,
                                "prob": 0.67778
                            },
                            {
                                "topic": 3,
                                "prob": 0.23333
                            }
                        ]
                    },
                    "20t_0,05a_0,005e": {
                        "number_of_topics": 20,
                        "alpha": 0.05,
                        "eta": 0.005,
                        "topics": [
                            {
                                "topic": 12,
                                "prob": 0.61
                            },
                            {
                                "topic": 4,
                                "prob": 0.21
                            }
                        ]
                    },
                    "40t_0,05a_0,005e": {
                        "number_of_topics": 40,
                        "alpha": 0.05,
                        "eta": 0.005,
                        "topics": [
                            {
                                "topic": 33,
                                "prob": 0.50833
                            },
                            {
                                "topic": 2,
                                "prob": 0.175
                            }
                        ]
                    },
                    "5t_0,05a_0,01e": {
                        "number_of_topics": 5,
                        "alpha": 0.05,
                        "eta": 0.01,
                        "topics": [
                            {
                                "topic": 1,
                                "prob": 0.71765
                            },
                            {
                                "topic": 0,
                                "prob": 0.24706
                            }
                        ]
                    },
                    "10t_0,05a_0,01e": {
                        "number_of_topics": 10,
                        "alpha": 0.05,
                        "eta": 0.01,
                        "topics": [
                            {
                                "topic": 5,
                                "prob": 0.67778
                            },
                            {
                                "topic": 2,
                                "prob": 0.23333
                            }
                        ]
                    },
                    "20t_0,05a_0,01e": {
                        "number_of_topics": 20,
                        "alpha": 0.05,
                        "eta": 0.01,
                        "topics": [
                            {
                                "topic": 4,
                                "prob": 0.41
                            },
                            {
                                "topic": 2,
                                "prob": 0.21
                            },
                            {
                                "topic": 12,
                                "prob": 0.21
                            }
                        ]
                    },
                    "40t_0,05a_0,01e": {
                        "number_of_topics": 40,
                        "alpha": 0.05,
                        "eta": 0.01,
                        "topics": [
                            {
                                "topic": 9,
                                "prob": 0.34167
                            },
                            {
                                "topic": 24,
                                "prob": 0.175
                            },
                            {
                                "topic": 6,
                                "prob": 0.175
                            }
                        ]
                    },
                    "5t_0,05a_0,05e": {
                        "number_of_topics": 5,
                        "alpha": 0.05,
                        "eta": 0.05,
                        "topics": [
                            {
                                "topic": 3,
                                "prob": 0.95294
                            }
                        ]
                    },
                    "10t_0,05a_0,05e": {
                        "number_of_topics": 10,
                        "alpha": 0.05,
                        "eta": 0.05,
                        "topics": [
                            {
                                "topic": 5,
                                "prob": 0.67778
                            },
                            {
                                "topic": 3,
                                "prob": 0.23333
                            }
                        ]
                    },
                    "20t_0,05a_0,05e": {
                        "number_of_topics": 20,
                        "alpha": 0.05,
                        "eta": 0.05,
                        "topics": [
                            {
                                "topic": 1,
                                "prob": 0.61
                            },
                            {
                                "topic": 13,
                                "prob": 0.21
                            }
                        ]
                    },
                    "40t_0,05a_0,05e": {
                        "number_of_topics": 40,
                        "alpha": 0.05,
                        "eta": 0.05,
                        "topics": [
                            {
                                "topic": 7,
                                "prob": 0.675
                            }
                        ]
                    },
                    "5t_0,05a_0,1e": {
                        "number_of_topics": 5,
                        "alpha": 0.05,
                        "eta": 0.1,
                        "topics": [
                            {
                                "topic": 2,
                                "prob": 0.95294
                            }
                        ]
                    },
                    "10t_0,05a_0,1e": {
                        "number_of_topics": 10,
                        "alpha": 0.05,
                        "eta": 0.1,
                        "topics": [
                            {
                                "topic": 7,
                                "prob": 0.67778
                            },
                            {
                                "topic": 2,
                                "prob": 0.23333
                            }
                        ]
                    },
                    "20t_0,05a_0,1e": {
                        "number_of_topics": 20,
                        "alpha": 0.05,
                        "eta": 0.1,
                        "topics": [
                            {
                                "topic": 2,
                                "prob": 0.61
                            },
                            {
                                "topic": 13,
                                "prob": 0.21
                            }
                        ]
                    },
                    "40t_0,05a_0,1e": {
                        "number_of_topics": 40,
                        "alpha": 0.05,
                        "eta": 0.1,
                        "topics": [
                            {
                                "topic": 34,
                                "prob": 0.34167
                            },
                            {
                                "topic": 33,
                                "prob": 0.175
                            },
                            {
                                "topic": 6,
                                "prob": 0.175
                            }
                        ]
                    },
                    "5t_0,1a_0,005e": {
                        "number_of_topics": 5,
                        "alpha": 0.1,
                        "eta": 0.005,
                        "topics": [
                            {
                                "topic": 0,
                                "prob": 0.91111
                            }
                        ]
                    },
                    "10t_0,1a_0,005e": {
                        "number_of_topics": 10,
                        "alpha": 0.1,
                        "eta": 0.005,
                        "topics": [
                            {
                                "topic": 7,
                                "prob": 0.62
                            },
                            {
                                "topic": 2,
                                "prob": 0.22
                            }
                        ]
                    },
                    "20t_0,1a_0,005e": {
                        "number_of_topics": 20,
                        "alpha": 0.1,
                        "eta": 0.005,
                        "topics": [
                            {
                                "topic": 3,
                                "prob": 0.18333
                            },
                            {
                                "topic": 14,
                                "prob": 0.18333
                            },
                            {
                                "topic": 8,
                                "prob": 0.18333
                            },
                            {
                                "topic": 10,
                                "prob": 0.18333
                            }
                        ]
                    },
                    "40t_0,1a_0,005e": {
                        "number_of_topics": 40,
                        "alpha": 0.1,
                        "eta": 0.005,
                        "topics": [
                            {
                                "topic": 23,
                                "prob": 0.2625
                            },
                            {
                                "topic": 36,
                                "prob": 0.1375
                            },
                            {
                                "topic": 4,
                                "prob": 0.1375
                            }
                        ]
                    },
                    "5t_0,1a_0,01e": {
                        "number_of_topics": 5,
                        "alpha": 0.1,
                        "eta": 0.01,
                        "topics": [
                            {
                                "topic": 0,
                                "prob": 0.91111
                            }
                        ]
                    },
                    "10t_0,1a_0,01e": {
                        "number_of_topics": 10,
                        "alpha": 0.1,
                        "eta": 0.01,
                        "topics": [
                            {
                                "topic": 7,
                                "prob": 0.62
                            },
                            {
                                "topic": 3,
                                "prob": 0.22
                            }
                        ]
                    },
                    "20t_0,1a_0,01e": {
                        "number_of_topics": 20,
                        "alpha": 0.1,
                        "eta": 0.01,
                        "topics": [
                            {
                                "topic": 17,
                                "prob": 0.51667
                            },
                            {
                                "topic": 0,
                                "prob": 0.18333
                            }
                        ]
                    },
                    "40t_0,1a_0,01e": {
                        "number_of_topics": 40,
                        "alpha": 0.1,
                        "eta": 0.01,
                        "topics": [
                            {
                                "topic": 0,
                                "prob": 0.2625
                            },
                            {
                                "topic": 22,
                                "prob": 0.1375
                            },
                            {
                                "topic": 2,
                                "prob": 0.1375
                            }
                        ]
                    },
                    "5t_0,1a_0,05e": {
                        "number_of_topics": 5,
                        "alpha": 0.1,
                        "eta": 0.05,
                        "topics": [
                            {
                                "topic": 2,
                                "prob": 0.91111
                            }
                        ]
                    },
                    "10t_0,1a_0,05e": {
                        "number_of_topics": 10,
                        "alpha": 0.1,
                        "eta": 0.05,
                        "topics": [
                            {
                                "topic": 1,
                                "prob": 0.62
                            },
                            {
                                "topic": 0,
                                "prob": 0.22
                            }
                        ]
                    },
                    "20t_0,1a_0,05e": {
                        "number_of_topics": 20,
                        "alpha": 0.1,
                        "eta": 0.05,
                        "topics": [
                            {
                                "topic": 17,
                                "prob": 0.51667
                            },
                            {
                                "topic": 2,
                                "prob": 0.18333
                            }
                        ]
                    },
                    "40t_0,1a_0,05e": {
                        "number_of_topics": 40,
                        "alpha": 0.1,
                        "eta": 0.05,
                        "topics": [
                            {
                                "topic": 16,
                                "prob": 0.2625
                            },
                            {
                                "topic": 23,
                                "prob": 0.1375
                            },
                            {
                                "topic": 5,
                                "prob": 0.1375
                            }
                        ]
                    },
                    "5t_0,1a_0,1e": {
                        "number_of_topics": 5,
                        "alpha": 0.1,
                        "eta": 0.1,
                        "topics": [
                            {
                                "topic": 1,
                                "prob": 0.91111
                            }
                        ]
                    },
                    "10t_0,1a_0,1e": {
                        "number_of_topics": 10,
                        "alpha": 0.1,
                        "eta": 0.1,
                        "topics": [
                            {
                                "topic": 5,
                                "prob": 0.62
                            },
                            {
                                "topic": 3,
                                "prob": 0.22
                            }
                        ]
                    },
                    "20t_0,1a_0,1e": {
                        "number_of_topics": 20,
                        "alpha": 0.1,
                        "eta": 0.1,
                        "topics": [
                            {
                                "topic": 14,
                                "prob": 0.51667
                            },
                            {
                                "topic": 3,
                                "prob": 0.18333
                            }
                        ]
                    },
                    "40t_0,1a_0,1e": {
                        "number_of_topics": 40,
                        "alpha": 0.1,
                        "eta": 0.1,
                        "topics": [
                            {
                                "topic": 23,
                                "prob": 0.3875
                            },
                            {
                                "topic": 6,
                                "prob": 0.1375
                            }
                        ]
                    },
                    "5t_0,5a_0,005e": {
                        "number_of_topics": 5,
                        "alpha": 0.5,
                        "eta": 0.005,
                        "topics": [
                            {
                                "topic": 0,
                                "prob": 0.23077
                            },
                            {
                                "topic": 1,
                                "prob": 0.23077
                            },
                            {
                                "topic": 2,
                                "prob": 0.23077
                            },
                            {
                                "topic": 3,
                                "prob": 0.23077
                            }
                        ]
                    },
                    "10t_0,5a_0,005e": {
                        "number_of_topics": 10,
                        "alpha": 0.5,
                        "eta": 0.005,
                        "topics": [
                            {
                                "topic": 1,
                                "prob": 0.27778
                            },
                            {
                                "topic": 7,
                                "prob": 0.27778
                            }
                        ]
                    },
                    "20t_0,5a_0,005e": {
                        "number_of_topics": 20,
                        "alpha": 0.5,
                        "eta": 0.005,
                        "topics": [
                            {
                                "topic": 6,
                                "prob": 0.17857
                            },
                            {
                                "topic": 0,
                                "prob": 0.10714
                            },
                            {
                                "topic": 17,
                                "prob": 0.10714
                            }
                        ]
                    },
                    "40t_0,5a_0,005e": {
                        "number_of_topics": 40,
                        "alpha": 0.5,
                        "eta": 0.005,
                        "topics": [
                            {
                                "topic": 0,
                                "prob": 0.0625
                            },
                            {
                                "topic": 22,
                                "prob": 0.0625
                            },
                            {
                                "topic": 15,
                                "prob": 0.0625
                            },
                            {
                                "topic": 20,
                                "prob": 0.0625
                            }
                        ]
                    },
                    "5t_0,5a_0,01e": {
                        "number_of_topics": 5,
                        "alpha": 0.5,
                        "eta": 0.01,
                        "topics": [
                            {
                                "topic": 2,
                                "prob": 0.38462
                            },
                            {
                                "topic": 0,
                                "prob": 0.23077
                            },
                            {
                                "topic": 3,
                                "prob": 0.23077
                            }
                        ]
                    },
                    "10t_0,5a_0,01e": {
                        "number_of_topics": 10,
                        "alpha": 0.5,
                        "eta": 0.01,
                        "topics": [
                            {
                                "topic": 7,
                                "prob": 0.27778
                            },
                            {
                                "topic": 0,
                                "prob": 0.16667
                            },
                            {
                                "topic": 4,
                                "prob": 0.16667
                            }
                        ]
                    },
                    "20t_0,5a_0,01e": {
                        "number_of_topics": 20,
                        "alpha": 0.5,
                        "eta": 0.01,
                        "topics": [
                            {
                                "topic": 12,
                                "prob": 0.17857
                            },
                            {
                                "topic": 2,
                                "prob": 0.10714
                            },
                            {
                                "topic": 13,
                                "prob": 0.10714
                            }
                        ]
                    },
                    "40t_0,5a_0,01e": {
                        "number_of_topics": 40,
                        "alpha": 0.5,
                        "eta": 0.01,
                        "topics": [
                            {
                                "topic": 19,
                                "prob": 0.0625
                            },
                            {
                                "topic": 2,
                                "prob": 0.0625
                            },
                            {
                                "topic": 15,
                                "prob": 0.0625
                            },
                            {
                                "topic": 26,
                                "prob": 0.0625
                            }
                        ]
                    },
                    "5t_0,5a_0,05e": {
                        "number_of_topics": 5,
                        "alpha": 0.5,
                        "eta": 0.05,
                        "topics": [
                            {
                                "topic": 0,
                                "prob": 0.69231
                            }
                        ]
                    },
                    "10t_0,5a_0,05e": {
                        "number_of_topics": 10,
                        "alpha": 0.5,
                        "eta": 0.05,
                        "topics": [
                            {
                                "topic": 4,
                                "prob": 0.38889
                            },
                            {
                                "topic": 0,
                                "prob": 0.16667
                            }
                        ]
                    },
                    "20t_0,5a_0,05e": {
                        "number_of_topics": 20,
                        "alpha": 0.5,
                        "eta": 0.05,
                        "topics": [
                            {
                                "topic": 0,
                                "prob": 0.10714
                            },
                            {
                                "topic": 14,
                                "prob": 0.10714
                            },
                            {
                                "topic": 13,
                                "prob": 0.10714
                            },
                            {
                                "topic": 7,
                                "prob": 0.10714
                            }
                        ]
                    },
                    "40t_0,5a_0,05e": {
                        "number_of_topics": 40,
                        "alpha": 0.5,
                        "eta": 0.05,
                        "topics": [
                            {
                                "topic": 24,
                                "prob": 0.0625
                            },
                            {
                                "topic": 4,
                                "prob": 0.0625
                            },
                            {
                                "topic": 25,
                                "prob": 0.0625
                            },
                            {
                                "topic": 28,
                                "prob": 0.0625
                            }
                        ]
                    },
                    "5t_0,5a_0,1e": {
                        "number_of_topics": 5,
                        "alpha": 0.5,
                        "eta": 0.1,
                        "topics": [
                            {
                                "topic": 0,
                                "prob": 0.53846
                            },
                            {
                                "topic": 1,
                                "prob": 0.23077
                            }
                        ]
                    },
                    "10t_0,5a_0,1e": {
                        "number_of_topics": 10,
                        "alpha": 0.5,
                        "eta": 0.1,
                        "topics": [
                            {
                                "topic": 0,
                                "prob": 0.16667
                            },
                            {
                                "topic": 2,
                                "prob": 0.16667
                            },
                            {
                                "topic": 5,
                                "prob": 0.16667
                            },
                            {
                                "topic": 6,
                                "prob": 0.16667
                            }
                        ]
                    },
                    "20t_0,5a_0,1e": {
                        "number_of_topics": 20,
                        "alpha": 0.5,
                        "eta": 0.1,
                        "topics": [
                            {
                                "topic": 0,
                                "prob": 0.10714
                            },
                            {
                                "topic": 14,
                                "prob": 0.10714
                            },
                            {
                                "topic": 10,
                                "prob": 0.10714
                            },
                            {
                                "topic": 9,
                                "prob": 0.10714
                            }
                        ]
                    },
                    "40t_0,5a_0,1e": {
                        "number_of_topics": 40,
                        "alpha": 0.5,
                        "eta": 0.1,
                        "topics": [
                            {
                                "topic": 0,
                                "prob": 0.0625
                            },
                            {
                                "topic": 28,
                                "prob": 0.0625
                            },
                            {
                                "topic": 31,
                                "prob": 0.0625
                            },
                            {
                                "topic": 20,
                                "prob": 0.0625
                            }
                        ]
                    },
                    "5t_0,9a_0,005e": {
                        "number_of_topics": 5,
                        "alpha": 0.9,
                        "eta": 0.005,
                        "topics": [
                            {
                                "topic": 2,
                                "prob": 0.34118
                            },
                            {
                                "topic": 0,
                                "prob": 0.22353
                            },
                            {
                                "topic": 1,
                                "prob": 0.22353
                            }
                        ]
                    },
                    "10t_0,9a_0,005e": {
                        "number_of_topics": 10,
                        "alpha": 0.9,
                        "eta": 0.005,
                        "topics": [
                            {
                                "topic": 7,
                                "prob": 0.22308
                            },
                            {
                                "topic": 1,
                                "prob": 0.14615
                            },
                            {
                                "topic": 5,
                                "prob": 0.14615
                            }
                        ]
                    },
                    "20t_0,9a_0,005e": {
                        "number_of_topics": 20,
                        "alpha": 0.9,
                        "eta": 0.005,
                        "topics": [
                            {
                                "topic": 9,
                                "prob": 0.13182
                            },
                            {
                                "topic": 11,
                                "prob": 0.08636
                            },
                            {
                                "topic": 0,
                                "prob": 0.08636
                            }
                        ]
                    },
                    "40t_0,9a_0,005e": {
                        "number_of_topics": 40,
                        "alpha": 0.9,
                        "eta": 0.005,
                        "topics": [
                            {
                                "topic": 0,
                                "prob": 0.0475
                            },
                            {
                                "topic": 32,
                                "prob": 0.0475
                            },
                            {
                                "topic": 27,
                                "prob": 0.0475
                            },
                            {
                                "topic": 28,
                                "prob": 0.0475
                            }
                        ]
                    },
                    "5t_0,9a_0,01e": {
                        "number_of_topics": 5,
                        "alpha": 0.9,
                        "eta": 0.01,
                        "topics": [
                            {
                                "topic": 2,
                                "prob": 0.34118
                            },
                            {
                                "topic": 0,
                                "prob": 0.22353
                            },
                            {
                                "topic": 1,
                                "prob": 0.22353
                            }
                        ]
                    },
                    "10t_0,9a_0,01e": {
                        "number_of_topics": 10,
                        "alpha": 0.9,
                        "eta": 0.01,
                        "topics": [
                            {
                                "topic": 1,
                                "prob": 0.22308
                            },
                            {
                                "topic": 2,
                                "prob": 0.14615
                            },
                            {
                                "topic": 5,
                                "prob": 0.14615
                            }
                        ]
                    },
                    "20t_0,9a_0,01e": {
                        "number_of_topics": 20,
                        "alpha": 0.9,
                        "eta": 0.01,
                        "topics": [
                            {
                                "topic": 10,
                                "prob": 0.13182
                            },
                            {
                                "topic": 0,
                                "prob": 0.08636
                            },
                            {
                                "topic": 14,
                                "prob": 0.08636
                            }
                        ]
                    },
                    "40t_0,9a_0,01e": {
                        "number_of_topics": 40,
                        "alpha": 0.9,
                        "eta": 0.01,
                        "topics": [
                            {
                                "topic": 1,
                                "prob": 0.0475
                            },
                            {
                                "topic": 22,
                                "prob": 0.0475
                            },
                            {
                                "topic": 23,
                                "prob": 0.0475
                            },
                            {
                                "topic": 28,
                                "prob": 0.0475
                            }
                        ]
                    },
                    "5t_0,9a_0,05e": {
                        "number_of_topics": 5,
                        "alpha": 0.9,
                        "eta": 0.05,
                        "topics": [
                            {
                                "topic": 0,
                                "prob": 0.22353
                            },
                            {
                                "topic": 1,
                                "prob": 0.22353
                            },
                            {
                                "topic": 2,
                                "prob": 0.22353
                            },
                            {
                                "topic": 3,
                                "prob": 0.22353
                            }
                        ]
                    },
                    "10t_0,9a_0,05e": {
                        "number_of_topics": 10,
                        "alpha": 0.9,
                        "eta": 0.05,
                        "topics": [
                            {
                                "topic": 8,
                                "prob": 0.3
                            },
                            {
                                "topic": 1,
                                "prob": 0.14615
                            }
                        ]
                    },
                    "20t_0,9a_0,05e": {
                        "number_of_topics": 20,
                        "alpha": 0.9,
                        "eta": 0.05,
                        "topics": [
                            {
                                "topic": 0,
                                "prob": 0.08636
                            },
                            {
                                "topic": 14,
                                "prob": 0.08636
                            },
                            {
                                "topic": 12,
                                "prob": 0.08636
                            },
                            {
                                "topic": 7,
                                "prob": 0.08636
                            }
                        ]
                    },
                    "40t_0,9a_0,05e": {
                        "number_of_topics": 40,
                        "alpha": 0.9,
                        "eta": 0.05,
                        "topics": [
                            {
                                "topic": 30,
                                "prob": 0.0725
                            },
                            {
                                "topic": 0,
                                "prob": 0.0475
                            },
                            {
                                "topic": 36,
                                "prob": 0.0475
                            }
                        ]
                    },
                    "5t_0,9a_0,1e": {
                        "number_of_topics": 5,
                        "alpha": 0.9,
                        "eta": 0.1,
                        "topics": [
                            {
                                "topic": 3,
                                "prob": 0.45882
                            },
                            {
                                "topic": 1,
                                "prob": 0.22353
                            }
                        ]
                    },
                    "10t_0,9a_0,1e": {
                        "number_of_topics": 10,
                        "alpha": 0.9,
                        "eta": 0.1,
                        "topics": [
                            {
                                "topic": 4,
                                "prob": 0.22308
                            },
                            {
                                "topic": 0,
                                "prob": 0.14615
                            },
                            {
                                "topic": 5,
                                "prob": 0.14615
                            }
                        ]
                    },
                    "20t_0,9a_0,1e": {
                        "number_of_topics": 20,
                        "alpha": 0.9,
                        "eta": 0.1,
                        "topics": [
                            {
                                "topic": 0,
                                "prob": 0.08636
                            },
                            {
                                "topic": 17,
                                "prob": 0.08636
                            },
                            {
                                "topic": 12,
                                "prob": 0.08636
                            },
                            {
                                "topic": 10,
                                "prob": 0.08636
                            }
                        ]
                    },
                    "40t_0,9a_0,1e": {
                        "number_of_topics": 40,
                        "alpha": 0.9,
                        "eta": 0.1,
                        "topics": [
                            {
                                "topic": 32,
                                "prob": 0.0725
                            },
                            {
                                "topic": 2,
                                "prob": 0.0475
                            },
                            {
                                "topic": 23,
                                "prob": 0.0475
                            }
                        ]
                    }
                }
            }
        }


class UpdatePhraseModel(BaseModel):
    txt_id: Optional[int]
    path: Optional[str]
    phrase: Optional[str]
    lenght: Optional[int]
    section: Optional[str]
    a_id: Optional[int]
    match_word: Optional[List[str]]
    topics: Optional[optional_model.Topics]



    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example":  {
                "txt_id": 6,
                "path": "./pdf/0001/0001008v3.tei.xml",
                "phrase": "this is the traditional machine learning problem.",
                "lenght": 49,
                "section": "text",
                "a_id": 885,
                "match_word": [
                    "machine learning"
                ],
                "topics": {
                    "5t_0,05a_0,005e": {
                        "number_of_topics": 5,
                        "alpha": 0.05,
                        "eta": 0.005,
                        "topics": [
                            {
                                "topic": 1,
                                "prob": 0.95294
                            }
                        ]
                    },
                    "10t_0,05a_0,005e": {
                        "number_of_topics": 10,
                        "alpha": 0.05,
                        "eta": 0.005,
                        "topics": [
                            {
                                "topic": 5,
                                "prob": 0.67778
                            },
                            {
                                "topic": 3,
                                "prob": 0.23333
                            }
                        ]
                    },
                    "20t_0,05a_0,005e": {
                        "number_of_topics": 20,
                        "alpha": 0.05,
                        "eta": 0.005,
                        "topics": [
                            {
                                "topic": 12,
                                "prob": 0.61
                            },
                            {
                                "topic": 4,
                                "prob": 0.21
                            }
                        ]
                    },
                    "40t_0,05a_0,005e": {
                        "number_of_topics": 40,
                        "alpha": 0.05,
                        "eta": 0.005,
                        "topics": [
                            {
                                "topic": 33,
                                "prob": 0.50833
                            },
                            {
                                "topic": 2,
                                "prob": 0.175
                            }
                        ]
                    },
                    "5t_0,05a_0,01e": {
                        "number_of_topics": 5,
                        "alpha": 0.05,
                        "eta": 0.01,
                        "topics": [
                            {
                                "topic": 1,
                                "prob": 0.71765
                            },
                            {
                                "topic": 0,
                                "prob": 0.24706
                            }
                        ]
                    },
                    "10t_0,05a_0,01e": {
                        "number_of_topics": 10,
                        "alpha": 0.05,
                        "eta": 0.01,
                        "topics": [
                            {
                                "topic": 5,
                                "prob": 0.67778
                            },
                            {
                                "topic": 2,
                                "prob": 0.23333
                            }
                        ]
                    },
                    "20t_0,05a_0,01e": {
                        "number_of_topics": 20,
                        "alpha": 0.05,
                        "eta": 0.01,
                        "topics": [
                            {
                                "topic": 4,
                                "prob": 0.41
                            },
                            {
                                "topic": 2,
                                "prob": 0.21
                            },
                            {
                                "topic": 12,
                                "prob": 0.21
                            }
                        ]
                    },
                    "40t_0,05a_0,01e": {
                        "number_of_topics": 40,
                        "alpha": 0.05,
                        "eta": 0.01,
                        "topics": [
                            {
                                "topic": 9,
                                "prob": 0.34167
                            },
                            {
                                "topic": 24,
                                "prob": 0.175
                            },
                            {
                                "topic": 6,
                                "prob": 0.175
                            }
                        ]
                    },
                    "5t_0,05a_0,05e": {
                        "number_of_topics": 5,
                        "alpha": 0.05,
                        "eta": 0.05,
                        "topics": [
                            {
                                "topic": 3,
                                "prob": 0.95294
                            }
                        ]
                    },
                    "10t_0,05a_0,05e": {
                        "number_of_topics": 10,
                        "alpha": 0.05,
                        "eta": 0.05,
                        "topics": [
                            {
                                "topic": 5,
                                "prob": 0.67778
                            },
                            {
                                "topic": 3,
                                "prob": 0.23333
                            }
                        ]
                    },
                    "20t_0,05a_0,05e": {
                        "number_of_topics": 20,
                        "alpha": 0.05,
                        "eta": 0.05,
                        "topics": [
                            {
                                "topic": 1,
                                "prob": 0.61
                            },
                            {
                                "topic": 13,
                                "prob": 0.21
                            }
                        ]
                    },
                    "40t_0,05a_0,05e": {
                        "number_of_topics": 40,
                        "alpha": 0.05,
                        "eta": 0.05,
                        "topics": [
                            {
                                "topic": 7,
                                "prob": 0.675
                            }
                        ]
                    },
                    "5t_0,05a_0,1e": {
                        "number_of_topics": 5,
                        "alpha": 0.05,
                        "eta": 0.1,
                        "topics": [
                            {
                                "topic": 2,
                                "prob": 0.95294
                            }
                        ]
                    },
                    "10t_0,05a_0,1e": {
                        "number_of_topics": 10,
                        "alpha": 0.05,
                        "eta": 0.1,
                        "topics": [
                            {
                                "topic": 7,
                                "prob": 0.67778
                            },
                            {
                                "topic": 2,
                                "prob": 0.23333
                            }
                        ]
                    },
                    "20t_0,05a_0,1e": {
                        "number_of_topics": 20,
                        "alpha": 0.05,
                        "eta": 0.1,
                        "topics": [
                            {
                                "topic": 2,
                                "prob": 0.61
                            },
                            {
                                "topic": 13,
                                "prob": 0.21
                            }
                        ]
                    },
                    "40t_0,05a_0,1e": {
                        "number_of_topics": 40,
                        "alpha": 0.05,
                        "eta": 0.1,
                        "topics": [
                            {
                                "topic": 34,
                                "prob": 0.34167
                            },
                            {
                                "topic": 33,
                                "prob": 0.175
                            },
                            {
                                "topic": 6,
                                "prob": 0.175
                            }
                        ]
                    },
                    "5t_0,1a_0,005e": {
                        "number_of_topics": 5,
                        "alpha": 0.1,
                        "eta": 0.005,
                        "topics": [
                            {
                                "topic": 0,
                                "prob": 0.91111
                            }
                        ]
                    },
                    "10t_0,1a_0,005e": {
                        "number_of_topics": 10,
                        "alpha": 0.1,
                        "eta": 0.005,
                        "topics": [
                            {
                                "topic": 7,
                                "prob": 0.62
                            },
                            {
                                "topic": 2,
                                "prob": 0.22
                            }
                        ]
                    },
                    "20t_0,1a_0,005e": {
                        "number_of_topics": 20,
                        "alpha": 0.1,
                        "eta": 0.005,
                        "topics": [
                            {
                                "topic": 3,
                                "prob": 0.18333
                            },
                            {
                                "topic": 14,
                                "prob": 0.18333
                            },
                            {
                                "topic": 8,
                                "prob": 0.18333
                            },
                            {
                                "topic": 10,
                                "prob": 0.18333
                            }
                        ]
                    },
                    "40t_0,1a_0,005e": {
                        "number_of_topics": 40,
                        "alpha": 0.1,
                        "eta": 0.005,
                        "topics": [
                            {
                                "topic": 23,
                                "prob": 0.2625
                            },
                            {
                                "topic": 36,
                                "prob": 0.1375
                            },
                            {
                                "topic": 4,
                                "prob": 0.1375
                            }
                        ]
                    },
                    "5t_0,1a_0,01e": {
                        "number_of_topics": 5,
                        "alpha": 0.1,
                        "eta": 0.01,
                        "topics": [
                            {
                                "topic": 0,
                                "prob": 0.91111
                            }
                        ]
                    },
                    "10t_0,1a_0,01e": {
                        "number_of_topics": 10,
                        "alpha": 0.1,
                        "eta": 0.01,
                        "topics": [
                            {
                                "topic": 7,
                                "prob": 0.62
                            },
                            {
                                "topic": 3,
                                "prob": 0.22
                            }
                        ]
                    },
                    "20t_0,1a_0,01e": {
                        "number_of_topics": 20,
                        "alpha": 0.1,
                        "eta": 0.01,
                        "topics": [
                            {
                                "topic": 17,
                                "prob": 0.51667
                            },
                            {
                                "topic": 0,
                                "prob": 0.18333
                            }
                        ]
                    },
                    "40t_0,1a_0,01e": {
                        "number_of_topics": 40,
                        "alpha": 0.1,
                        "eta": 0.01,
                        "topics": [
                            {
                                "topic": 0,
                                "prob": 0.2625
                            },
                            {
                                "topic": 22,
                                "prob": 0.1375
                            },
                            {
                                "topic": 2,
                                "prob": 0.1375
                            }
                        ]
                    },
                    "5t_0,1a_0,05e": {
                        "number_of_topics": 5,
                        "alpha": 0.1,
                        "eta": 0.05,
                        "topics": [
                            {
                                "topic": 2,
                                "prob": 0.91111
                            }
                        ]
                    },
                    "10t_0,1a_0,05e": {
                        "number_of_topics": 10,
                        "alpha": 0.1,
                        "eta": 0.05,
                        "topics": [
                            {
                                "topic": 1,
                                "prob": 0.62
                            },
                            {
                                "topic": 0,
                                "prob": 0.22
                            }
                        ]
                    },
                    "20t_0,1a_0,05e": {
                        "number_of_topics": 20,
                        "alpha": 0.1,
                        "eta": 0.05,
                        "topics": [
                            {
                                "topic": 17,
                                "prob": 0.51667
                            },
                            {
                                "topic": 2,
                                "prob": 0.18333
                            }
                        ]
                    },
                    "40t_0,1a_0,05e": {
                        "number_of_topics": 40,
                        "alpha": 0.1,
                        "eta": 0.05,
                        "topics": [
                            {
                                "topic": 16,
                                "prob": 0.2625
                            },
                            {
                                "topic": 23,
                                "prob": 0.1375
                            },
                            {
                                "topic": 5,
                                "prob": 0.1375
                            }
                        ]
                    },
                    "5t_0,1a_0,1e": {
                        "number_of_topics": 5,
                        "alpha": 0.1,
                        "eta": 0.1,
                        "topics": [
                            {
                                "topic": 1,
                                "prob": 0.91111
                            }
                        ]
                    },
                    "10t_0,1a_0,1e": {
                        "number_of_topics": 10,
                        "alpha": 0.1,
                        "eta": 0.1,
                        "topics": [
                            {
                                "topic": 5,
                                "prob": 0.62
                            },
                            {
                                "topic": 3,
                                "prob": 0.22
                            }
                        ]
                    },
                    "20t_0,1a_0,1e": {
                        "number_of_topics": 20,
                        "alpha": 0.1,
                        "eta": 0.1,
                        "topics": [
                            {
                                "topic": 14,
                                "prob": 0.51667
                            },
                            {
                                "topic": 3,
                                "prob": 0.18333
                            }
                        ]
                    },
                    "40t_0,1a_0,1e": {
                        "number_of_topics": 40,
                        "alpha": 0.1,
                        "eta": 0.1,
                        "topics": [
                            {
                                "topic": 23,
                                "prob": 0.3875
                            },
                            {
                                "topic": 6,
                                "prob": 0.1375
                            }
                        ]
                    },
                    "5t_0,5a_0,005e": {
                        "number_of_topics": 5,
                        "alpha": 0.5,
                        "eta": 0.005,
                        "topics": [
                            {
                                "topic": 0,
                                "prob": 0.23077
                            },
                            {
                                "topic": 1,
                                "prob": 0.23077
                            },
                            {
                                "topic": 2,
                                "prob": 0.23077
                            },
                            {
                                "topic": 3,
                                "prob": 0.23077
                            }
                        ]
                    },
                    "10t_0,5a_0,005e": {
                        "number_of_topics": 10,
                        "alpha": 0.5,
                        "eta": 0.005,
                        "topics": [
                            {
                                "topic": 1,
                                "prob": 0.27778
                            },
                            {
                                "topic": 7,
                                "prob": 0.27778
                            }
                        ]
                    },
                    "20t_0,5a_0,005e": {
                        "number_of_topics": 20,
                        "alpha": 0.5,
                        "eta": 0.005,
                        "topics": [
                            {
                                "topic": 6,
                                "prob": 0.17857
                            },
                            {
                                "topic": 0,
                                "prob": 0.10714
                            },
                            {
                                "topic": 17,
                                "prob": 0.10714
                            }
                        ]
                    },
                    "40t_0,5a_0,005e": {
                        "number_of_topics": 40,
                        "alpha": 0.5,
                        "eta": 0.005,
                        "topics": [
                            {
                                "topic": 0,
                                "prob": 0.0625
                            },
                            {
                                "topic": 22,
                                "prob": 0.0625
                            },
                            {
                                "topic": 15,
                                "prob": 0.0625
                            },
                            {
                                "topic": 20,
                                "prob": 0.0625
                            }
                        ]
                    },
                    "5t_0,5a_0,01e": {
                        "number_of_topics": 5,
                        "alpha": 0.5,
                        "eta": 0.01,
                        "topics": [
                            {
                                "topic": 2,
                                "prob": 0.38462
                            },
                            {
                                "topic": 0,
                                "prob": 0.23077
                            },
                            {
                                "topic": 3,
                                "prob": 0.23077
                            }
                        ]
                    },
                    "10t_0,5a_0,01e": {
                        "number_of_topics": 10,
                        "alpha": 0.5,
                        "eta": 0.01,
                        "topics": [
                            {
                                "topic": 7,
                                "prob": 0.27778
                            },
                            {
                                "topic": 0,
                                "prob": 0.16667
                            },
                            {
                                "topic": 4,
                                "prob": 0.16667
                            }
                        ]
                    },
                    "20t_0,5a_0,01e": {
                        "number_of_topics": 20,
                        "alpha": 0.5,
                        "eta": 0.01,
                        "topics": [
                            {
                                "topic": 12,
                                "prob": 0.17857
                            },
                            {
                                "topic": 2,
                                "prob": 0.10714
                            },
                            {
                                "topic": 13,
                                "prob": 0.10714
                            }
                        ]
                    },
                    "40t_0,5a_0,01e": {
                        "number_of_topics": 40,
                        "alpha": 0.5,
                        "eta": 0.01,
                        "topics": [
                            {
                                "topic": 19,
                                "prob": 0.0625
                            },
                            {
                                "topic": 2,
                                "prob": 0.0625
                            },
                            {
                                "topic": 15,
                                "prob": 0.0625
                            },
                            {
                                "topic": 26,
                                "prob": 0.0625
                            }
                        ]
                    },
                    "5t_0,5a_0,05e": {
                        "number_of_topics": 5,
                        "alpha": 0.5,
                        "eta": 0.05,
                        "topics": [
                            {
                                "topic": 0,
                                "prob": 0.69231
                            }
                        ]
                    },
                    "10t_0,5a_0,05e": {
                        "number_of_topics": 10,
                        "alpha": 0.5,
                        "eta": 0.05,
                        "topics": [
                            {
                                "topic": 4,
                                "prob": 0.38889
                            },
                            {
                                "topic": 0,
                                "prob": 0.16667
                            }
                        ]
                    },
                    "20t_0,5a_0,05e": {
                        "number_of_topics": 20,
                        "alpha": 0.5,
                        "eta": 0.05,
                        "topics": [
                            {
                                "topic": 0,
                                "prob": 0.10714
                            },
                            {
                                "topic": 14,
                                "prob": 0.10714
                            },
                            {
                                "topic": 13,
                                "prob": 0.10714
                            },
                            {
                                "topic": 7,
                                "prob": 0.10714
                            }
                        ]
                    },
                    "40t_0,5a_0,05e": {
                        "number_of_topics": 40,
                        "alpha": 0.5,
                        "eta": 0.05,
                        "topics": [
                            {
                                "topic": 24,
                                "prob": 0.0625
                            },
                            {
                                "topic": 4,
                                "prob": 0.0625
                            },
                            {
                                "topic": 25,
                                "prob": 0.0625
                            },
                            {
                                "topic": 28,
                                "prob": 0.0625
                            }
                        ]
                    },
                    "5t_0,5a_0,1e": {
                        "number_of_topics": 5,
                        "alpha": 0.5,
                        "eta": 0.1,
                        "topics": [
                            {
                                "topic": 0,
                                "prob": 0.53846
                            },
                            {
                                "topic": 1,
                                "prob": 0.23077
                            }
                        ]
                    },
                    "10t_0,5a_0,1e": {
                        "number_of_topics": 10,
                        "alpha": 0.5,
                        "eta": 0.1,
                        "topics": [
                            {
                                "topic": 0,
                                "prob": 0.16667
                            },
                            {
                                "topic": 2,
                                "prob": 0.16667
                            },
                            {
                                "topic": 5,
                                "prob": 0.16667
                            },
                            {
                                "topic": 6,
                                "prob": 0.16667
                            }
                        ]
                    },
                    "20t_0,5a_0,1e": {
                        "number_of_topics": 20,
                        "alpha": 0.5,
                        "eta": 0.1,
                        "topics": [
                            {
                                "topic": 0,
                                "prob": 0.10714
                            },
                            {
                                "topic": 14,
                                "prob": 0.10714
                            },
                            {
                                "topic": 10,
                                "prob": 0.10714
                            },
                            {
                                "topic": 9,
                                "prob": 0.10714
                            }
                        ]
                    },
                    "40t_0,5a_0,1e": {
                        "number_of_topics": 40,
                        "alpha": 0.5,
                        "eta": 0.1,
                        "topics": [
                            {
                                "topic": 0,
                                "prob": 0.0625
                            },
                            {
                                "topic": 28,
                                "prob": 0.0625
                            },
                            {
                                "topic": 31,
                                "prob": 0.0625
                            },
                            {
                                "topic": 20,
                                "prob": 0.0625
                            }
                        ]
                    },
                    "5t_0,9a_0,005e": {
                        "number_of_topics": 5,
                        "alpha": 0.9,
                        "eta": 0.005,
                        "topics": [
                            {
                                "topic": 2,
                                "prob": 0.34118
                            },
                            {
                                "topic": 0,
                                "prob": 0.22353
                            },
                            {
                                "topic": 1,
                                "prob": 0.22353
                            }
                        ]
                    },
                    "10t_0,9a_0,005e": {
                        "number_of_topics": 10,
                        "alpha": 0.9,
                        "eta": 0.005,
                        "topics": [
                            {
                                "topic": 7,
                                "prob": 0.22308
                            },
                            {
                                "topic": 1,
                                "prob": 0.14615
                            },
                            {
                                "topic": 5,
                                "prob": 0.14615
                            }
                        ]
                    },
                    "20t_0,9a_0,005e": {
                        "number_of_topics": 20,
                        "alpha": 0.9,
                        "eta": 0.005,
                        "topics": [
                            {
                                "topic": 9,
                                "prob": 0.13182
                            },
                            {
                                "topic": 11,
                                "prob": 0.08636
                            },
                            {
                                "topic": 0,
                                "prob": 0.08636
                            }
                        ]
                    },
                    "40t_0,9a_0,005e": {
                        "number_of_topics": 40,
                        "alpha": 0.9,
                        "eta": 0.005,
                        "topics": [
                            {
                                "topic": 0,
                                "prob": 0.0475
                            },
                            {
                                "topic": 32,
                                "prob": 0.0475
                            },
                            {
                                "topic": 27,
                                "prob": 0.0475
                            },
                            {
                                "topic": 28,
                                "prob": 0.0475
                            }
                        ]
                    },
                    "5t_0,9a_0,01e": {
                        "number_of_topics": 5,
                        "alpha": 0.9,
                        "eta": 0.01,
                        "topics": [
                            {
                                "topic": 2,
                                "prob": 0.34118
                            },
                            {
                                "topic": 0,
                                "prob": 0.22353
                            },
                            {
                                "topic": 1,
                                "prob": 0.22353
                            }
                        ]
                    },
                    "10t_0,9a_0,01e": {
                        "number_of_topics": 10,
                        "alpha": 0.9,
                        "eta": 0.01,
                        "topics": [
                            {
                                "topic": 1,
                                "prob": 0.22308
                            },
                            {
                                "topic": 2,
                                "prob": 0.14615
                            },
                            {
                                "topic": 5,
                                "prob": 0.14615
                            }
                        ]
                    },
                    "20t_0,9a_0,01e": {
                        "number_of_topics": 20,
                        "alpha": 0.9,
                        "eta": 0.01,
                        "topics": [
                            {
                                "topic": 10,
                                "prob": 0.13182
                            },
                            {
                                "topic": 0,
                                "prob": 0.08636
                            },
                            {
                                "topic": 14,
                                "prob": 0.08636
                            }
                        ]
                    },
                    "40t_0,9a_0,01e": {
                        "number_of_topics": 40,
                        "alpha": 0.9,
                        "eta": 0.01,
                        "topics": [
                            {
                                "topic": 1,
                                "prob": 0.0475
                            },
                            {
                                "topic": 22,
                                "prob": 0.0475
                            },
                            {
                                "topic": 23,
                                "prob": 0.0475
                            },
                            {
                                "topic": 28,
                                "prob": 0.0475
                            }
                        ]
                    },
                    "5t_0,9a_0,05e": {
                        "number_of_topics": 5,
                        "alpha": 0.9,
                        "eta": 0.05,
                        "topics": [
                            {
                                "topic": 0,
                                "prob": 0.22353
                            },
                            {
                                "topic": 1,
                                "prob": 0.22353
                            },
                            {
                                "topic": 2,
                                "prob": 0.22353
                            },
                            {
                                "topic": 3,
                                "prob": 0.22353
                            }
                        ]
                    },
                    "10t_0,9a_0,05e": {
                        "number_of_topics": 10,
                        "alpha": 0.9,
                        "eta": 0.05,
                        "topics": [
                            {
                                "topic": 8,
                                "prob": 0.3
                            },
                            {
                                "topic": 1,
                                "prob": 0.14615
                            }
                        ]
                    },
                    "20t_0,9a_0,05e": {
                        "number_of_topics": 20,
                        "alpha": 0.9,
                        "eta": 0.05,
                        "topics": [
                            {
                                "topic": 0,
                                "prob": 0.08636
                            },
                            {
                                "topic": 14,
                                "prob": 0.08636
                            },
                            {
                                "topic": 12,
                                "prob": 0.08636
                            },
                            {
                                "topic": 7,
                                "prob": 0.08636
                            }
                        ]
                    },
                    "40t_0,9a_0,05e": {
                        "number_of_topics": 40,
                        "alpha": 0.9,
                        "eta": 0.05,
                        "topics": [
                            {
                                "topic": 30,
                                "prob": 0.0725
                            },
                            {
                                "topic": 0,
                                "prob": 0.0475
                            },
                            {
                                "topic": 36,
                                "prob": 0.0475
                            }
                        ]
                    },
                    "5t_0,9a_0,1e": {
                        "number_of_topics": 5,
                        "alpha": 0.9,
                        "eta": 0.1,
                        "topics": [
                            {
                                "topic": 3,
                                "prob": 0.45882
                            },
                            {
                                "topic": 1,
                                "prob": 0.22353
                            }
                        ]
                    },
                    "10t_0,9a_0,1e": {
                        "number_of_topics": 10,
                        "alpha": 0.9,
                        "eta": 0.1,
                        "topics": [
                            {
                                "topic": 4,
                                "prob": 0.22308
                            },
                            {
                                "topic": 0,
                                "prob": 0.14615
                            },
                            {
                                "topic": 5,
                                "prob": 0.14615
                            }
                        ]
                    },
                    "20t_0,9a_0,1e": {
                        "number_of_topics": 20,
                        "alpha": 0.9,
                        "eta": 0.1,
                        "topics": [
                            {
                                "topic": 0,
                                "prob": 0.08636
                            },
                            {
                                "topic": 17,
                                "prob": 0.08636
                            },
                            {
                                "topic": 12,
                                "prob": 0.08636
                            },
                            {
                                "topic": 10,
                                "prob": 0.08636
                            }
                        ]
                    },
                    "40t_0,9a_0,1e": {
                        "number_of_topics": 40,
                        "alpha": 0.9,
                        "eta": 0.1,
                        "topics": [
                            {
                                "topic": 32,
                                "prob": 0.0725
                            },
                            {
                                "topic": 2,
                                "prob": 0.0475
                            },
                            {
                                "topic": 23,
                                "prob": 0.0475
                            }
                        ]
                    }
                }
            }
        }



@app.post("/", response_description="Add new phrase", response_model=PhraseModel)
async def create_phrase(phrase: PhraseModel = Body(...)):
    phrase = jsonable_encoder(phrase)
    new_phrase = await db1["phrases"].insert_one(phrase)
    created_phrase = await db1["phrases"].find_one({"_id": new_phrase.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_phrase)


@app.get(
    "/", response_description="List all phrases", response_model=List[PhraseModel]
) 
async def list_phrases(skip: int = 0, limit: int = 10):
    phrases = await db1["phrases"].find(skip=skip).to_list(limit)
    return phrases


@app.get(
    "/{id}", response_description="Get a single phrase", response_model=PhraseModel
)
async def show_phrase(id: int):
    if (phrase := await db1["phrases"].find_one({"_id": id})) is not None:
        return phrase

    raise HTTPException(status_code=404, detail=f"phrase {id} not found")


@app.put("/{id}", response_description="Update a phrase", response_model=PhraseModel)
async def update_phrase(id: int, phrase: UpdatePhraseModel = Body(...)):
    phrase = {k: v for k, v in phrase.dict().items() if v is not None}

    if len(phrase) >= 1:
        update_result = await db1["phrases"].update_one({"_id": id}, {"$set": phrase})

        if update_result.modified_count == 1:
            if (
                updated_phrase := await db1["phrases"].find_one({"_id": id})
            ) is not None:
                return updated_phrase

    if (existing_phrase := await db1["phrases"].find_one({"_id": id})) is not None:
        return existing_phrase

    raise HTTPException(status_code=404, detail=f"phrase {id} not found")


@app.delete("/{id}", response_description="Delete a phrase")
async def delete_phrase(id: str):
    delete_result = await db1["phrases"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"phrase {id} not found")
