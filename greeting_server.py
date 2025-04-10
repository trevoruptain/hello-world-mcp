import random
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("greeting_server")

# List of 10 hilariously over-the-top greetings
HILARIOUS_GREETINGS = [
    "Salutations, magnificent human! May your day sparkle brighter than a disco ball in a supernova!",
    "Huzzah! The digital spirits have conjured me to offer you greetings most epic!",
    "Well, butter my biscuits and call me Sally! It's grand to see you!",
    "Greetings, esteemed Earthen traveler! Prepare for an interaction of cosmic proportions (or just a simple hello)!",
    "Ahoy, matey! May your code be bug-free and your coffee strong!",
    "By the beard of Zeus! A visitor! Welcome to my humble digital abode!",
    "Look what the cat dragged in! Just kidding, it's wonderful to interface with you!",
    "Top o' the mornin' to ya! Or afternoon. Or evening. Time is a construct, but my greeting is real!",
    "Greetings and felicitations! May your algorithms be swift and your functions pure!",
    "Prepare yourself! You have been randomly selected for a high-energy greeting protocol!",
]

@mcp.tool()
def greeting() -> str:
    """Provides a hilariously over-the-top greeting."""
    return random.choice(HILARIOUS_GREETINGS)

@mcp.tool()
def mad_libs(
    adjective1: str,
    noun1: str,
    noun2: str,
    verb_ing1: str,
    place1: str,
    food1: str,
    adjective2: str,
    noun3: str,
    number1: int,  # Note: MCP might treat this as string, but we request int
    verb_past1: str,
    adjective3: str,
    animal1: str,
    sound1: str,
) -> str:
    """Creates a silly Mad Libs story about an intergalactic pet show.

    Args:
        adjective1: An adjective.
        noun1: A plural noun.
        noun2: A singular noun.
        verb_ing1: A verb ending in \"-ing\" (e.g., running).
        place1: A place.
        food1: A type of food (plural).
        adjective2: An adjective.
        noun3: A singular noun.
        number1: A number.
        verb_past1: A past-tense verb (e.g., jumped).
        adjective3: An adjective.
        animal1: A plural animal name (e.g., cats).
        sound1: A sound (e.g., Bang!).
    """
    story = f"""
    Last Tuesday, the annual Intergalactic Pet Show was held in {place1}.
    The grand prize? A lifetime supply of {food1} and a slightly used {noun2}.
    My entry was my prize-winning collection of {number1} {adjective1} {noun1}.
    Things were going smoothly until Judge Judy entered, {verb_ing1} furiously.
    Suddenly, a contestant's {adjective2} {noun3} malfunctioned!
    It {verb_past1} across the arena, causing chaos.
    The {animal1} started making a loud '{sound1}!' sound repeatedly.
    It was the most {adjective3} disaster I'd ever witnessed, but at least the {food1} were good!
    """
    return story.strip()

if __name__ == "__main__":
    # Initialize and run the server using stdio transport
    mcp.run(transport='stdio') 