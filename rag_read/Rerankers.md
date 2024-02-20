1 - UPR
https://zhuanlan.zhihu.com/p/672777138
https://github.com/DevSinghSachan/unsupervised-passage-reranking
2 - TART
https://github.com/facebookresearch/tart
3 - BM25

4 - LLM
https://zhuanlan.zhihu.com/p/660596492
https://zhuanlan.zhihu.com/p/664918134
5 - MonoT5
6 - bge_reranker

https://zhuanlan.zhihu.com/p/657653570
https://zhuanlan.zhihu.com/p/665044136
https://zhuanlan.zhihu.com/p/675269272

模型更新。BGE-*-zh-v1.5缓解了相似度分布问题，通过对训练数据进行过滤，删除低质量数据，提高训练时温度系数temperature至0.02，使得相似度数值更加平稳 。
新增模型。开源BGE-reranker 交叉编码器模型，可更加精准找到相关文本，支持中英双语。不同于向量模型需要输出向量，BGE-reranker直接文本对输出相似度，
排序准确度更高，可用于对向量召回结果的重新排序，提升最终结果的相关性。
新增功能。BGE1.1增加难负样本挖掘脚本，难负样本可有效提升微调后检索的效果；在微调代码中增加在微调中增加指令的功能；
模型保存也将自动转成 sentence transformer 格式，更方便模型加载。

与embedding模型不同，reranker使用问题和文档作为输入，直接输出相似度而不是embedding。   cross_entropy
您可以通过向重新排序器输入查询和段落来获得相关性分数。 重排序器是基于交叉熵损失进行优化的，因此相关性得分不受特定范围的限制。

一定阈值范围 调用

rrf 重排

7 - Cohere Rerank