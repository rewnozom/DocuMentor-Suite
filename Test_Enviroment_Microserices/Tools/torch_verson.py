import torch
print("PyTorch version:", torch.__version__)
print("CUDA tillgänglig:", torch.cuda.is_available())
print("Aktiv CUDA-enhet:", torch.cuda.get_device_name(torch.cuda.current_device()))
