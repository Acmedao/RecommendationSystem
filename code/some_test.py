import torch

# 假设：
num_prompts = 3   # 物品特征数量（如ID、类别、标签）
seq_len = 5      # 用户序列最大长度
hidden_dim = 8  # 嵌入维度

# 1. 物品特征（Prefix Prompts）
prefix_embeddings = torch.randn(num_prompts, hidden_dim)  # 可学习或通过物品编码器生成

# 2. 用户序列（历史UID嵌入）
user_embeddings = torch.randn(seq_len, hidden_dim)  # 实际中通过UID查找表获取

# 3. 添加 [CLS] Token
cls_token = torch.nn.Parameter(torch.randn(1, hidden_dim))  # 可学习参数
input_embeddings = torch.cat([prefix_embeddings, user_embeddings, cls_token], dim=0)
print(prefix_embeddings)
print(user_embeddings)
print(cls_token)
print(input_embeddings)