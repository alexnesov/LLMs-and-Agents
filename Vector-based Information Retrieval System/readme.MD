
# Effective Chunking: Maintaining Semantic Coherence in Text Processing

A way to circumvent the issue of a text being too big to be ingested by the language model (LLM) is through a process called 'chunking' or '**disassembling and reassembling.**'

But this process needs to **make sense**. We don't just split the text randomly (eventhough this could make sens for some cases). <br>
We want the chunks need to be sementically related. 

### What does 'semantically related' mean?

 It means that we don't want to simply divide the text into different parts; rather, we want to split it in a way that maintains the discursive logic and ensures that the different chunks are connected in terms of meaning."

![docker_compose_setup](Sentences-are-semantically-similar-if-they-can-be-answered-by-the-same-responses.png)

Image reference: https://www.researchgate.net/figure/Sentences-are-semantically-similar-if-they-can-be-answered-by-the-same-responses_fig1_324690566


### LangChain text splitters