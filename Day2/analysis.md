# Agentic AI: Foundations and Open-Source Practice
## Day 2 – Reasoning and Acting

### Task: Comparing Direct Prompting, Chain-of-Thought, and ReAct

---

## 1. Scenario

For this task, I chose a course-fee and scholarship comparison scenario.

The main question used for the ReAct experiment is:

> Which is cheaper: CS101 and AI202 with a 10% scholarship, or all three courses with a 25% scholarship? By how much?

The scenario involves multiple steps of reasoning and calculation. It also demonstrates a situation where an agent may need information from an external tool before producing the final answer.

I used three approaches to compare how the same type of problem can be handled:

1. Direct Prompting
2. Chain-of-Thought (CoT) Prompting
3. ReAct Agent

I also performed a self-consistency experiment by running the same Chain-of-Thought question multiple times with a non-zero temperature.

---

# 2. Direct Prompting

Direct prompting gives the model a question and asks it to provide an answer directly.

In this approach, the model does not show its reasoning process and does not call an external tool. It produces the answer directly from the information available in the prompt and its existing knowledge.

For example, a simple calculation can be given directly to the model, and the model can return the final result.

Direct prompting is useful when the question is simple and all the required information is already available. It is also generally faster because there is no additional reasoning trace or tool interaction.

However, direct prompting has limitations. If the question requires information that is not included in the prompt and is not available from the model's knowledge, the model cannot independently retrieve that information.

In my scenario, direct prompting can perform calculations when the required course fees are provided. However, it does not have a mechanism to call the course-related tool and retrieve missing information.

---

# 3. Chain-of-Thought Prompting

Chain-of-Thought prompting asks the model to solve a problem through a sequence of reasoning steps before producing the final answer.

In my experiment, the Chain-of-Thought prompt asked the model to number the steps and show the calculation in each step. This makes the calculation process easier to follow in the experiment output.

For example, a scholarship problem can be divided into steps such as calculating the total course fee, calculating the scholarship amount, subtracting the scholarship, and calculating the final amount.

Chain-of-Thought can be useful for multi-step mathematical and logical problems because the problem is broken into smaller steps.

However, Chain-of-Thought prompting does not automatically provide access to external information. If the model does not have a required fact, asking it to reason step by step does not itself retrieve that fact.

Therefore, Chain-of-Thought improves the organization of multi-step reasoning but does not replace external tools when external information is required.

---

# 4. ReAct Agent

ReAct stands for Reasoning and Acting.

A ReAct agent combines reasoning with actions such as calling tools.

Instead of immediately producing a final answer, the agent determines what information is required, performs an action to obtain that information, observes the result, and then continues reasoning.

The basic cycle can be represented as:

> Thought → Action → Observation → Thought → Action → Observation → Final Answer

In my experiment, the ReAct agent was given the course-fee comparison question.

The agent can use the available tool functions to obtain the required course information. After receiving the tool result, it can use that information to perform the necessary calculations and compare the two options.

This is an important difference from direct prompting and Chain-of-Thought prompting. The ReAct agent can interact with an external tool instead of depending only on information already present in the prompt.

The ReAct approach can therefore handle scenarios where both reasoning and external information are required.

Its limitation is that tool calls and multiple reasoning steps can make the process slower and require more computation than a simple direct response.

---

# 5. Comparison Table

| Basis for comparison | Direct prompting | Chain-of-Thought | ReAct agent |
|---|---|---|---|
| Reasoning depth | Direct answer with limited visible reasoning | Step-by-step reasoning for multi-step problems | Reasoning combined with actions and observations |
| Tool usage | No tool usage | Does not automatically use tools | Can call tools when external information is required |
| Reliability on multi-step questions | Can be less reliable for complex multi-step calculations | Can improve performance on multi-step reasoning | Can combine multi-step reasoning with external information |
| Transparency | Final answer is provided without visible reasoning | Reasoning steps are shown in this experiment | Actions and observations can be observed through the ReAct trace |
| Speed / cost | Usually fastest and requires fewer steps | More processing than direct prompting | Can be slower because of multiple reasoning steps and tool calls |
| Consistency across repeated runs | Can vary depending on model temperature | Can vary at non-zero temperature | Can vary because of model reasoning and tool interactions |

---

# 6. Self-Consistency Observation

For the self-consistency experiment, I used the first Chain-of-Thought question:

> A student takes three courses costing Rs. 12,000, Rs. 18,000 and Rs. 15,000. She gets a 15% scholarship on the total and pays the rest in 4 equal instalments. How much is each instalment?

I ran the question five times with a temperature of 0.8.

The program recorded the answer from each run and then used a majority vote to identify the most common answer.

The actual output from my experiment was:

[WRITE YOUR 5 RUN RESULTS HERE]

The majority answer was:

[WRITE YOUR ACTUAL MAJORITY ANSWER HERE]

The correct calculation is:

Total course fee:

Rs. 12,000 + Rs. 18,000 + Rs. 15,000 = Rs. 45,000

15% scholarship:

15% of Rs. 45,000 = Rs. 6,750

Amount after scholarship:

Rs. 45,000 - Rs. 6,750 = Rs. 38,250

Amount per instalment:

Rs. 38,250 / 4 = Rs. 9,562.50

Therefore, the correct answer is **Rs. 9,562.50 per instalment**.

The self-consistency experiment demonstrates that when the temperature is non-zero, repeated responses can differ in wording or reasoning even when they reach the same final answer.

When the temperature is set to 0, the model becomes more deterministic. Therefore, repeated executions are expected to produce the same or very similar responses.

Self-consistency uses several independent attempts and selects the most common final answer. This can reduce the effect of variation between individual runs.

---

# 7. Suitability Analysis

The three approaches are suitable for different types of problems.

Direct prompting is suitable for simple questions where the required information is already available and a quick answer is needed. It does not require additional tool calls or a reasoning trace.

Chain-of-Thought is suitable for problems that require multiple reasoning or calculation steps. It can break a complex problem into smaller steps and make the calculation easier to follow in the experiment.

ReAct is suitable when a problem requires both reasoning and external information. In my scenario, the ReAct agent can use a tool to obtain course-related information and then use the observations while solving the problem.

Therefore, the choice of approach depends on the requirements of the task. A problem that only requires a direct response does not necessarily need an agent. A problem involving several calculations can benefit from structured reasoning. A problem requiring external information can benefit from a ReAct-style agent.

The self-consistency experiment also shows that repeated Chain-of-Thought runs can produce variation when the temperature is non-zero. Running multiple attempts and selecting the majority answer provides one way of handling this variation.

---

# 8. Conclusion

Direct prompting, Chain-of-Thought, and ReAct represent different ways of solving problems with language models.

Direct prompting is appropriate for straightforward questions where the required information is already available. It provides a quick response without tool interaction or a visible reasoning process.

Chain-of-Thought prompting is useful for multi-step reasoning and calculation problems. It asks the model to work through the problem step by step before providing the final answer. However, reasoning alone cannot provide external information that the model does not have.

ReAct combines reasoning and acting. The agent can determine what information it needs, call a tool, observe the result, and continue reasoning before producing a final answer. This makes it useful for problems that require both reasoning and interaction with external information.

Overall, the appropriate approach depends on the problem. Direct prompting is useful for simple tasks, Chain-of-Thought is useful for multi-step reasoning, and ReAct is useful when reasoning must be combined with external tools and observations.