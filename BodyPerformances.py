from pydantic import BaseModel


class BodyPerformance(BaseModel):
    age: int
    gender: int
    height: float
    weight: float
    body_fat: float
    diastolic: float
    systolic: float
    gripForce: float
    ben_forward: float
    sit_up_counts: int
    broad_jump: float
