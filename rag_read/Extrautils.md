
1 - Query Decomposition

https://zhuanlan.zhihu.com/p/633406099

提出了一种链式验证（CoVe）方法，通过该方法模型首先起草初始回答，然后计划验证问题来核实起草结果，独立回答这些问题以避免受到其他回答的影响，最终生成验证后的回答。

复杂问题 问题拆分
问题分解
Step_Back_Prompting


2 - Query Generate

问题生成 无法匹配到问题


3 - Evidence Extractor
PromptTemplate, ChatPromptTemplate  提示工程

4 - Step_Back_Prompting
https://zhuanlan.zhihu.com/p/670442559
Step-Back Prompting是由Google DeepMind的研究提出的。Step-Back Prompting是一种提示方法，使LLMs能够执行抽象操作，从而可以得出准确的答案。
step-back提示是一种提示工程方法，其中原始问题需要被精炼为step-back问题。随后，step-back答案用于最终答案。

25   30 -> 复杂问题 Step_Back_Prompting


5 - REDE Search Detector

6 - RAG Fusion