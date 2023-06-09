# Some bits of theory

## Intro

The dog wigged it's {...} ? [pen, CPU, AI, screen, tail?]<br>
Ok, not only you just got the intutition of what an LLM is, but you also proved that your brain behaves like one :yum:

## What is an ambiguous prompt ? (Or called "one-shot prompt")

We can describe zero shot prompting by describing what it lacks:

1.  You don't give directions (in this order) such as:

- Instructions (Summarize, Complete, Translate, Answer, Write)
- Context (Length, language, question, theme)
- Input data
- Output indicator (Data format for example)

2. Model is guessing at its best effort without you giving an example


Provide guidance: <br>
**Ex**: I want a list of random monument names as an output, in this format => [apple, tree, banana]

Zero shot prompting is therefore inefficient. The probability of "hallucinations" will increase.

<br>

Here, the model get's **guidance**. <br><br>

# Advanced *Prompt Engineering* to implement more autonomous agents and increase the LLM's output's accuracy

##  Chain of Thought Prompting

*We explore how generating a chain of thought—a series of intermediate reasoning
steps—significantly improves the ability of large language models to perform
complex reasoning. In particular, we show how such reasoning abilities emerge
naturally in sufficiently large language models via a simple method called chain-ofthought prompting, where a few chain of thought demonstrations are provided as
exemplars in prompting.
Experiments on three large language models show that chain-of-thought prompting
improves performance on a range of arithmetic, commonsense, and symbolic
reasoning tasks. The empirical gains can be striking. For instance, prompting a
PaLM 540B with just eight chain-of-thought exemplars achieves state-of-the-art
accuracy on the GSM8K benchmark of math word problems, surpassing even
finetuned GPT-3 with a verifier.*

See: https://arxiv.org/pdf/2201.11903.pdf
<br>

## ReAct

"*While large language models (LLMs) have demonstrated impressive capabilities across tasks in language understanding and interactive decision making, their abilities for reasoning (e.g. chain-of-thought prompting) and acting (e.g. action plan generation) have primarily been studied as separate topics. In this paper, we explore the use of LLMs to generate both reasoning traces and task-specific actions in an interleaved manner, allowing for greater synergy between the two: reasoning traces help the model induce, track, and update action plans as well as handle exceptions, while actions allow it to interface with external sources, such as knowledge bases or environments, to gather additional information. We apply our approach, named ReAct, to a diverse set of language and decision making tasks and demonstrate its effectiveness over state-of-the-art baselines, as well as improved human interpretability and trustworthiness over methods without reasoning or acting components. Concretely, on question answering (HotpotQA) and fact verification (Fever), ReAct overcomes issues of hallucination and error propagation prevalent in chain-of-thought reasoning by interacting with a simple Wikipedia API, and generates human-like task-solving trajectories that are more interpretable than baselines without reasoning traces. On two interactive decision making benchmarks (ALFWorld and WebShop), ReAct outperforms imitation and reinforcement learning methods by an absolute success rate of 34% and 10% respectively, while being prompted with only one or two in-context examples.*" <br>

See: https://react-lm.github.io/
<br>

Briefly, it's about the integration of the LLMs **reasoning** ability with the **action** capability of the software that calls it. The feedback loop implements an entity that we can call an "**agent**". <br>
The goal is to avoid one shot programs and introduce dynamic agents that self-adjust towards a certain goal.

<br>

