import time
import numpy as np
from utils_2 import nb_txt, dim, nb_new 

def find_similar_numpy(new_texts_matrix, all_txt_matrix):
    dot_product = np.dot(all_txt_matrix, new_texts_matrix.T)
    all_txt_norm = np.linalg.norm(all_txt_matrix, axis=1)
    new_texts_norm = np.linalg.norm(new_texts_matrix, axis=1)
    denominator = all_txt_norm[:, np.newaxis] * new_texts_norm[np.newaxis, :]
    similarity = dot_product / denominator
    return np.argsort(-similarity, axis=1)[:, :3]


if __name__ == "__main__":
    existing_txt_np = np.random.rand(nb_txt, dim).astype(np.float32)
    new_txt_np = np.random.rand(nb_new,dim).astype(np.float32)
    t = time.time()
    closest_indices_np = find_similar_numpy(new_txt_np, existing_txt_np)
    print(f"Took %.3f seconds" % (time.time() - t))