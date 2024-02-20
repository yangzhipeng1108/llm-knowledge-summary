评价指标


https://baoyu.io/translations/rag/a-guide-on-12-tuning-strategies-for-production-ready-rag-applications
https://baoyu.io/translations/rag/evaluating-rag-applications-with-ragas

https://github.com/explodinggradients/ragas
评价指标
RAGAs 为您提供了一些 指标，可用于从组件层面和整体流程两个方面评估 RAG 流程的性能。
在 组件层次 上，RAGAs 提供了评价检索组件（包括 context_relevancy 和 context_recall）和生成组件（涉及 faithfulness 和 answer_relevancy）的专门指标 [2]:
上下文精准度 衡量检索出的上下文中有用信息与无用信息的比率。该指标通过分析 question 和 contexts 来计算。
上下文召回率 用来评估是否检索到了解答问题所需的全部相关信息。这一指标依据 ground_truth（此为框架中唯一基于人工标注的真实数据的指标）和 contexts 进行计算。
真实性 用于衡量生成答案的事实准确度。它通过对比给定上下文中正确的陈述与生成答案中总陈述的数量来计算。这一指标结合了 question、contexts 和 answer。
答案相关度 评估生成答案与问题的关联程度。例如，对于问题“法国在哪里及其首都是什么？”，答案“法国位于西欧。”的答案相关度较低，因为它只回答了问题的一部分。


https://juejin.cn/post/7308583491934142502

https://www.bilibili.com/read/cv28266724/?jump_opus=1
https://zhuanlan.zhihu.com/p/664052784



步骤是清晰的，那么，我们来看下评估指标：Hit Rate和MRR。
Hit Rate即命中率，一般指的是我们预期的召回文本（真实值）在召回结果的前 k 个文本中会出现，也就是 Recall@k 时，
能得到预期文本。一般，Hit Rate越高，就说明召回算法效果越好。

MRR即 Mean Reciprocal Rank 平均倒数排名，是一种常见的评估检索效果的指标。MRR 是衡量系统在一系列查询中返回相关文档或信息的平均排名的逆数的平均值。
例如，如果一个系统对第一个查询的正确答案排在第二位，对第二个查询的正确答案排在第一位，则 MRR 为 (1/2 + 1/1) / 2。


一. 上下文相关性： 评估从embedding库检索的上下文是否与用户查询相关。
二. 一致性：评估LLMs是否保持与从向量数据库检索到的相同上下文。
三. 答案相关性：答案相关性评估 RAG 管道是否提供与query相关的响应。


https://luxiangdong.com/2023/11/06/rerank/#/Elasticsearch%E4%B8%AD%E7%9A%84%E7%9B%B8%E4%BC%BC%E5%BA%A6%E6%A3%80%E7%B4%A2%E7%AE%97%E6%B3%95
ANN算法目前主要有三种：

基于图的算法创建数据的图表示，最主要的就是**分层可导航小世界图算法(HNSW)**。
基于哈希的算法：流行的算法包括:位置敏感哈希（LSH）、多索引哈希（MIH）；
基于树的算法：流行的是kd树、球树和随机投影树（RP树）。对于低维空间（≤10），基于树的算法是非常有效的。