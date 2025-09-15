import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator

file_path = 'file_name.txt'
data = np.loadtxt(file_path)

p2 = data[:, 0]           # p2
chi1 = data[:, 1]         # chi1
sigma_ratio = data[:, 2]  # величина для контуров

# Минимум и диапазон
sigma_min = sigma_ratio.min()
sigma_max = sigma_ratio.max()

# Создаём уровни раскраски
num_levels_total = 80
num_near_min = int(0.7 * num_levels_total)
num_far = num_levels_total - num_near_min

# Уровни вблизи минимума
near_min_threshold = sigma_min + 0.2 * (sigma_max - sigma_min)
levels_near = np.linspace(sigma_min, near_min_threshold, num_near_min)

# Остальные уровни
levels_far = np.linspace(near_min_threshold, sigma_max, num_far + 1)[1:]  # без дубля

# Объединяем уровни
levels = np.concatenate([levels_near, levels_far])

# BoundaryNorm для неравномерного масштабирования цветов
cmap = plt.get_cmap('jet_r')
# Можно также попробовать: 'hot', 'afmhot', 'Reds', 'jet_r'

# Сопоставление значени с цветами
norm = BoundaryNorm(levels, cmap.N)

plt.figure(figsize=(8, 6))

# Закрашенные контуры с неравномерным цветом
cp = plt.tricontourf(p2, chi1, sigma_ratio, levels=levels, cmap=cmap, norm=norm)

# Чёрные контурные линии
contours = plt.tricontour(p2, chi1, sigma_ratio, levels=levels, colors='black', linewidths=0.4, alpha=0.6)

# Цветовая шкала
cbar = plt.colorbar(cp, extend='neither')

# Равномерные метки по диапазону
tick_positions = np.linspace(sigma_min, sigma_max, 5)
cbar.set_ticks(tick_positions)
cbar.set_ticklabels([f'{tick:.3f}' for tick in tick_positions])
cbar.set_label(r'$\Sigma_1 / \Sigma_2$', fontsize=18)
plt.setp(cbar.ax.get_yticklabels(), fontsize=14)

plt.yticks(np.arange(0, 1.6, 0.25), fontsize=18)
plt.xticks(fontsize=16)
plt.xlabel(r'$p_2$', fontsize=20)
plt.ylabel(r'$\chi_1$', fontsize=20)

plt.tight_layout()
plt.savefig("Contour_line_map.png", dpi=150, bbox_inches="tight")
# plt.show()