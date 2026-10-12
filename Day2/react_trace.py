"""Day 2, Part D: print the agent's real ReAct trace to compare with your paper trace."""

import sys

# Add Day 1 folder so Python can find agent.py
sys.path.insert(0, r"..\day1-AI fluency")

from agent import agent


QUESTION = (
    "Which is cheaper: CS101 and AI202 with a 10% scholarship, "
    "or all three courses with a 25% scholarship? By how much?"
)


print("QUESTION:", QUESTION, "\n")
print("--- the agent's actions and observations ---")


answer = agent(QUESTION, max_steps=8)


print("\nFINAL ANSWER:", answer)