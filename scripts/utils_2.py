nb_txt = 1000
dim = 100
nb_new = 100
# --- Running 2_numpy.py ---
# Took 0.002 seconds

# ==============================
# --- Running 2_pytorch_cpu.py ---
# Took 0.002 seconds

# ==============================
# --- Running 2_pytorch_gpu.py ---
# Took 1.196 seconds

nb_txt = 10000
dim = 100
nb_new = 1000
# --- Running 2_numpy.py ---
# Took 0.305 seconds

# ==============================
# --- Running 2_pytorch_cpu.py ---
# Took 0.054 seconds

# ==============================
# --- Running 2_pytorch_gpu.py ---
# Took 0.022 seconds

# ==============================



nb_txt = 1000000
dim = 100
nb_new = 1000
# --- Running 2_numpy.py ---
# Took 30.882 seconds

# ==============================
# --- Running 2_pytorch_cpu.py ---
# Took 4.023 seconds

# ==============================
# --- Running 2_pytorch_gpu.py ---
# Took 0.026 seconds

# ==============================



nb_txt = 10000
dim = 1000
nb_new = 1000
# --- Running 2_numpy.py ---
# Took 0.323 seconds

# ==============================
# --- Running 2_pytorch_cpu.py ---
# Took 0.063 seconds

# ==============================
# --- Running 2_pytorch_gpu.py ---
# Took 0.021 seconds

# ==============================

nb_txt = 100000
dim = 1000
nb_new = 1000

# --- Running 2_numpy.py ---
# Took 3.117 seconds

# ==============================
# --- Running 2_pytorch_cpu.py ---
# Took 0.444 seconds

# ==============================
# --- Running 2_pytorch_gpu.py ---
# Took 0.022 seconds


nb_txt = 10000
dim = 1000
nb_new = 10000

# --- Running 2_numpy.py ---
# Took 4.167 seconds

# ==============================
# --- Running 2_pytorch_cpu.py ---
# Took 0.563 seconds

# ==============================
# --- Running 2_pytorch_gpu.py ---
# Took 0.117 seconds



nb_txt = 100000
dim = 1000
nb_new = 10000

# --- Running 2_numpy.py ---
# Took 41.750 seconds

# ===================<===========
# --- Running 2_pytorch_cpu.py ---
# Took 5.713 seconds

# ==============================
# --- Running 2_pytorch_gpu.py ---
# Took 0.263 seconds


nb_txt = 100000
dim = 1000
nb_new = 100000
# --- Running 2_numpy.py ---
# ./run_all_2.sh: line 3: 35710 Killed: 9               python3 "$f"

# ==============================
# --- Running 2_pytorch_cpu.py ---
# ./run_all_2.sh: line 3: 35787 Killed: 9               python3 "$f"

# ==============================
# --- Running 2_pytorch_gpu.py ---
# Traceback (most recent call last):
#   File "/Users/peltouz/Library/Mobile Documents/com~apple~CloudDocs/GitHub/Advanced Programming/2_pytorch_gpu.py", line 35, in <module>
#     closest_indices_gpu = find_similar_pytorch(new_txt_gpu, existing_txt_gpu)
#   File "/Users/peltouz/Library/Mobile Documents/com~apple~CloudDocs/GitHub/Advanced Programming/2_pytorch_gpu.py", line 18, in find_similar_pytorch
#     dot_product = torch.matmul(all_txt_tensor, new_texts_tensor.T)
# RuntimeError: Invalid buffer size: 37.25 GiB


