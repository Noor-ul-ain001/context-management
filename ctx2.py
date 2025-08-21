# student = StudentProfile(
#     student_id="STU-456",
#     student_name="Hassan Ahmed",
#     current_semester=4,
#     total_courses=5
# )

import asyncio
from connection import config
from agents import Agent, RunContextWrapper, Runner, function_tool
from pydantic import BaseModel
import rich

class StudentProfile(BaseModel):
    student_id: str
    student_name: str
    current_semester: int
    total_courses: int

student_profile = StudentProfile(
    student_id="STU-456",
    student_name="Hassan Ahmed",
    current_semester=4,
    total_courses=5
)

@function_tool
def get_student_details(wrapper: RunContextWrapper[StudentProfile]):
    return f'Student Name: {wrapper.context.student_name}, Semester: {wrapper.context.current_semester}, Courses: {wrapper.context.total_courses}'

student_agent = Agent(
    name="StudentAgent",
    instructions="You are a helpful assistant, always call the tool to get the student's profile information",
    tools=[get_student_details]
)

async def main():
    result = await Runner.run(
        student_agent,
        'What is student name ,student id,  my current semester and total courses?',
        run_config=config,
        context=student_profile
    )
    rich.print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
