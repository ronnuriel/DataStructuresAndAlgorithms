# 📚 שיעור: תורי עדיפויות (Priority Queues) ו־Binary Heaps — סיכום מלא
**מה יש בחבילה:**
- `priority_queues_heaps.ipynb` — מחברת **Jupyter** עם הסברים בעברית + תאי קוד רצים.
- `priority_queues_heaps.py` — מימוש **Min-Binary-Heap** (insert / find-min / delete-min / decrease-key) + build-heap + heapsort + בדיקות.
- README זה — סיכום תמציתי + הוראות הרצה.

> תואם למצגת “Priority Queues / Binary Heaps”: הגדרות, עץ בינארי כמעט־מלא, פעולות, Build-Heap ב־O(n), Heapsort ב־O(n log n).

---

## 🔎 מה זה Priority Queue?
ADT שמנהל אוסף איברים כשכל איבר מקבל **מפתח (key)** — עדיפות.  
פעולות עיקריות:
- `insert(x, k)`
- `find-min()`
- `delete-min()`
- `decrease-key(x, k)`

### מימושים נפוצים
| מבנה | insert | find-min | delete-min | decrease-key |
|------|--------|----------|------------|--------------|
| רשימה לא־ממוינת | O(1) | O(n) | O(n) | O(1) |
| רשימה ממוינת | O(n) | O(1) | O(1) | O(n) |
| **Binary Heap** | **O(log n)** | **O(1)** | **O(log n)** | **O(log n)** |

---

## 🌲 Binary Heap (ערימה בינארית)
- עץ בינארי **כמעט־מלא** (Almost-complete)
- **Min-Heap**: כל צומת ≤ ילדיו ⇒ המינימום בשורש.
- גובה העץ: `⌊log₂ n⌋`

### אינטואיציות על פעולות
- `insert` — מוסיפים בסוף ה־array ומרימים למעלה (sift-up) ⇒ O(log n)
- `delete-min` — מחליפים שורש עם אחרון, מסירים, ומורידים למטה (sift-down) ⇒ O(log n)
- `decrease-key` — מקטינים מפתח למעלה דרך sift-up ⇒ O(log n)
- `find-min` — לוקחים את השורש ⇒ O(1)

---

## 🧰 Build-Heap ב־O(n)
- מתחילים ממערך שרירותי בגודל n.
- “חושבים עליו” כעל ערימה בינארית (ללא תכונת heap).
- **מחלחלים מטה** (sift-down) מכל אינדקס `i = ⌊n/2⌋-1 .. 0`.
- הניתוח: סכום הגבהים לכל צומת נותן \(\sum_{h=0}^{\lfloor\log n\rfloor} (n/2^{h+1}) \cdot O(h) = O(n)\).

---

## 🧹 Heapsort
1. Build-Heap ב־O(n)
2. מבצעים n פעמים `delete-min` ⇒ O(n log n)
3. מקבלים סדר עולה (ללא זיכרון נוסף אם עובדים in-place עם max-heap)

---

## ▶️ איך מריצים
### מחברת Jupyter
```bash
jupyter notebook priority_queues_heaps.ipynb
```

### סקריפט Python (עם בדיקות קטנות)
```bash
python priority_queues_heaps.py
```

---

## 🧠 טיפים
- להרגיש את הפעולות: שנו seed, צרו נתונים רנדומליים, בדקו שמירת תכונת heap.
- `decrease-key` דורש **מפה item→index** כדי למצוא את האיבר ב־O(1) לפני הרמה למעלה.

בהצלחה! ✨
