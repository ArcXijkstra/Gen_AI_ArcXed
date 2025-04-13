from pydantic import BaseModel, Field
from typing import List

# -------------------------- Question Generator Output --------------------------

class ChapterQuestion(BaseModel):
    chapter: str = Field(..., example="Algebra", description="Chapter name")
    questions: List[str] = Field(
        ..., 
        min_items=2, 
        max_items=2,
        example=[
            "Explain the concept of completing the square.",
            "Describe a real-life application of quadratic equations."
        ],
        description="Two conceptual questions from the chapter."
    )

class SubjectQuestionSet(BaseModel):
    subject: str = Field(..., example="Maths", description="The name of the subject.")
    chapter_questions: List[ChapterQuestion] = Field(
        ..., 
        description="Two conceptual questions per chapter within the subject."
    )

class QuestionGeneratorOutput(BaseModel):
    diagnostic_questions: List[SubjectQuestionSet] = Field(
        ..., 
        description="List of subjects with 2 conceptual questions per chapter."
    )

# -------------------------- Answer Evaluation Output --------------------------

class SubjectScore(BaseModel):
    subject: str = Field(..., example="Physics", description="The name of the subject")
    score: int = Field(..., ge=0, le=10, example=6, description="Overall subject-level score (0–10)")

class AnswerEvaluationOutput(BaseModel):
    evaluated_understanding: List[SubjectScore] = Field(
        ..., 
        description="List of subject-level evaluated understanding scores."
    )

# -------------------------- Study Plan Output --------------------------
class ChapterStudyRecommendation(BaseModel):
    chapter: str = Field(..., example="Algebra", description="Chapter name.")
    priority: str = Field(..., example="High", description="Study priority: High, Medium, or Low.")
    tip: str = Field(..., example="Focus on conceptual clarity through solved examples.", description="Short actionable tip.")
    time_to_study_per_week: str = Field(..., example="2 hours", description="Recommended weekly time to spend on this chapter.")
    user_confidence: str = Field(..., example="Low", description="Confidence level of the user in this chapter: High, Medium, or Low.")
    recommended_mode: str = Field(..., example="Conceptual practice with examples", description="Suggested study mode for this chapter.")
    revise_by: str = Field(..., example="2024-05-01", description="Deadline or recommended date to complete revision.")
    learning_goals: List[str] = Field(
        ..., 
        example=["Understand integration techniques", "Solve 5 real-world application problems"],
        description="Clear goals for the user to achieve in this chapter."
    )
    resources: List[str] = Field(
        ..., 
        example=["https://www.khanacademy.org/math", "https://youtu.be/exampleVideo"],
        description="Links to recommended videos or study resources."
    )

class SubjectStudyPlan(BaseModel):
    subject: str = Field(..., example="Maths", description="Subject name.")
    chapters: List[ChapterStudyRecommendation] = Field(
        ..., 
        description="Enhanced chapter-wise personalized plan."
    )

class StudyPlanOutput(BaseModel):
    study_plan: List[SubjectStudyPlan] = Field(
        ..., 
        description="Personalized study plan with detailed guidance per chapter."
    )