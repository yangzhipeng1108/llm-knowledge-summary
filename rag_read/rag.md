1 - 文档加载
    docx
    pdf  1、PDFMinerLoader 2、PaddleOCR pdf 转成 img OCR pptx 转成 pdf
    excel
    md  markdown

1-1 文档预处理
    异常清洗  规范化空格 去除乱码 去除网页标识符 去除表情符
    过滤  检查文档的字重复率  检查文档的词重复率  检查文档的特殊字符率  检查文档的色情暴力词率 检查文档的困惑度
    去重  去重 余弦相识度 simhash  jaccard  编辑距离
    以64位的签名来说，把它以每16位划分块，如果两个签名海明距离小于等于3，则至少有一个16位块完全相同

    
2 - 文档分割
    tokenizer
    ChineseRecursiveTextSplitter
    ChineseCharacterTextSplitter
    nlp_bert_document-segmentation_chinese-base
    ParentDocumentRetriever
    对话不切分  文档切分 markdown切割标题
    父子文档切割 ChineseRecursiveTextSplitter 
    可以看到主要是["\n\n","\n","。|！|？", "\.\s|\!\s|\?\s","；|;\s","，|,\s"] 进行分割
    另外一个小技巧，先文本切句，用户问和文本短句匹配，再匹配到的文本短句和长段落匹配，再构建(用户问，标题层级，长段落)
    文本切分用默认的 recursive时好时坏，因为切的不好，就是会带来噪声，所以还是要按照标题层级来切。都是纯手工不添加的苦力活
    短的话 50-100 即可
    
3 - embedding 向量化
    openai -- tiktokenencoding = tiktoken.encoding_for_model('gpt-3.5-turbo')
    multilingual-e5
    bge-large-zh
    m3e
4 - 文档存储  向量数据库 文档数据库  Elasticsearch
             文档  对话
             多个文档库
             1 - chroma  一个开源嵌入式数据库
             2 - faiss  Facebook AI相似性搜索服务
             3 - milvus  用于存储、索引和管理由深度神经网络和其他机器学习（ML）模型产生的大量嵌入向量的数据库
             4 - pgEmbedding  MarkdownHeaderTextSplitter
             5 - pgVector  一个用于Postgres的开源向量相似性搜索服务
             6 - pinecone  一个具有广泛功能的向量数据库
             7 - ElasticSearch	ElasticSearch

5 - 检索召回  意图识别对应知识库
             对称语义检索    问题检索 关键字(ner)
             非对称语义检索   标题 关键字召回 bm25文档召回 向量召回  ColBERTv2 阈值很低时候使用  训练roberta模型 计算两个语义是否相似  batch内负采样 
             HyDE

6 - 检索召回优化  问题扩展  问题生成   生成指令集的问题进行扩展 多个问题对应一个答案
                问题分解   复杂问题  对比问题分解
                问题Step_Back_Prompting   langchain-ai/stepback-answer
                TSF(Think Step-Further)
                链式验证
                COT  多个计算问题分解 提示

7 - 检索重排  rrf 正常使用这个
             BM25  正常使用这个组合
             bge_reranker  阈值很低时候使用
             开源 BGE-reranker 交叉编码器模型，可更加精准找到相关文本，支持中英双语。不同于向量模型需要输出向量，BGE-reranker 直接文本对输出相似度，
             排序准确度更高，可用于对向量召回结果的重新排序，提升最终结果的相关性。
             UPR 
             TART

8 - self-Critique


9 - 输入大模型   q1 q2 q3 q4
               q2 q3 q4 q1


10 - 多轮对话  训练层面： https://zhuanlan.zhihu.com/p/673478090
              问答层面：  
              外挂小知识库
              知识库硬盘  向量知识库和文档知识库
              知识库内存  外挂小的向量知识库   最低阈值 代表这轮对话结束 外挂知识库清空 最高阈值 代表文档相关度高 一起去检测

11 - RAG评价指标
      答案  召回文档对比

12 - 意图识别  识别对应库  roberta 最后一层套了一个drop和 FFN

提示压缩

RAG系统的“七宗罪”
https://zhuanlan.zhihu.com/p/677691070

与传统的 LLM 相比，Self-RAG 具有多项优势。
自适应段落检索：通过这种方式，LLM 可以不断检索上下文，直到找到所有相关上下文（当然是在上下文窗口内）。
更相关的检索：很多时候，嵌入模型并不擅长检索相关上下文。Self-RAG 可以通过相关/不相关特殊标记来解决这个问题。
击败其他同类模型：Self-RAG 击败了其他同类模型，而且在许多任务中出人意料地击败了 ChatGPT。如果能与 ChatGPT 没有训练过的数据，
即更专有的工业数据，进行比较，那将会非常有趣。
不改变底层 LM：对我来说，这是一个巨大的优势，因为我们知道微调和 RLHF 很容易导致模型出现偏差。Self-RAG 似乎可以通过添加特殊标记来解决这个问题，
除此之外，文本生成保持不变。

https://zhuanlan.zhihu.com/p/662654185

Self-RAG是一个新的框架，通过自我反思令牌（Self-reflection tokens）来训练和控制任意LM。它主要分为三个步骤：检索、生成和批评。
检索：首先，Self-RAG解码检索令牌（retrieval token）以评估是否需要检索，并控制检索组件。如果需要检索，LM将调用外部检索模块查找相关文档。
生成：如果不需要检索，模型会预测下一个输出段。如果需要检索，模型首先生成批评令牌（critique token）来评估检索到的文档是否相关，
然后根据检索到的段落生成后续内容。
批评：如果需要检索，模型进一步评估段落是否支持生成。最后，一个新的批评令牌（critique token）评估响应的整体效用。

训练

Self-RAG 的训练包括三个模型：检索器（Retriever）、评论家（Critic）和生成器（Generator）。
首先，训练评论家，使用检索器检索到的段落以及反思令牌增强指令-输出数据。
然后，使用标准的下一个 token 预测目标来训练生成器 LM，以学习生成 自然延续(continuations)以及特殊 tokens (用来检索或批评其自己的生成内容).

推理
Self-RAG 通过学习生成反思令牌，使得在不需要训练LMs的情况下为各种下游任务或偏好量身定制模型行为。特别是：
它可以适应性地使用检索令牌进行检索，因此模型可以自发判断是不是有必要进行检索。
它引入了多种细粒度的批评令牌，这些令牌用于评估生成内容的各个方面的质量。在生成过程中，作者使用期望的批评令牌概率的线性插值进行segment级的beam search，
以在每一个时间步骤中确定最佳的K个续写方案。