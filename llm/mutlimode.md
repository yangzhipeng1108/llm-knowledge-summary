Mixtral-8x7B和LLaMA结构唯一的区别，在于将MLP layer复制成了8个expert layers并在一起，通过一个gate layer，对每个token选择top-2的专家模型进行计算
模型确实是用top-2训练的（杠一下的话，top-3也不是没有可能）
Mixtral-8x7B的模型是利用Mistral-7B训练过程中early-stage的checkpoint训练而来的。Attention layer是直接继承的checkpoint，FFN是复制了8份，
然后加上gate layer继续完成后续的预训练的。这样就能解释Attention和MLP有一定的相似度，但不太高。这不会是独立训练8个模型或者在模型收敛后finetune一下能得到的结果。

MoEs：

• 相比于常规密集型模型，MoEs 的预训练过程更加快速
• 在具有相同数量参数的模型中，MoEs 展现出更快的推理速度
• 由于需要将所有专家模块加载到内存中，因此对 VRAM 的需求较高
• 虽然在微调方面面临许多挑战，但最近关于 MoE 指令调优的研究进展显示出积极的前景