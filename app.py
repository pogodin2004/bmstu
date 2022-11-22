import tensorflow as tf
import os, sys
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
import pandas as pd

model_loaded_1 = keras.models.load_model(r"C:\Users\ИТЦ\Desktop\bmstu\models\depth_model")
model_loaded_2 = keras.models.load_model(r"C:\Users\ИТЦ\Desktop\bmstu\models\width_model")

while True:
    try:
        n = int(input("Выберите прогнозируемое значение:\n 1 - Глубина сварочного шва\n 2 - Ширина сварочного шва\n"))
        if 1 <= n <=2:
            print('OK')
            break
        else:
            raise ValueError
    except ValueError:
        print("Вы ввели не число или число не входит в указанный диапазаон. Попробуйте снова: ")


col = ['Величина сварочного тока (IW)', '\nТок фокусировки электронного пучка (IF): ', '\nСкорость сварки (VW):', 
       '\nРасстояние до электронно-оптической системы(FP): ']
values = ['(50...40)','(120...160)', '(3.0...15.0)', '(60...150)']

input_val = pd.DataFrame()
j = []
i = 0

print("\nВведите параметры для расчета\n")
while i < len(col):
    line = f" {col[i]}{values[i]}: "
    while True:
        try:
            param_val = input(line)
            param_value = float(param_val)
        except:
            print("\nERROR!!! Введите числовое значение")
            continue
        break
    j.append(param_value)
    i += 1
df= pd.DataFrame([j], columns = col)


if n == 1:
    #print(model_loaded_1.summary())
    test_predictions_1 = model_loaded_1.predict((np.array(df)))
    print("\nПрогнозное значение глубины сварочного шва: ", str(test_predictions_1)[1:-1])
elif n == 2:
    test_predictions_2 = model_loaded_2.predict((np.array(df)))
    print("\nПрогнозное значение ширины сварочного шва: ", str(test_predictions_2)[1:-1])
