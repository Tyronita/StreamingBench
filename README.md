## 数据处理
先解压云盘下载的文件到ori_data下
- StreamingBench自动生成下所有文件 解压到 ori_data/1，先解压无_new后缀的，再解压有_new后缀的，覆盖无_new后缀的文件
- StreamingBench人工数据下所有文件 解压到 ori_data/2，0723_20.zip无需解压
- StreamingBenchGlobal/Active_Output下所有文件 解压到 ori_data/active
- StreamingBenchGlobal/Related_Context_Understanding下所有文件 解压到 ori_data/context

运行 Eval/data/process.sh

## 评测
需要在model文件夹下写对应的模型评测文件，继承于modelclass，参考MiniCPMV.py，然后在eval.py中如下位置添加模型评测代码：
```python
    if args.model_name == "GPT4o":
        from model.GPT4o import GPT4o
        model = GPT4o()
    elif args.model_name == "MiniCPM-V":
        from model.MiniCPMV import MiniCPMV
        model = MiniCPMV()
```

修改 cli-eval.sh 中的相关参数，运行 cli-eval.sh