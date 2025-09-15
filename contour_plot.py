import numpy as np
import matplotlib.pyplot as plt

file_path = f'file_name.txt'

data = np.loadtxt(file_path, skiprows=1)
# Загружаемый файл в формате столбцов. 
# Если есть строка с обозначением, какой столбец за что овечает, то
# skiprows=1,
# если такой строки нет, то
# skiprows=0 или убрать


p2 = data[:, 0] 
chi1 = data[:, 1]  
sigma_ratio = data[:, 2] 

scatter = plt.scatter(p2, chi1, c=sigma_ratio, cmap='viridis', marker="s", s=1100)
plt.colorbar(scatter, label='$\Sigma_1 / \Sigma_2$')

plt.xlabel('$p_2$', fontsize=18)
plt.ylabel('$\chi_1$', fontsize=18)
plt.ylim(0.0, 1.5)
plt.xlim(1.0, 10)
plt.yticks(np.arange(0, 1.6, 0.25))
plt.xticks(np.arange(1.0, 11, 1))
# plt.title(f"$N_s = {N_s}$")

plt.grid(True, color='black', linestyle='-', linewidth=0.5)
plt.tight_layout()
plt.savefig(f"contour_map.png", dpi=150, bbox_inches="tight")
