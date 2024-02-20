file Loaders:
1 - ppt -- python-pptx
2 - pdf-- 1、PDFMinerLoader 2、PaddleOCR pdf 转成 img OCR
3 - docx -- python-docx
4 - excel --openpyxl sheet --csv --CSVLoader 读取
5 - DeepDoctection -- 有格式的PDF和html 提取页面布局信息和表格信息 只支持英文

text splitter：
1 - code  RecursiveCharacterTextSplitter.from_language(language=Language[language_name]  定义语言
2 - html  HTMLHeaderTextSplitter   定义想要分割的标题列表和名称
3 - latex  LatexTextSplitter  	沿着Latex标题、标题、枚举等分割文本。  定义想要分割的标题列表和名称
4 - markdown  MarkdownHeaderTextSplitter 沿着Markdown的标题、代码块或水平规则来分割文本。  定义想要分割的标题列表和名称
5 - text  RecursiveCharacterTextSplitter  CharacterTextSplitter
   RecursiveCharacterTextSplitter
将按不同的字符递归地分割(按照这个优先级["\n\n", "\n", " ", ""])，这样就能尽量把所有和语义相关的内容尽可能长时间地保留在同一位置。
RecursiveCharacterTextSplitter需要关注的是4个参数：
separators - 分隔符字符串数组
chunk_size - 每个文档的字符数量限制
chunk_overlap - 两份文档重叠区域的长度
length_function - 长度计算函数
RecursiveCharacterTextSplitter 利用了滑动窗口算法，计算的实际规则是这样的：
首先，用我们定义的分割字符来切割文本，获得分割之后多段文本的数组
第一段文本不会计算长度，也就是说和chunk_size无关，不管chunk_size设置为多少，第一段的文本都是会无损获得（包括后续每个窗口的第一段文本）
第二段开始开始校验长度，定义一个窗口数组，如果前面所有段落的文本加上分隔字符的长度没超，那就正常往里丢就好了，如果当前文本片即将要超了chunk_size，
这时候就把前面的文本用分隔字符还原后保存到最终结果的数组中
然后还会执行一个操作就是将窗口数组中的文本片从第一个开始挨个丢掉，窗口一直往右滑，直到剩下的文本片的长度总和小于包的大小以及重叠窗口的大小，
如果我们配置了重叠窗口的长度，那么剩下来的文本片就用在了下一段的文本总和中，当然如果说下一段的文本片本身就超长，相当于就是把窗口往右推到底，
窗口里的文本片一个都不用了，直接把下一段作为窗口的第一个元素
   CharacterTextSplitter
分隔符的参数是单个的字符串。这就会使得RecursiveCharacterTextSplitter比CharacterTextSplitter对文档切割得更加碎片化，最后组装的时候两者的粒度就会有一定的差距了

CharacterTextSplitter 是字符文本分割，分隔符的参数是单个的字符串；RecursiveCharacterTextSplitter 是递归字符文本分割，
将按不同的字符递归地分割（按照这个优先级[“\n\n”, “\n”, " ", “”]），这样就能尽量把所有和语义相关的内容尽可能长时间地保留在同一位置。
因此，RecursiveCharacterTextSplitter 比 CharacterTextSplitter 对文档切割得更加碎片化

6 - token  
  TokenTextSplitter  根据openAI的token数进行分割  gpt2
  一种字节对编码（Byte Pair Encoder，BPE）方法，而BPE是一种自然语言处理领域中被经常使用的数据压缩算法
  SpacyTextSplitter 使用 Spacy分词后，按句子切割文本  
  text_splitter = SpacyTextSplitter(pipeline='zh_core_web_sm',chunk_size=1000,chunk_overlap=200)

  SentenceTransformersTokenTextSplitter  sentence-transformers/all-mpnet-base-v2 加载 sentence-transformers相关tokenizer
  NLTKTextSplitter  使用 NLTK分词后，按句子分割文本
  CharacterTextSplitter.from_huggingface_tokenizer   tokenizers加载其他模型tokenizers
  tiktoken openai开源

  https://zhuanlan.zhihu.com/p/638929185


7 - chinese_text  
ChineseRecursiveTextSplitter 可以看到主要是["\n\n","\n","。|！|？", "\.\s|\!\s|\?\s","；|;\s","，|,\s"] 进行分割
ChineseCharacterTextSplitter  使用正则化和标点符号把文档划分 将中、英文省略号进行规范等
8 - AliText
   modelscope.pipelines import pipeline
   pipeline(
            task="document-segmentation",
            model='damo/nlp_bert_document-segmentation_chinese-base',
            device="cpu")
   use_document_segmentation参数指定是否用语义切分文档，此处采取的文档语义分割模型为达摩院开源的nlp_bert_document-segmentation_chinese-base，
   如果使用模型进行文档语义切分，那么需要安装modelscope[nlp]：
   考虑到使用了三个模型，可能对于低配置gpu不太友好，因此这里将模型load进cpu计算，有需要的话可以替换device为自己的显卡id
   文档分割被定义为自动预测文档的段（段落或章节）边界。近年来，诸多研究者提出了许多基于神经网络的文本分割算法 

9 - AliWord
   modelscope.pipelines import pipeline
   pipeline(
            task="word-segmentation",
            model='damo/nlp_bert_document-segmentation_chinese-base',
            device="cpu")


10 - parent_and_child
    parent_splitter = RecursiveCharacterTextSplitter(separators, keep_separator, chunk_size=1000, **kwargs)
    child_splitter = RecursiveCharacterTextSplitter(separators, keep_separator, chunk_size=400, **kwargs)
    self.splitter  = ParentDocumentRetriever
https://zhuanlan.zhihu.com/p/673880793

下面我们来搜索与用户问题相似度较高的子文档块：

sub_docs = vectorstore.similarity_search("恐龙是冷血动物吗？")
print(sub_docs[0].page_content)
这里我们通过向量数据库的similarity_search方法搜索出来的是与用户问题相关的子文档块的内容，
下面我们使用检索器的get_relevant_documents的方法来对这个问题进行检索，它会返回该子文档块所属的主文档块的全部内容
retrieved_docs = retriever.get_relevant_documents("恐龙是冷血动物吗？")
print(retrieved_docs[0].page_content)

Embedding模型的语义提取能力有限。它们在呈现多主题、多回合语料库时不如简单语料库有效。这就是为什么RAG更喜欢较短的块。那么块的大小是最好的呢?在微软的分析中，
最小的块大小是512个tokens。一些企业级RAG应用程序中的块大小只有100个tokens。最小的块大小是否总是能获得更好的结果?

如前所述，分块策略会将文本语料库分解成小块，导致信息丢失。数据块越小，丢失的信息就越多。所以，有一个最优的块大小。过小的分块可能不太理想。
然而，寻找最优块大小就像超参数调优一样。你必须用你的数据做实验。

重叠背后的原因是重叠可以帮助将相邻的块链接在一起，并为块提供更好的上下文信息。然而，即使是非常激进的25%重叠也只能将准确率提高1.5%，从42.4%提高到43.9%。
这意味着这不是优化RAG性能的最有效方法。我们不能通过更多的重叠来进一步提高RAG的性能。记住，重叠分块甚至不能用于小块。

https://zhuanlan.zhihu.com/p/673906072