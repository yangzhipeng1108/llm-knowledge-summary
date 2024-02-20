
合并中文扩充词表并与原版LLaMA模型的32K词表，这里直接使用官方训练好的词表chinese_sp.model。当然，你也可以基于特有领域的语料训练专属的词表，
具体可参考之前的文章：大模型词表扩充必备工具SentencePiece。


第一阶段预训练、第二阶段预训练和指令精调三部分
第一阶段：冻结transformer参数，仅训练embedding，在尽量不干扰原模型的情况下适配新增的中文词向量。
第二阶段：使用 LoRA 技术，为模型添加LoRA权重（adapter），训练embedding的同时也更新LoRA参数。
将 LoRA 权重与基础模型合并
指令精调
https://zhuanlan.zhihu.com/p/631360711