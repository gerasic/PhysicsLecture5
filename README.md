# Projectile Motion Simulation with Air Resistance

## Описание
Этот проект моделирует движение тела, брошенного под углом к горизонту с учетом сопротивления воздуха, пропорционального скорости. Реализован графический интерфейс с использованием библиотеки `tkinter`. Пользователь может настраивать начальную скорость, угол броска, высоту и коэффициент сопротивления среды.

## Используемые формулы и законы

1. **Сила сопротивления воздуха:**
   - Сила сопротивления воздуха пропорциональна скорости тела:
   - F<sub>d</sub> = -k * v
     - где:
       - k — коэффициент сопротивления воздуха (кг/с),
       - v — скорость тела (м/с).

2. **Уравнения движения:**

   **По оси X (горизонтальное движение):**

   - Изменение скорости по оси X описывается уравнением:
     
     m * (dv<sub>x</sub>/dt) = -k * v<sub>x</sub>
   - Это уравнение можно переписать как:
     
     dv<sub>x</sub>/dt = (k/m) * v<sub>x</sub>

   **По оси Y (вертикальное движение):**

   - Изменение скорости по оси Y описывается уравнением:
  
     m * (dv<sub>y</sub>/dt) = -m * g - k * v<sub>y</sub>
   - Это уравнение можно переписать как:
     
     dv<sub>y</sub>/dt = -g - (k/m) * v<sub>y</sub>

4. **Метод численного решения:**
   - Для интегрирования уравнений движения используется метод Рунге-Кутты 4-го порядка, который обеспечивает высокую точность и стабильность при вычислении траектории тела.

## Как использовать

1. **Запуск приложения:**
   - Установите run.exe
   - Запустите его двойным щелчком

2. **Настройка параметров:**
   
   Введите значения для следующих параметров:
     - **Начальная скорость (м/с):** скорость тела при броске.
     - **Угол броска (градусы):** угол, под которым тело брошено.
     - **Начальная высота (м):** высота, с которой брошено тело.
     - **Коэффициент сопротивления (кг/с):** коэффициент сопротивления воздуха.

3. **Запуск симуляции:**
   
   Нажмите кнопку **Run Simulation** для запуска расчета и отображения графиков. Результаты симуляции будут представлены в виде графиков:
     - **Траектория движения тела** (по осям X и Y).
     - **Скорость тела** как функция времени.
     - **Координаты тела** (x и y) как функции времени.

## Видео
https://github.com/user-attachments/assets/a059903e-dd7b-4ebf-9132-45279bf4ead8


