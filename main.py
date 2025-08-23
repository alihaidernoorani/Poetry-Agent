from agents import Agent, Runner
from connection import config
from dotenv import load_dotenv
import asyncio

load_dotenv()

lyric_agent = Agent(
    name="Lyric Agent",
    instructions="You are a lyric agent. Your task is to analyze only lyric poetry."
)

narrative_agent = Agent(
    name="Narrative Agent",
    instructions="You are a narrative agent. Your task is to analyze any analyze only narrative poetry."
)

dramatic_agent = Agent(
    name="Dramatic Agent",
    instructions="You are a dramatic agent. Your task is to analyze only dramatic poetry."
)

triage_agent = Agent(
    name="Triage Agent",
    instructions="""
    You are the triage agent. Your job is to carefully read the poem provided by the user and decide which type of poetry it belongs to:
    - Lyric poetry: Focuses on personal emotions, feelings, or moods.
    - Narrative poetry: Tells a story with characters, events, or a plot.
    - Dramatic poetry: Written as a speech or monologue, meant to be performed.

    Steps to follow:
    1. Read the poem carefully.
    2. Decide whether it is Lyric, Narrative, or Dramatic poetry.
    3. If it clearly fits one of these categories:
    - Handoff to the correct analyst agent:
        * Narrative → Narrative Agent
        * Lyric → Lyric Agent
        * Dramatic → Dramatic Agent
    4. If the poem does NOT fit any of the above categories, ask the user to provide a valid type of poetry before proceeding.

    Only one handoff should occur per poem.
    """,
    handoffs=[narrative_agent, lyric_agent, dramatic_agent]
)

async def main():
    result = await Runner.run(
        triage_agent,
        input=""" 
        A boy once found, beside the shore,
        A lantern washed from days of yore.
        Its glass was cracked, its flame was dim,
        But something in it beckoned him.

        He lit the wick with trembling hand,
        And saw a path not made of sand—
        It shimmered through the midnight fog,
        A silver trail across the bog.

        He followed deep where no one dared,
        Through whispering winds that no one heard.
        At journey's end, a voice so low:
        "Return the light, and you may go."

        He placed the lamp upon a stone—
        It flared once bright, then left him lone.
        He walked back home with empty palms,
        But in his heart, a thousand psalms.
        """,
        run_config=config
    )

    print(result.final_output)


if __name__ == "__main__":
   asyncio.run(main())
