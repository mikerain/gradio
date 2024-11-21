import gradio as gr

# 假设这是一个简单的文本分类模型
def sentiment_analysis(text):
    if "happy" in text:
        return "Positive"
    else:
        return "Negative"

# 创建 Gradio 界面
interface = gr.Interface(fn=sentiment_analysis, inputs="text", outputs="text", title="情感分析")

# 启动界面
interface.launch()