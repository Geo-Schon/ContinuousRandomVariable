# 4. Рост взрослого населения города X имеет нормальное распределение. Причем, средний рост равен 174 см, а среднее
# квадратичное отклонение равно 8 см. Какова вероятность того, что случайным образом выбранный взрослый человек имеет рост:
#     a). больше 182 см
#     b). больше 190 см
#     c). от 166 см до 190 см
#     d). от 166 см до 182 см
#     e). от 158 см до 190 см
#     f). не выше 150 см или не ниже 190 см
#     h). не выше 150 см или не ниже 198 см
#     i). ниже 166 см.

from scipy.stats import norm

mean = 174
standart_deviation = 8

a = 182
pa = 1-norm.cdf(a, mean, standart_deviation)
print(f'Вероятность роста больше {a} см = {pa: .4f}-> {pa *100:0.2f}%')

b = 190
pb = 1-norm.cdf(b, mean, standart_deviation)
print(f'Вероятность роста больше {b} см = {pb: .4f} -> {pb *100:0.2f}%')

c1, c2 = 166, 190
pc = norm.cdf(c2, mean, standart_deviation) - norm.cdf(c1, mean, standart_deviation)
print(f'Вероятность роста от {c1} см до {c2} см = {pc: .4f} -> {pc *100:0.2f}%')

d1, d2 = 166, 182
pd = norm.cdf(d2, mean, standart_deviation) - norm.cdf(d1, mean, standart_deviation)
print(f'Вероятность роста от {d1} см до {d2} см = {pd: .4f} -> {pd *100:0.2f}%')

e1, e2 = 158, 190
pe = norm.cdf(e2, mean, standart_deviation) - norm.cdf(d1, mean, standart_deviation)
print(f'Вероятность роста от {e1} см до {e2} см = {pe: .4f} -> {pe *100:0.2f}%')

f1, f2 = 150, 190
pf = norm.cdf(f1, mean, standart_deviation) + 1 - norm.cdf(f2, mean, standart_deviation)
print(f'Вероятность роста не выше {f1} см или не ниже {f2} см = {pf: .4f} -> {pf *100:0.2f}%')

h1, h2 = 150, 198
ph = norm.cdf(h1, mean, standart_deviation) + 1 - norm.cdf(h2, mean, standart_deviation)
print(f'Вероятность роста не выше {h1} см или не ниже {h2} см = {ph: .4f} -> {ph *100:0.2f}%')

i = 166
pi = norm.cdf(i, mean, standart_deviation)
print(f'Вероятность роста ниже {i} см = {pi: .4f} -> {pi *100:0.2f}%')