问题改写模型：a）将意图分为单表增删改查和多表增删改查，识别意图；b）使用GPT-4将原问题和改写以后问题组成QA对生成指令集数据，人工纠察指令集。
如查询：改写：查询表：，表关联：查询条件，查询内容：内容合并方式。使用多种模型（chatglm，baichuan等，）
和多种方式（Freeze方法、Lora方法、全量参数等）对指令集进行微调训练，并精确匹配率的评价指标选取最优微调模型。

Texttosql模型：a）将意图分为不同数据库类型，识别意图；b）使用GPT-4将改写以后问题和sql语句组成QA对生成指令集数据，人工纠察指令集。
使用多种模型（chatglm，baichuan等，）和多种方式（Freeze方法、Lora方法、全量参数等）对指令集进行微调训练，并执行正确率的评价指标选取最优微调模型。

关键词知识库：数据库，表名，字段，表关联方式，内容合并方式生成对应中文关键词，生成关键词知识库。

推理：根据输入查询语句，调用问题改写模型，生成改写以后问题，再和关键词匹配，如果所有改写条件完全匹配则直接输出sql或者查询结果，
如果没有完全匹配，这调用Texttosql模型生成输出sql或者查询结果。


https://blog.csdn.net/qq_42681787/article/details/132297830
https://github.com/ruc-datalab/zeronl2sql

https://zhuanlan.zhihu.com/p/662927748
https://github.com/ruckbreasoning/resdsql

本文提出了一种将预训练语言模型（PLMs）和大型语言模型（LLMs）相结合的ZeroNL2SQL框架，用于支持零样本NL2SQL生成。
该框架首先使用PLMs通过模式对齐生成SQL草图，然后使用LLMs通过复杂推理填充缺失信息。
通过实验验证，ZeroNL2SQL在真实世界基准测试中取得了最佳的零样本NL2SQL性能。