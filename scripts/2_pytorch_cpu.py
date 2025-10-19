import torch
import time
import numpy as np
from utils_2 import nb_txt, dim, nb_new


device = torch.device("cpu")

def find_similar_pytorch(new_texts_tensor, all_txt_tensor):
    dot_product = torch.matmul(all_txt_tensor, new_texts_tensor.T)
    all_txt_norm = torch.linalg.norm(all_txt_tensor, dim=1)
    new_texts_norm = torch.linalg.norm(new_texts_tensor, dim=1)
    denominator = all_txt_norm.unsqueeze(1) * new_texts_norm.unsqueeze(0)
    similarity = dot_product / denominator
    return torch.argsort(similarity, dim=1, descending=True)[:, :3]



if __name__ == "__main__":
    existing_txt_np = np.random.rand(nb_txt, dim).astype(np.float32)
    new_txt_np = np.random.rand(nb_new,dim).astype(np.float32)
    existing_txt_pt_cpu = torch.from_numpy(existing_txt_np)
    new_txt_pt_cpu = torch.from_numpy(new_txt_np)

    t = time.time()
    closest_indices_pt_cpu = find_similar_pytorch(new_txt_pt_cpu, existing_txt_pt_cpu)
    print(f"Took %.3f seconds" % (time.time() - t))
