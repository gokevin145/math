import tkinter as tk
from tkinter import messagebox
import math
# 快速排序法
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # 選擇中間元素作為基準
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# one系列:平方公式
# (A+B)**2=?
def one_to_one(a, b):
    return a ** 2 + (2 * a * b) + b ** 2
# (A-B)**2=?
def one_to_two(a, b):
    return a ** 2 - (2 * a * b) + b ** 2
# A**2-B**2
def one_to_three(a, b):
    return (a + b) * (a - b)
# (A+B+C)**2
def one_to_four(a, b, c):
    return a ** 2 + b ** 2 + c ** 2 + 2 * a * b + 2 * b * c + 2 * a * c
# two系列:立方公式
# (A+B)**3
def two_to_one(a, b):
    return a ** 3 + (3 * a * a * b) + (3 * a * b * b) + b ** 3
# (A-B)**3
def two_to_two(a, b):
    return a ** 3 - (3 * a * a * b) + (3 * a * b * b) - b ** 3
# A**3+B**3
def two_to_three(a, b):
    return (a + b) * (a ** 2 - (2 * a * b) + b ** 2)
# A**3-B**3
def two_to_four(a, b):
    return (a - b) * (a ** 2 + (2 * a * b) + b ** 2)
# three分點公式 數線上
def three_to_one(a, b, p):
    if p > a or p > b:
        print("P點數據輸入錯誤")
    else:
        if a > b:
            m = p - b
            n = a - p
            return ((m * b) + (n * a)) / (m + n)
        if b > a:
            m = p - a
            n = b - p
            return ((m * b) + (n * a)) / (m + n)
# four 兩點的座標點的 距離公式 分點公式
# 距離公式
def four_to_one(x1, y1, x2, y2):
    ab = ((x2 - x1) ** 2 + (y2 - y1) ** 2)
    ab = pow(ab, 0.5)
    return ab
# 分點公式
def four_to_two(x1, y1, x2, y2, p1, p2):
    m = four_to_one(x1, y1, p1, p2)
    n = four_to_one(x2, y2, p1, p2)
    px = (n * x1 + m * x2) / (m + n)
    py = (n * y1 + m * y2) / (m + n)
    return px, py
# five斜率
def five_to_one(x1, y1, x2, y2):
    if x1 != x2:
        if y1 == y2:
            return 0
        else:
            m = (y2 - y1) / (x2 - x1)
            return m
    else:
        return "線段為鉛直線，斜率不存在"
# six直線方程式
# 點斜式
def six_to_one(x, y, m):
    ans = "y-" + str(y) + "=" + str(m) + "(x-" + str(x) + ")"
    return ans
# 兩點式
def six_to_two(x1, y1, x2, y2):
    if x1 != x2:
        ans = "y-" + str(y1) + "=" + str((y2 - y1) / (x2 - x1)) + "*(x-" + str(x1) + ")"
        return ans
# seven數據分析
# 算術平均數
def seven_to_one(n):
    alli = 0
    for a in range(n):
        i = float(input())
        alli = alli + i
    ansi = alli / n
    return ansi
# 中位數
def seven_to_two(n):
    one = []
    for i in range(n):
        number = float(input())
        one.append(number)
    ans_test = quick_sort(one)
    how_many = len(ans_test)
    how_many = how_many / 2
    if how_many / 2 == 0:
        num = (math.floor(how_many))
        me = ans_test[num - 1] + ans_test[num] / 2
    else:
        me = ans_test[how_many]
    return me
class MathFunctionsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Functions App")
        # 創建按鈕
        self.create_button("快速排序:隨意輸入多個數字，用逗號隔開", quick_sort)
        self.create_button("(A+B)**2=?", one_to_one)
        self.create_button("(A-B)**2=?", one_to_two)
        self.create_button("A**2-B**2", one_to_three)
        self.create_button("(A+B+C)**2", one_to_four)
        self.create_button("(A+B)**3", two_to_one)
        self.create_button("(A-B)**3", two_to_two)
        self.create_button("A**3+B**3", two_to_three)
        self.create_button("A**3-B**3", two_to_four)
        self.create_button("分點公式 數線上:a, b, p", three_to_one)
        self.create_button("兩點的座標點的 距離公式x1, y1, x2, y2", four_to_one)
        self.create_button("兩點的座標點的 分點公式x1, y1, x2, y2, p1, p2", four_to_two)
        self.create_button("斜率x1, y1, x2, y2", five_to_one)
        self.create_button("點斜式x, y, m", six_to_one)
        self.create_button("兩點式x1, y1, x2, y2", six_to_two)
        self.create_button("算術平均數", seven_to_one)
        self.create_button("中位數", seven_to_two)
    def create_button(self, text, function):
        button = tk.Button(self.root, text=text, command=lambda: self.get_input_and_execute(function))
        button.pack(pady=5)
    def get_input_and_execute(self, function):
        input_window = tk.Toplevel(self.root)
        tk.Label(input_window, text="Enter values separated by commas:").pack(pady=5)
        entry = tk.Entry(input_window)
        entry.pack(pady=5)
        tk.Button(input_window, text="Execute", command=lambda: self.execute_function(function, entry.get())).pack(
            pady=10)
    def execute_function(self, function, input_values):
        try:
            # 將輸入的值轉換為參數
            input_values = tuple(map(float, input_values.split(',')))
            result = function(*input_values)
            self.show_result(result)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    def show_result(self, result):
        # 創建新的視窗來顯示結果
        result_window = tk.Toplevel(self.root)
        result_label = tk.Label(result_window, text=f"Result: {result}")
        result_label.pack(padx=20, pady=20)
if __name__ == "__main__":
    root = tk.Tk()
    app = MathFunctionsApp(root)
    root.mainloop()
