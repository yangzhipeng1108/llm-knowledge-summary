问题自动填充

在本文中，作者研究了基于LLM的query扩展。与传统的基于PRF的query扩展不同，LLM不限于初始检索的文档集，并且可以生成传统方法未涵盖的扩展项。
作者提出一个大型语言模型并为其提供一个查询，然后使用模型的输出用新的术语扩展原始查询，这些术语有助于文档检索。

实验结果表明，思想链提示对于query扩展特别有前途，因为它们指示模型生成详细的解释，这些解释可以涵盖各种各样的新关键字。
此外，在各种提示中包含PRF文档可以提高检索阶段的头重脚轻排名度量性能，并且在与较小的模型大小一起使用时更具鲁棒性，这有助于基于LLM的query扩展的实际部署。

问题改写

https://mp.weixin.qq.com/s/99MfXYFbz8KpHHJS7K3UQg

步骤一 ：构建查询改写数据集
利用线上的query改写策略  去生成查询， 改写pair对，从而采样一批数据。


https://xie.infoq.cn/article/2d22bf6d3cc6106f593a6a8e6
https://zhuanlan.zhihu.com/p/427312447
https://zhuanlan.zhihu.com/p/443452942