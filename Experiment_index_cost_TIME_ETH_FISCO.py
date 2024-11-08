import os
import sys
sys.path.append("../")
sys.path.append("")
sys.path.append("sdk/")
sys.path.append(os.getcwd())
import pandas as pd
from datetime import datetime
import ipfshttpclient
from tqdm import tqdm
from SQL_MiddleWare_fisco import SQLMiddleware, generate_random_times
block_sizes = [16, 32, 64, 128, 256, 512, 1024]


def main():
    # 假设合约和 IPFS 客户端实例已被初始化
    try:
        ipfs_client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001')  # 替换为你的 IPFS 节点地址
    except Exception as e:
        print(e)
        print("IPFS Connect failed, plz check if ipfs is configured correctly and turned on")
        ipfs_client = None

    # 部署合约
    sql_middleware = SQLMiddleware(None, ipfs_client)

    # 逐步增加块的数量，从 256 到 16384
    df = pd.read_csv('../0to999999_BlockTransaction.csv', usecols=['timestamp', 'transactionHash'], nrows=6000)

    # 将数据转换为指定格式的列表，并格式化时间戳为 %Y-%m-%d
    data_list = [
        {
            'hash': row['transactionHash'],
            'time_stamp': datetime.fromtimestamp(row['timestamp']).strftime('%Y-%m-%d %H:%M:%S')
        }
        for _, row in df.iterrows()
    ]
    time_stamp_list = []
    for data in data_list:
        time_stamp_list.append(data['time_stamp'])
    min_time = min(time_stamp_list)
    max_time = max(time_stamp_list)
    min_time = datetime.strptime(str(min_time), '%Y-%m-%d %H:%M:%S')
    max_time = datetime.strptime(str(max_time), '%Y-%m-%d %H:%M:%S')
    print("min_time:", min_time)
    print("max_time:", max_time)
    # 验证是否成功读取
    print(f"Loaded {len(data_list)} items from data_list.csv")
    with open("../AAA_TIME_INDEX_COST_ETH_FISCO_BCOS" + str(datetime.now().strftime('%Y-%m-%d %H_%M_%S')), 'a+') as fw:
        for j in range(0, len(block_sizes)):
            block_size = block_sizes[j]
            print(f"----- Starting test for {block_size} blocks -----")
            fw.write(f"----- Starting test for {block_size} blocks -----")
            fw.write("\n")
            print(f"----- Starting insert query for {block_size} blocks -----")
            for i in tqdm(range(0 if j == 0 else block_sizes[j - 1], block_size)):
                text_hash = data_list[i]['hash']
                time_stamp = data_list[i]['time_stamp']
                image_path = "../sample_image.jpg"  # 请替换为实际图片路径
                video_path = "../sample_video.mp4"  # 请替换为实际视频路径
                insert_query = f"INSERT INTO multimodal_data (textHash, imageCID, videoCID, timestamp) VALUES ('{text_hash}', '{image_path}', '{video_path}', '{time_stamp}')"
                sql_middleware.parse_query(insert_query)

            print(f"----- Starting select query for {block_size} blocks -----")
            for _ in tqdm(range(0 if j == 0 else block_sizes[j - 1], block_size)):
                # 构建 SELECT 查询并调用 parse_query
                a, b = generate_random_times(str(min_time), str(max_time))
                select_query = f"SELECT * FROM multimodal_data WHERE timestamp BETWEEN '{a}' AND '{b}'"
                sql_middleware.parse_query(select_query)

            avg_MulChain_o_index_build_time = (sum(sql_middleware.MulChain_o_index_building_times) /
                                               len(sql_middleware.MulChain_o_index_building_times))

            avg_MulChain_o_select_latency = sum(sql_middleware.select_MulChain_o_latency) / len(
                sql_middleware.select_MulChain_o_latency)
            avg_MulChain_BT_select_latency = sum(sql_middleware.select_latency) / len(sql_middleware.select_latency)
            avg_MulChain_v_index_build_time = sum(sql_middleware.index_building_times) / len(
                sql_middleware.index_building_times)
            print(f"MulChain_v Insert time for {block_size} blocks: {avg_MulChain_v_index_build_time:.4f} seconds")
            fw.write(
                f"MulChain_v Insert time for {block_size} blocks: {avg_MulChain_v_index_build_time:.4f} seconds")
            fw.write("\n")
            print(
                f"MulChain_o Insert time for {block_size} blocks: {avg_MulChain_o_index_build_time:.4f} seconds")
            fw.write(
                f"MulChain_o Insert time for {block_size} blocks: {avg_MulChain_o_index_build_time:.4f} seconds")
            fw.write("\n")

            print(f"MulChain_Bt Select latency for {block_size} blocks: {avg_MulChain_BT_select_latency:.8f} seconds")
            fw.write(f"MulChain_Bt Select latency for {block_size} blocks: {avg_MulChain_BT_select_latency:.8f} seconds")
            fw.write("\n")

            print(
                f"MulChain_o Select latency for {block_size} blocks: {avg_MulChain_o_select_latency:.8f} seconds")
            fw.write(
                f"MulChain_o Select latency for {block_size} blocks: {avg_MulChain_o_select_latency:.8f} seconds")
            fw.write("\n")


if __name__ == "__main__":
    main()
