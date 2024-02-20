from pymilvus import (
    connections,
    utility,
    FieldSchema,
    CollectionSchema,
    DataType,
    Collection,
)

# 连接服务器：
connections.connect("default", host="localhost", port="19530")

# 创建集合：
fields = [
    FieldSchema(name="pk", dtype=DataType.INT64, is_primary=True, auto_id=False),
    FieldSchema(name="random", dtype=DataType.DOUBLE),
    FieldSchema(name="embeddings", dtype=DataType.FLOAT_VECTOR, dim=8)
]
schema = CollectionSchema(fields, "hello_milvus is the simplest demo to introduce the APIs")
hello_milvus = Collection("hello_milvus", schema)

# 在集合中插入向量：
import random

entities = [
    [i for i in range(3000)],  # field pk
    [float(random.randrange(-20, -10)) for _ in range(3000)],  # field random
    [[random.random() for _ in range(8)] for _ in range(3000)],  # field embeddings
]
insert_result = hello_milvus.insert(entities)
# After final entity is inserted, it is best to call flush to have no growing segments left in memory
hello_milvus.flush()

# 在实体上构建索引：
index = {
    "index_type": "IVF_FLAT",
    "metric_type": "L2",
    "params": {"nlist": 128},
}
hello_milvus.create_index("embeddings", index)

# 加载集合到内存并执行向量相似度搜索：
hello_milvus.load()
vectors_to_search = entities[-1][-2:]
search_params = {
    "metric_type": "L2",
    "params": {"nprobe": 10},
}
result = hello_milvus.search(vectors_to_search, "embeddings", search_params, limit=3, output_fields=["random"])

# 执行向量查询：
result = hello_milvus.query(expr="random > -14", output_fields=["random", "embeddings"])

# 执行混合搜索：
result = hello_milvus.search(vectors_to_search, "embeddings", search_params, limit=3, expr="random > -12",
                             output_fields=["random"])

# 通过主键删除实体：
expr = f"pk in [{ids[0]}, {ids[1]}]"
hello_milvus.delete(expr)

# 删除集合：
utility.drop_collection("hello_milvus")