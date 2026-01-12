cluster_1= [

r'(AI|Artificial intelligen.{0,3}|artificially intelligen.{0,3}|GenAI|xAI|ASI|AGI|AI.driven|AI.based|ML|ANI|NLP|LLM|LLMs|RLM|RLMs|VLM|VLMs|computational Intelligen.{0,3}|ChatGPT|GPT|google bard|Claude|Midjourney|bing chat|Chatbot|Gemini|copilot|co.{0,1}pilot|generative model*"|LLaMA|Mistral|Mixtral|BERT|PubMedBERT|BioBERT|BioGPT|OpenAI|Meta AI|T5 model|Flan.T5|Flan T5|DeepSeek|Ernie|Grok|Qwen)( (\w+)){0,3} (agent|agents|agentic|agentic|multiagent|Multi.Agent|agent.based|autonomous|autonomy|autonomously|automate|automates|multi.actor|multi actor.{0.3}|self navigating|self.navigating|self navigation|selfnavigation|multi.{0,1}step reasoning|multi.{0,1}step planning|self.{0,1}adaptive|adaptability|adaptive|multi.{0,1}step task.{0,3}|multi.{0,1}stage task.{0,3}|multi stage task.{0,3})',

r'(agent|agents|agentic|agentic|multiagent|Multi.Agent|agent.based|autonomous|autonomy|autonomously|automate|automates|multi.actor|multi actor.{0.3}|self navigating|self.navigating|self navigation|selfnavigation|multi.{0,1}step reasoning|multi.{0,1}step planning|self.{0,1}adaptive|adaptability|adaptive|multi.{0,1}step task.{0,3}|multi.{0,1}stage task.{0,3}|multi stage task.{0,3})( (\w+)){0,3} (AI|Artificial intelligen.{0,3}|artificially intelligen.{0,3}|GenAI|xAI|ASI|AGI|AI.driven|AI.based|ML|ANI|NLP|LLM|LLMs|RLM|RLMs|VLM|VLMs|computational Intelligen.{0,3}|ChatGPT|GPT|google bard|Claude|Midjourney|bing chat|Chatbot|Gemini|copilot|co.{0,1}pilot|generative model*"|LLaMA|Mistral|Mixtral|BERT|PubMedBERT|BioBERT|BioGPT|OpenAI|Meta AI|T5 model|Flan.T5|Flan T5|DeepSeek|Ernie|Grok|Qwen)',

r'(multi.{0,1}agent system|multi.{0,1}agent systems|multiagent system|multiagent systems|multi agent system|multi agent systems|autonomous system|autonomous systems|AI orchestrat|LLM orchestrat|automate AI workflow|multi.{0,1}actor application|multi-actor system|multi actor application|multi actor system|Multi.{0,1}Agent Orchestrat|MultiAgent Orchestrat|Multi Agent Orchestrat|Stateful LLM Workflow|Multi.{0,1}AI agent|task decomposition|workflow automation|multi.{0,1}agent coordination|multiagent coordination|multi agent coordination)',

r'(CrewAI|AutoGen|ReAct Framework|Reasoning and Acting|LangChain|FlowiseAI|Haystack|TaskWeaver|Auto.{0.1}GPT|LlamaIndex|MetaGPT|SuperAGI|OpenAI Agent|agent|agents|agentic|multiagent|Multi.{0,1}Agent|agent.{0,1}based)'
]

cluster_2 = [
        r'(meta.{0,1}analys)',
        r'cochrane review',
        r'systematic review',
        r'systematic overview',
        r'literature review',
        r'scoping review',
        r'rapid review',
        r'narrative review',
        r'umbrella review',
        r'review of reviews',
        r'overview of reviews',
        r'research synthes',
		r'systematic synthes',
        r'literature synthes',
        r'evidence synthes',
        r'evidence review',
        r'evidence map',
        r'evidence summar',
        r'gap map',]
        # r'((literature|document.{0,3}|citation.{0,3}|paper.{0,1}|article.{0,1}|manuscript.{0,1}|study|studies|publication.{0,1}|database.{0,1})( (\w+)){0,3} (search.{0,3}|seek|seeking|retriev.{0,3}|find|finding))',
		# r'(search.{0,3}|seek|seeking|retriev.{0,3}|find|finding)( (\w+)){0,3} literature|document.{0,3}|citation.{0,3}|paper.{0,1}|article.{0,1}|manuscript.{0,1}|study|studies|publication.{0,1}|database.{0,1}',
		# r'(search strateg.{0,3}|search string.{0,1}|query|queries|search syntax|search)( (\w+)){0,3} (design.{0,3}|build.{0,3}|formulat.{0,3}|generat.{0,3}|develop.{0,2})',
		# r'(design.{0,3}|build.{0,3}|formulat.{0,3}|generat.{0,3}|develop.{0,2})( (\w+)){0,3} (search strateg.{0,3}|search string.{0,1}|query|queries|search syntax|search)',
		# r'(literature|document.{0,1}|paper.{0,1}|article.{0,1}|manuscript.{0,1}|title.{0,1}|abstract.{0,1}|full.{0,1}text.{0,1}|fulltext.{0,1}|full text.{0,1}|record.{0,1}|study|studies|citation.{0,1}|reference.{0,1}|paper.{0,1}|article.{0,1}|publication.{0,1}|literature|document.{0,1})( (\w+)){0,3} (screen.{0,3})',
		# r'(screen.{0,3})( (\w+)){0,3} (literature|document.{0,1}|paper.{0,1}|article.{0,1}|manuscript.{0,1}|title.{0,1}|abstract.{0,1}|full.{0,1}text.{0,1}|fulltext.{0,1}|full text.{0,1}|record.{0,1}|study|studies|citation.{0,1}|reference.{0,1}|paper.{0,1}|article.{0,1}|publication.{0,1}|literature|document.{0,1})',
		# r'(literature|document.{0,1}|paper.{0,1}|article.{0,1}|manuscript.{0,1}|title.{0,1}|abstract.{0,1}|full.{0,1}text.{0,1}|fulltext.{0,1}|full text.{0,1}|record.{0,1}|study|studies|citation.{0,1}|reference.{0,1}|paper.{0,1}|article.{0,1}|publication.{0,1}|literature|document.{0,1})( (\w+)){0,3} (selection|inclusion|quality assessment.{0,1}|critical appraisal|risk of bias|methodological appraisal|appraisal|abstraction|data extraction|information extraction|data captur.{0,1}|synthes.{0,1}|collat.{0,3})',
		# r'(selection|inclusion|quality assessment.{0,1}|critical appraisal|risk of bias|methodological appraisal|appraisal|abstraction|data extraction|information extraction|data captur.{0,1}|synthes.{0,1}|collat.{0,3})( (\w+)){0,3} (literature|document.{0,1}|paper.{0,1}|article.{0,1}|manuscript.{0,1}|title.{0,1}|abstract.{0,1}|full.{0,1}text.{0,1}|fulltext.{0,1}|full text.{0,1}|record.{0,1}|study|studies|citation.{0,1}|reference.{0,1}|paper.{0,1}|article.{0,1}|publication.{0,1}|literature|document.{0,1})'
        # ]

cluster_NOT_titles = []
cluster_NOT_abstracts = []