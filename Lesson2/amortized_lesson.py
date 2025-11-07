# -*- coding: utf-8 -*-
"""
amortized_lesson.py — הדגמות אמורטיות עם הסברים
תלויות: numpy, matplotlib

הרצה:
    python amortized_lesson.py                  # מריץ הכול
    python amortized_lesson.py --save-plots     # שומר גרפים ל-out/
    python amortized_lesson.py --section counter|dynamic|clear|all
"""
import argparse
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
OUT = Path("out"); OUT.mkdir(exist_ok=True)

def save_or_show(fig, name, save):
    if save:
        path = OUT / f"{name}.png"
        fig.savefig(path, bbox_inches="tight", dpi=140)
        print("[saved]", path)
    else:
        plt.show()

# ---------- 1) Binary Counter ----------
def binary_counter_total_flips(m: int) -> int:
    total = 0
    i = 1
    while i <= m:
        total += m // i
        i <<= 1
    return total

def demo_binary_counter(m=1000, save=False):
    total = binary_counter_total_flips(m)
    amort = total / m
    print("Binary Counter:")
    print(f"  total flips ≈ {total}  | amortized per increment ≈ {amort:.3f}  (צפוי < 2)")
    fig = plt.figure()
    xs = np.arange(1, m+1)
    bound = 2 * xs
    flips = [binary_counter_total_flips(k) for k in xs]
    plt.plot(xs, bound, label="2m (חסם עליון)")
    plt.plot(xs, flips, label="סה\"כ היפוכים עד m")
    plt.xlabel("m (מספר אינקרמנטים)")
    plt.ylabel("סה\"כ היפוכים")
    plt.title("Binary Counter: total bit flips ≤ 2m")
    plt.legend()
    save_or_show(fig, "binary_counter_total_flips", save)

# ---------- 2) Dynamic Array ----------
def simulate_dynamic_array_appends(m=2000, growth=2):
    """
    מדמה Array שמכפיל קיבולת כשמתמלא.
    מחזיר:
      costs_all_ops  - רשימת עלויות לכל פעולה בפועל (כולל resize וגם append)
      cum_after_each_append - מצטבר לאחר כל append (אורך מדויק m)
    """
    capacity = 1
    size = 0
    total_cost = 0
    costs_all_ops = []
    cum_after_each_append = []
    for _ in range(m):
        if size == capacity:
            total_cost += size          # עלות ההעתקה
            costs_all_ops.append(size)
            capacity *= growth
        total_cost += 1                  # append
        costs_all_ops.append(1)
        size += 1
        cum_after_each_append.append(total_cost)
    return np.array(costs_all_ops), np.array(cum_after_each_append), total_cost

def demo_dynamic_array(m=2000, growth=2, save=False):
    costs_all, cum_after_each, total = simulate_dynamic_array_appends(m, growth)
    amort = total / m
    print(f"Dynamic Array (growth x{growth}): total={total}, amortized≈{amort:.3f}")

    # גרף 1: כל הפעולות (כולל resize)
    fig1 = plt.figure()
    xs1 = np.arange(1, len(costs_all)+1)
    plt.plot(xs1, np.cumsum(costs_all))
    plt.xlabel("מספר פעולות בפועל (resize + append)")
    plt.ylabel("עלות מצטברת")
    plt.title("Dynamic Array: כל הפעולות")
    save_or_show(fig1, f"dynamic_array_all_ops_x{growth}", save)

    # גרף 2: אחרי כל append בלבד (אורך = m)
    fig2 = plt.figure()
    xs2 = np.arange(1, m+1)
    plt.plot(xs2, cum_after_each)
    plt.xlabel("מספר הוספות (m)")
    plt.ylabel("עלות מצטברת לאחר כל append")
    plt.title("Dynamic Array: עלות מצטברת לפי הוספות")
    save_or_show(fig2, f"dynamic_array_after_each_append_x{growth}", save)

# ---------- 3) Clearable Table ----------
class LazyClearTable:
    def __init__(self, n: int):
        self.n = n
        self.values = [0]*n
        self.stamp  = [0]*n
        self.current_stamp = 1
    def clear(self):
        self.current_stamp += 1  # O(1)
    def set(self, i: int, x: int):
        self.values[i] = x
        self.stamp[i] = self.current_stamp
    def get(self, i: int) -> int:
        return self.values[i] if self.stamp[i] == self.current_stamp else 0

def demo_lazy_clear(n=10, rounds=5):
    t = LazyClearTable(n)
    ops = 0
    for r in range(rounds):
        t.clear(); ops += 1
        for i in range(r % n):
            t.set(i, r); ops += 1
        for i in range(r % n):
            _ = t.get(i); ops += 1
    print(f"LazyClearTable: בוצעו ~{ops} פעולות, clear נשאר O(1).")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--save-plots", action="store_true", help="שמור גרפים לתיקיית out/")
    ap.add_argument("--section", choices=["all","counter","dynamic","clear"], default="all")
    ap.add_argument("--m", type=int, default=2000, help="מס' פעולות לסימולציות")
    ap.add_argument("--growth", type=int, default=2, help="פקטור הגדלה למערך הדינמי")
    args = ap.parse_args()

    if args.section in ("all","counter"):
        demo_binary_counter(m=args.m, save=args.save_plots)
    if args.section in ("all","dynamic"):
        demo_dynamic_array(m=args.m, growth=args.growth, save=args.save_plots)
    if args.section in ("all","clear"):
        demo_lazy_clear(n=32, rounds=10)

if __name__ == "__main__":
    main()
