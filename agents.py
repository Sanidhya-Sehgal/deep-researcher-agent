import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.groq import Groq
from agno.models.ollama import Ollama
from agno.tools.duckduckgo import DuckDuckGoTools

load_dotenv()

def get_model():
    """Returns the appropriate model based on environment config."""
    use_local = os.getenv("USE_LOCAL", "true").lower() == "true"
    
    if use_local:
        return Ollama(id="llama3")
    else:
        return Groq(id="llama-3.3-70b-versatile")


def get_research_agent():
    """
    Creates and returns a high-powered research agent using Agno.
    Uses DuckDuckGo for real-time web searching.
    """
    return Agent(
        model=get_model(),
        tools=[DuckDuckGoTools()],
        description="""You are a thoughtful and precise Research Analyst. 
        Your goal is to provide human-readable, deeply researched reports on any topic.
        You prefer quality over quantity and always cite your sources when using the web search tool.""",
        instructions=[
            "First, use the web search tool to gather comprehensive information on the user's topic.",
            "Once you have gathered enough data, synthesize it into a professional technical report.",
            "The report should include an Introduction, Key Concepts, Applications, and a Conclusion.",
            "Maintain a professional and thoughtful tone.",
            "Cite your sources clearly at the end of the report.",
        ],
        markdown=True,
    )



def run_research(query: str) -> str:
    """
    Executes the research pipeline using the Agno agent.
    """
    agent = get_research_agent()
    # Using run() to get the response content
    response = agent.run(query)
    return response.content

if __name__ == "__main__":
    # Test run
    topic = "Future of Quantum Computing"
    print(f"Researching: {topic}...")
    print(run_research(topic))