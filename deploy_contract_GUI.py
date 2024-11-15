import json
import os
import tkinter as tk
from tkinter import filedialog, messagebox, Label
from PIL import Image, ImageTk  # PIL库用于处理非GIF图片
import hashlib
import ipfshttpclient
from solcx import compile_standard, install_solc, set_solc_version
from web3 import Web3
import imageio
import threading

install_solc("0.8.20")
set_solc_version("0.8.20")
# 连接到IPFS和Web3
try:
    client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001')
except Exception as e:
    print(e)
    print("IPFS Client not properly installed or u forgot to start it at all!")
w3 = Web3(Web3.EthereumTesterProvider())
w3.eth.default_account = w3.eth.accounts[0]
with open("contracts/management_storage.sol", "r", encoding="utf-8") as file:
    simple_nft_file = file.read()

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"management_storage.sol": {"content": simple_nft_file}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]
                }
            }
        },
    },
    allow_paths=["."]
)

with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)
# 加载合约ABI和Bytecode
bytecode = compiled_sol['contracts']['management_storage.sol']['MultiModalStorageManager']['evm']['bytecode']['object']
# print(f"Bytecode: {bytecode}")
abi = compiled_sol['contracts']['management_storage.sol']['MultiModalStorageManager']['abi']
Greeter = w3.eth.contract(abi=abi, bytecode=bytecode)

# 部署合约
tx_hash = Greeter.constructor().transact()
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
contract_instance = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)


# 上传到IPFS
def upload_to_ipfs(file_path):
    res = client.add(file_path)
    return res['Hash']


# 生成文本哈希值
def generate_text_hash(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def show_image(image_path):
    img = Image.open(image_path)
    img = img.resize((250, 250), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(img)
    img_label.config(image=photo)
    img_label.image = photo  # keep a reference!


def play_video(video_path):
    video = imageio.get_reader(video_path)
    for image in video.iter_data():
        frame_image = Image.fromarray(image)
        frame_photo = ImageTk.PhotoImage(image=frame_image)
        video_label.config(image=frame_photo)
        video_label.image = frame_photo
        video_label.update()


# 上传并存储数据
def upload_and_store():
    image_path = filedialog.askopenfilename(title="Select an image", filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    video_path = filedialog.askopenfilename(title="Select a video", filetypes=[("MP4 files", "*.mp4")])
    text_content = "Hello, world! This is a test text"

    if image_path and video_path:
        image_cid = upload_to_ipfs(image_path)
        video_cid = upload_to_ipfs(video_path)
        text_hash = generate_text_hash(text_content)

        tx_hash = contract_instance.functions.storeData(text_hash, image_cid, video_cid).transact()
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

        if tx_receipt['status'] == 1:
            messagebox.showinfo("Success", "Data stored on blockchain successfully!")
            # show_image(image_path)
            # threading.Thread(target=play_video, args=(video_path,), daemon=True).start()
        else:
            messagebox.showerror("Error", "Transaction failed!")


def download_from_ipfs(cid, file_type):
    file_path = f"./cache/{cid}"
    if not os.path.exists('./cache/'):
        os.makedirs('./cache/')
    client.get(cid, target=file_path)
    if not os.path.exists(file_path + "/" + f"{cid}" + "." + file_type):
        os.rename(file_path + "/" + f"{cid}", file_path + "/" + f"{cid}" + "." + file_type)
    return file_path + "/" + f"{cid}." + file_type


def fetch_and_display():
    # try:
    data = contract_instance.functions.getData(0).call()
    image_cid = data[1]
    video_cid = data[2]
    image_path = download_from_ipfs(image_cid, 'jpg')
    video_path = download_from_ipfs(video_cid, 'mp4')
    show_image(image_path)
    threading.Thread(target=play_video, args=(video_path,), daemon=True).start()
    # except Exception as e:
    #     messagebox.showerror("Error", str(e))


# 查询数据
def query_data():
    try:
        data = contract_instance.functions.getData(0).call()
        messagebox.showinfo("Data Retrieved",
                            f"Text Hash: {data[0]}\nImage CID: {data[1]}\nVideo CID: {data[2]}\nTimestamp: {data[3]}")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# 创建GUI界面
root = tk.Tk()
root.title("Blockchain Data Manager")

upload_button = tk.Button(root, text="1、Upload and Store Data", command=upload_and_store)
upload_button.pack(pady=20)

query_button = tk.Button(root, text="2.1、Query hash on chain", command=query_data)
query_button.pack(pady=20)

query_button = tk.Button(root, text="2.2、Query Mulchain_v_CPU_Time_BTC on IPFS", command=fetch_and_display)
query_button.pack(pady=20)

img_label = Label(root)
img_label.pack(pady=20)

video_label = Label(root)
video_label.pack(pady=20)

root.mainloop()
