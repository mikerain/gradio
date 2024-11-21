import gradio as gr
from llama_cpp import Llama

# 加载模型
def load_model(model_path):
    try:
        return Llama(model_path=model_path)
    except Exception as e:
        raise RuntimeError(f"Failed to load model: {e}")

llm = load_model("/home/qxu/model/Llama-3.2-1B-Instruct-Q8_0.gguf")

# 预测函数
def predict(message, history):
    try:
        # 将历史记录和当前消息合并为用户输入
        messages = [{"role": "user", "content": msg} for msg, _ in history]
        # messages=[]
        messages.append({"role": "user", "content": message})  # 添加当前用户输入

        response = ""

        # 流式生成响应
        for chunk in llm.create_chat_completion(stream=True, messages=messages):
            part = chunk["choices"][0]["delta"].get("content", None)

            if part:
                response += part
            yield response

        yield response  # 输出剩余内容
    except Exception as e:
        yield f"An error occurred: {e}"

# 创建 Gradio 界面
demo = gr.ChatInterface(fn=predict,

                        )
demo.launch()

