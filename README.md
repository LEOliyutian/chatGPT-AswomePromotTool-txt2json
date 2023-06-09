# TextToJsonConverter

## 介绍
这个GUI脚本是一个将文本文件转换为JSON格式文件的工具。它可以将符合特定格式的文本文件转换成对应的JSON格式文件。这个工具适用于在桌面版的ChatGPT中需要批量导入prompts的场景。但需要注意，转换的过程需要遵循一些特定的规则。

## 使用方法
1. 运行程序后，在窗口中点击 "Select Input File" 按钮选择要转换的文本文件。
2. 在弹出的对话框中选择对应的文本文件，点击 "Open"。
3. 点击 "Select Output File" 按钮选择输出的 JSON 文件的保存路径。
4. 在弹出的对话框中输入文件名和保存路径，点击 "Save"。
5. 点击 "Convert to JSON" 按钮进行转换，成功后弹出提示框。

## 输入文件格式
输入文件应该满足以下条件：
- 每两行为一组，每组代表一个 JSON 对象。
- 每个 JSON 对象包含以下字段：cmd、act、prompt。
- 字段之间以空行分隔。
- 输入文件第一行为标题，不作为 JSON 对象的内容。

## 输出文件格式
输出文件为标准的 JSON 格式文件，每个 JSON 对象包含以下字段：cmd、act、prompt。

## 注意事项
- 由于我的数据集是2行为一组，考虑数据的格式，我在转换前需要先复制每个 JSON 对象的第一行，填充到对应的 JSON 对象中。
- 输入文件中的空行不会被转换为 JSON 对象。
- 以上代码和文档来自于chatGPT和cursor。

