# 4.2. Beräkning av summa 1+2+3+... + n
n = int(input("Vad ska n vara?: "))
summa = 0
ett = 1
while ett <= n:
    summa = (summa * summa) + (ett * ett)
    ett = ett + 1
print(f"Summan blir {summa}")