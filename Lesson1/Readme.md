# Lesson 1 – Induction & Asymptotics
### שיעור 1 — אינדוקציה ואסימפטוטיקה

## 🇬🇧 Summary
- **Proof by Induction:** Base case → Inductive hypothesis → Inductive step.  
  Variants: *weak induction* and *strong induction* (use previous results up to n).  
- **Asymptotic Notation:**  
  - Big‑O upper bound; Big‑Ω lower bound; Big‑Θ tight bound.  
  - Little‑o (strictly smaller order), little‑ω (strictly larger order).  
- **Common Orders:** `1 < log n < n < n log n < n^2 < n^3 < 2^n < n!` (for large n).  
- **Rules:** transitivity, sum rule (max), product rule, polynomials vs exponentials, logs bases differ by constants.  
- **Pitfalls:** forgetting constants/threshold `n0`, proving only one side (O but not Ω), mixing pointwise with asymptotic claims.

## 🇮🇱 סיכום
- **הוכחה באינדוקציה:** צעד בסיס → הנחת אינדוקציה → צעד אינדוקטיבי.  
  גרסאות: אינדוקציה חלשה/חזקה.  
- **סימונים אסימפטוטיים:**  
  - Big‑O חסם עליון; Big‑Ω חסם תחתון; Big‑Θ חסם הדוק.  
  - little‑o קטן ממש; little‑ω גדול ממש.  
- **סדרי גידול נפוצים:** `1 < log n < n < n log n < n^2 < n^3 < 2^n < n!` עבור n גדול.  
- **כללי אצבע:** סכום נשלט ע״י הגודל הגדול יותר; כפל מכפיל סדרי גידול; פולינום < מעריכי; בסיסי לוג שונים נבדלים בקבוע.  
- **מוקשים:** להשמיט קבועים/סף, להוכיח רק O בלי Ω, בלבול בין שוויון נקודתי לבין גבולות אסימפטוטיים.

> See the notebook for hands‑on examples (plots, ratio tests) and worked induction proofs.
