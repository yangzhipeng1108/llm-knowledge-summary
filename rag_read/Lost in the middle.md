大模型对相关信息的位置很敏感，当相关的信息在输入prompt的开头或者结尾时，能够取得较好的效果，而当相关的信息在prompt中间部分时，性能会显著下降。

面的实验用的模型都是Decoder-only的架构，下图增加了两种Encoder-Decoder模型（flan-t5-xxl、flan-ul2）在多文档问答上的实验结果，可以看到同样有类似的现象。
将query放在文档之前同样有“Lost in the middle”的现象。
发现指令微调之前，仍然具有“Lost in the middle”现象。
对于Llama模型来说，13B和70B的“Lost in the middle”的现象更加明显，而7B模型相对没这么明显。
准确率相比召回文档数量的边际收益是明显递减的，也就是说召回的多余的文档对于回答问题并没有太大作用。