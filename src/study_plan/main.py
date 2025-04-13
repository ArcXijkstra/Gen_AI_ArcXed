#!/usr/bin/env python
from random import randint

from pydantic import BaseModel

from crewai.flow import Flow, listen, start
import warnings
warnings.filterwarnings("ignore", category=SyntaxWarning)
from study_plan.crews.question_generate.question_generate import QuestionGenerate
from study_plan.crews.study_plan.study_plan import StudyPlan


class PoemState(BaseModel):
    sentence_count: int = 1
    poem: str = ""


class PoemFlow(Flow[PoemState]):

    @start()
    def generate_poem(self):
        current_level = [
        {
            "Subject": "English",
            "Chapters": {
            "Reading Passage": 7,
            "Grammar": 8,
            "Vocabulary": 5,
            "Phonemes and Stress": 3
            }
        },
        {
            "Subject": "Maths",
            "Chapters": {
            "Set and Function": 6,
            "Algebra": 8,
            "Trigonometry": 5,
            "Coordinate Geometry": 7,
            "Calculus": 4,
            "Vectors": 3
            }
        },
        {
            "Subject": "Physics",
            "Chapters": {
            "Mechanics": 6,
            "Heat and Thermodynamics": 5,
            "Wave and Optics": 7,
            "Electricity and Magnetism": 4,
            "Modern Physics and Electronics": 3
            }
        },
        {
            "Subject": "Chemistry",
            "Chapters": {
            "Physical Chemistry": 6,
            "Inorganic Chemistry": 4,
            "Organic Chemistry": 3
            }
        }
        ]
        syllabus =[
                {"Subject": "English",
        "Total_marks": 22,
        "Number_of_questions": 18,
        "Chapters":{
            "Reading Passage":{"mark1":0, "mark2":4},
            "Grammar":{"mark1":10, "mark2":0},
            "Vocabulary":{"mark1":2, "mark2":0},
            "Phonemes and Stress":{"mark1":2, "mark2":0}
            }
        },
        {
            "Subject": "Maths",
            "Total_marks": 50,
            "Number_of_questions": 25, 
            "Chapters":{
                "Set and Function":{"mark1":1, "mark2":1},
                "Algebra":{"mark1":2, "mark2":4},
                "Trigonometry":{"mark1":1, "mark2":2},
                "Coordinate Geometry":{"mark1":2, "mark2":4},
                "Calculus":{"mark1":3, "mark2":4},
                "Vectors": {"mark1":1, "mark2":1}
            }
        },
        {
            "Subject": "Physics",
            "Total_marks": 40,
            "Number_of_questions": 25,
            "Chapters":{
                "Mechanics":{"mark1":2, "mark2":4},
                "Heat and Thermodynamics":{"mark1":2, "mark2":1},
                "Wave and Optics":{"mark1":2, "mark2":3},
                "Electricity and Magnetism":{"mark1":2, "mark2":4},
                "Modern Physics and Electronics":{"mark1":2, "mark2":3}
            }
        },
        {
            "Subject": "Chemistry",
            "Total_marks": 20,
            "Number_of_questions": 16,
            "Chapters":{
                "Physical Chemistry":{"mark1":6, "mark2":3},
                "Inorganic Chemistry":{"mark1":3, "mark2":1},
                "Organic Chemistry":{"mark1":3, "mark2":0}
            }
        }]
        questions = [
                {
                    "subject": "Chemistry",
                    "question": "What is the difference between physical and chemical adsorption? Give an example of each.",
                    "answer": "Physical adsorption is when gas particles are absorbed on a surface due to chemical bonds. Chemical adsorption happens due to physical forces like van der Waals. An example of physical is hydrogen on platinum. I might be mixing it though."
                },
                {
                    "subject": "Chemistry",
                    "question": "How does the rate of a reaction vary with temperature? Explain using the Arrhenius equation.",
                    "answer": "When temperature increases, the reaction becomes slower because molecules move more. Arrhenius equation is something like k = A + Ea/RT, but I don’t remember how it works exactly."
                },
                {
                    "subject": "Physics",
                    "question": "Explain how a transformer works. Why can’t it be used with direct current?",
                    "answer": "Transformer increases or decreases voltage using copper wires. It can't work with DC because DC has low voltage. I think AC is better because it's faster or something."
                },
                {
                    "subject": "Physics",
                    "question": "Calculate the potential energy stored in a capacitor of 10 μF charged to 100 V.",
                    "answer": "I used U = CV². So 10 × 100² = 100000. I think the energy is 100000 joules, not sure if I need to divide by 2."
                },
                {
                    "subject": "Maths",
                    "question": "If f(x) = sin(x^2), find f'(x) using the chain rule.",
                    "answer": "f'(x) = cos(x^2) × 2. I think the derivative of x² is 2 and we multiply with cos, but not totally sure about the order."
                },
                {
                    "subject": "Maths",
                    "question": "Find the area under the curve y = x^2 from x = 1 to x = 3.",
                    "answer": "I added the values: 1² + 2² + 3² = 14. So area is 14 units². That’s how area works, right?"
                },
                {
                    "subject": "English",
                    "question": "Identify the main clause and subordinate clause in the sentence: 'The boy, who was wearing a red cap, ran across the field.'",
                    "answer": "Subordinate clause: 'The boy ran across the field'. Main clause: 'who was wearing a red cap'. I get confused sometimes with these."
                },
                {
                    "subject": "English",
                    "question": "Choose the correct stress pattern for the word 'photograph' and use it in a sentence.",
                    "answer": "I think the stress is on 'graph' like pho-TO-GRAPH. My sentence: 'I took a photograph in the morning'. But not sure about the stress part."
                }
                ]
        
        
            
        print("Generating poem")
        result = (
            QuestionGenerate()
            .crew()
            .kickoff(inputs={"current_level": current_level,
                             "syllabus": syllabus,})
        )
        question_generated = result.tasks_output[0].pydantic
        
        results2 = (
            StudyPlan()
            .crew()
            .kickoff(inputs={"current_level": current_level,
                             "questions": questions,
                             "syllabus": syllabus})
        )
        print("Poem generated", result.raw)
        self.state.poem = result.raw

    


def kickoff():
    poem_flow = PoemFlow()
    poem_flow.kickoff()


def plot():
    poem_flow = PoemFlow()
    poem_flow.plot()


if __name__ == "__main__":
    flow = PoemFlow()
    flow.generate_poem()
