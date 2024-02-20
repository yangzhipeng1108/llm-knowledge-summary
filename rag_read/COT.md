https://zhuanlan.zhihu.com/p/629087587
https://zhuanlan.zhihu.com/p/655427670
https://zhuanlan.zhihu.com/p/634180290

Zero-shot prompting：利用大模型基于需求直接生成源代码，不需要演示样例；  让我们一步步思考
Few-shot prompting：随机地挑选一些需求 - 代码对作为演示样例，利用大模型为一个新的需求直接生成源代码；
Chain-of-Thought prompting：few-shot prompting 的一个变体，采用需求 - 思维链 - 代码作为演示样例，引导大模型先生成一段思维链，再生成源代码。

多数投票提高CoT性能——自洽性（Self-consistency） 投票法

思维链只是在一些有限的领域，比如数学问题

正则化匹配 只有有数字时候才会调用 COT

https://opencompass.readthedocs.io/zh-cn/latest/prompt/chain_of_thought.html
https://www.promptingguide.ai/zh/techniques/tot