# ## 构建词汇表
# - 给定文本 "The car is blue."，我们可以根据其中出现的单词构建词汇表。  
# - 假设嵌入维度为4


# 定义文本
text = "The car is blue."

# 分词处理
tokens = text.split()

# 构建词汇表
vocab = ['[PAD]', '[UNK]', '[CLS]', '[SEP]']  # 特殊标记
for token in tokens:
    if token not in vocab:
        vocab.append(token)

# 输出词汇表
print("Vocabulary:")
# 将词汇表保存为文件
with open("vocab.txt", "w", encoding="utf-8") as f:
    for word in vocab:
        f.write(word + "\n")