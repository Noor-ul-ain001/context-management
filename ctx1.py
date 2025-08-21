# bank_account = BankAccount(
#     account_number="ACC-789456",
#     customer_name="Fatima Khan",
#     account_balance=75500.50,
#     account_type="savings"
# )

import asyncio
from connection import config
from agents import Agent, RunContextWrapper, Runner, function_tool
from pydantic import BaseModel
import rich

class BankInfo(BaseModel):
    account_number: str
    customer_name: str
    account_balance: int | float
    account_type: str
    
bank_info = BankInfo (
     account_number="ACC-789456",
     customer_name="Fatima Khan",
     account_balance=75500.50,
     account_type="savings"
    )  

@function_tool
def get_bank_details(wrapper: RunContextWrapper[BankInfo]) :
    return f'The user info is {wrapper.context}'



personal_agent = Agent(
    name = "Agent",
    instructions="You are a helpful assistant, always call the tool to get user's account information",
    tools=[get_bank_details]
)

async def main():
    result = await Runner.run(
        personal_agent,  
        'What is my account number, customer  number account balance', 
        run_config=config,
        context = bank_info 
        )
    rich.print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
