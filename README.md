### MulChain

This is the official repo for our DASFAA2025 paper MulChain.

**WARNING**: This is an academic proof-of-concept prototype, and in particular has not received careful code review. This implementation is NOT ready for production use.

#### System Requirements
- Operating System: Windows, Mac OS X, or Linux
- Python 3.7 or higher
- Network connection for downloading dependencies and interacting with IPFS and Ethereum networks

#### Installation Steps

##### 1. Install Python Dependencies
You need to install several Python libraries to run the application. Open your terminal or command prompt, ensure Python and pip are available, and run:

```bash
python --version
pip --version
```

If Python and pip are installed, proceed to install the necessary Python libraries:

```bash
pip install -r requirements.txt
pip install -U "web3[tester]"
```

These libraries enable interaction with Ethereum, handle images and videos, and create the graphical user interface.

##### 2. Install IPFS Desktop
To manage and store multimedia files, you need to install IPFS Desktop, which provides an easy interface for interacting with IPFS:

- Download the Windows installer for [IPFS Desktop v0.13.2](https://github.com/ipfs/ipfs-desktop/releases/download/v0.13.2/IPFS-Desktop-Setup-0.13.2.exe). For other OS, please visit https://github.com/ipfs/ipfs-desktop/releases/tag/v0.13.2 to download the corresponding version.
- IPFS Desktops with version newer than v0.13.2 are not recommended.
- Run the downloaded installer and follow the on-screen instructions to install.
- After installation, launch IPFS Desktop. It will automatically set up and start an IPFS node.

##### 3. Solidity Compiler
The application uses Solidity smart contracts, requiring the Solidity compiler. Install the Solidity compiler with the following command:

```bash
pip install py-solc-x
```

##### 4. Ethereum Network Connection
The application uses the Web3.py library to connect to the Ethereum network, defaulting to an in-memory test network. For actual deployment or testing with real transactions, configure Web3.py to connect to a public test network or a local Ethereum network.

#### Running the Experiments
After installing all dependencies, you can run the application. Navigate to the directory containing your script and run: (use "-e" or "--experiment" to specify the exact experiment you wish to run, choices=["CSB", "CSE", "FCSB", "FCSE", "FBC", "FBCF", "FEC", "FECF", "ALL"], "ALL" means that all exps will be run sequentially)

```bash
python run_exp.py
```

[//]: # (#### Usage)

[//]: # (- **Upload and Store Data**: Click this button to open a file dialog, select an image and a video. The selected files will be uploaded to IPFS, and their metadata &#40;hashes and CIDs&#41; will be stored on Ethereum.)

[//]: # (- **Query Data**: Click this button to retrieve and display the stored file metadata from the Ethereum blockchain.)

#### Troubleshooting
- Ensure IPFS Desktop is running before starting the application. (MulChain can run without IPFS with basic functionalities)
- Check the Python console for any error messages, which may indicate network connection or dependency issues.
- If a transaction fails, verify that the Ethereum test network is correctly configured and that you have test Ether.
