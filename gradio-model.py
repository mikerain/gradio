import gradio as gr
from llama_cpp import Llama

# 指定本地 GGUF 模型的路径
# model_path = "/home/qxu/model/Llama-3.2-1B-Instruct-Q8_0.gguf"
model_path = "/home/qxu/model/granite-7b-lab-Q4_K_M.gguf"
# 加载模型
llama = Llama(model_path=model_path)

# 定义生成响应的函数
def generate_response(prompt):
    # 调用 Llama 模型进行文本生成
    output = llama(
        prompt,  # 输入的提示词
        max_tokens=128,  # 最大生成 token 数量
        temperature=0.7,  # 控制生成内容的多样性
    )
    return output["choices"][0]["text"]

# 创建 Gradio 界面
interface = gr.Interface(
    fn=generate_response,  # 指定生成函数
    inputs="text",  # 用户输入
    outputs="text",  # 模型输出
    title="模型测试",
    description="请输入问题, 模型将生成回答。",
)

# 启动 Gradio 服务
interface.launch()
