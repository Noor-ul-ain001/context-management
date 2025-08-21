# 3. LIBRARY BOOK CONTEXT
# library_book = LibraryBook(
#     book_id="BOOK-123",
#     book_title="Python Programming",
#     author_name="John Smith",
#     is_available=True
# )


import asyncio
from connection import config
from agents import Agent, RunContextWrapper, Runner, function_tool
from pydantic import BaseModel
import rich

class LibraryBook(BaseModel):
    book_id: str
    book_title: str
    author_name: str
    is_available: bool

library_book = LibraryBook(
    book_id="BOOK-123",
    book_title="Python Programming",
    author_name="John Smith",
    is_available=True
)

@function_tool
def get_book_details(wrapper: RunContextWrapper[LibraryBook]):
    return f'Book: {wrapper.context.book_title}, Author: {wrapper.context.author_name}'

library_agent = Agent(
    name="LibraryAgent",
    instructions="You are a helpful assistant, always call the tool to get library book information",
    tools=[get_book_details]
)

async def main():
    result = await Runner.run(
        library_agent,
        'Is the book available?',
        run_config=config,
        context=library_book
    )
    rich.print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
