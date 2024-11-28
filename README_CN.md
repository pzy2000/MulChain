### MulChain

这是我们 DASFAA2025 论文 MulChain 的官方仓库

**WARNING**: 这是一个学术概念验证原型，特别是尚未接受仔细的代码审查。此实现尚未准备好用于生产使用。

#### 系统要求
- 操作系统：Windows、Mac OS X 或 Linux
- Python 3.7 或更高版本
- 用于下载依赖项和与 IPFS 和以太坊网络交互的网络连接

#### 安装步骤

##### 1. 安装 Python 依赖
你需要安装几个 Python 库来运行应用。打开你的终端或命令提示符，确保 Python 和 pip 可用，运行：

```bash
python --version
pip --version
```

如果 Python 和 pip 已安装，继续安装必要的 Python 库：

```bash
pip install -r requirements.txt
pip install -U "web3[tester]"
```

这些库允许与以太坊交互、处理图像和视频、以及创建图形用户界面。

##### 2. 安装 IPFS 桌面版
为了管理和存储多媒体文件，你需要安装 IPFS 桌面版，它提供了与 IPFS 交互的简单界面：

- 从 [IPFS 桌面版 v0.13.2](https://github.com/ipfs/ipfs-desktop/releases/download/v0.13.2/IPFS-Desktop-Setup-0.13.2.exe) 下载 Windows 安装程序。
- 不建议使用版本低于 v0.13.2 的 IPFS 桌面版。
- 运行下载的安装程序并按照屏幕上的指示安装。
- 安装完成后，运行 IPFS 桌面版。它会自动设置并启动一个 IPFS 节点。

##### 3. Solidity 编译器
应用使用 Solidity 智能合约，需要 Solidity 编译器。使用以下命令安装 Solidity 编译器：

```bash
pip install py-solc-x
```

##### 4. 以太坊网络连接
应用通过 Web3.py 库来连接到以太坊网络，默认使用内存中的测试网络。对于实际部署或使用真实交易进行测试，请配置 Web3.py 连接到公共测试网络或本地以太坊网络。

#### 运行实验
所有依赖项安装完成后，你可以运行应用。导航到包含你脚本的目录并运行：(使用 "-e" 或 "--experiment" 参数来明确您想要运行的实验, 有以下选项["CSB", "CSE", "FCSB", "FCSE", "FBC", "FBCF", "FEC", "FECF", "ALL"], "ALL"代表依次运行全部实验)

```bash
python run_exp.py
```

[//]: # (将 `deploy_contract_GUI.py` 替换为你的 Python 脚本的名称。)

[//]: # ()
[//]: # (#### 使用方法)

[//]: # (- **上传并存储数据**：点击此按钮打开文件对话框，选择一个图像和一个视频。选定的文件将被上传到 IPFS，它们的元数据（哈希和 CID）将被存储在以太坊上。)

[//]: # (- **查询数据**：点击此按钮从以太坊区块链获取并显示存储文件的元数据。)

#### 故障排除
- 确保在启动应用之前 IPFS 桌面版正在运行。
- 检查 Python 控制台是否有任何错误消息，这可能表明网络连接或依赖问题。
- 如果交易未能通过，验证以太坊测试网络是否正确配置并且是否有测试以太币。

此应用提供了一个基本框架，用于整合区块链技术与多媒体数据管理，并展示了去中心化应用的潜力。根据具体用例和需求，可以进行调整和增强。