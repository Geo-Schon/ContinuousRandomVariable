# 2. О случайной непрерывной равномерно распределенной величине B известно, что ее дисперсия равна 0.2.
# Можно ли найти правую границу величины B и ее среднее значение зная, что левая граница равна 0.5? Если да, найдите ее.

d = 0.2
l = 0.5
b = l + (d * 12) ** (1 / 2)
print(
    f'Правая граница  величины В = {b: .3f}; Среднее значение величины В ({l}; {b: .2f}) (μ) = {(b + 0.5) / 2: .2f}')
