# OAK INTERNATIONAL SCHOOL
# PREMIUM MATHEMATICS ACTIVITY WORKBOOK — CLASS 3
## Grade Level: Cinquième (5ème) / IB MYP 3 (Ages 12–13)
**Academic Year:** 2026–2027 | **Series Version:** OIS-WB-5EME-MYP3-V1.0  
**Programmes:** IB Middle Years Programme (English) & Beninese National APC Curriculum (Français)  

---

## SECTION A — STUDENT INTRODUCTION / INTRODUCTION POUR L'ÉLÈVE

### Unlocking Geometric Elegance and Algebraic Foundations
*Bienvenue en classe de Cinquième / IB MYP 3 à Oak International School !*

In this pivotal academic year, your mathematical universe expands into negative numbers and formal planar properties:
- In **IB MYP 3**, you investigate general algebraic rules (Criterion B), apply scientific notation to astronomical and atomic scales, and construct real-world linear models for distance, speed, and cost (Criterion D).
- In **Beninese 5ème (APC)**, you explore **Situation d'Apprentissage N°2 (Configurations du plan)** and **N°3 (Nombres et calculs)**. You establish the timeless properties of parallel lines cut by a transversal, prove that the angle sum of any triangle is exactly $180^\circ$, and uncover the rotational magic of central symmetry (*symétrie centrale*) and parallelograms.

This workbook is your dual-language toolkit to ensure complete mastery of both programmes without cognitive interference.

---

## SECTION B — BILINGUAL MATHEMATICAL LANGUAGE / GLOSSAIRE BILINGUE

### Angles, Quadrilaterals & Signed Numbers

| English Term | French Equivalent (*Terme Français*) | Mathematical Definition & Symbolic Example | Common Translation Pitfalls |
|---|---|---|---|
| **Directed numbers / Integers** | *Nombres relatifs / Entiers relatifs* | Signed numbers: $\mathbb{Z} = \{\dots, -3, -2, -1, 0, +1, +2, +3, \dots\}$. | In French, *relatif* includes both positive and negative values. |
| **Alternate interior angles** | *Angles alternes-internes* | Non-adjacent angles on opposite sides of a transversal between parallel lines: $\hat{\alpha} = \hat{\beta}$. | In French: *alternes-internes* (never say "angles alternatifs"). |
| **Corresponding angles** | *Angles correspondants* | Angles in matching relative positions at each intersection of two lines with a transversal. | In French: *angles correspondants*. |
| **Vertically opposite angles** | *Angles opposés par le sommet* | Angles formed by two intersecting lines sharing a common vertex: $\hat{1} = \hat{2}$. | In English, often called "vertical angles". |
| **Point reflection / Central symmetry** | *Symétrie centrale* | Transformation through point $O$ where $O$ is the midpoint of $[MM']$: $S_O(M) = M'$. | In English, equivalent to a rotation of $180^\circ$ around point $O$. |
| **Parallelogram** | *Parallélogramme* | A quadrilateral with both pairs of opposite sides parallel and equal. | Diagonals bisect each other (*se coupent en leur milieu*). |
| **Scientific notation** | *Écriture scientifique* | Expression in form $a \times 10^k$, where $1 \le a < 10$ and $k \in \mathbb{Z}$. | French *notation scientifique* has the identical mathematical constraint on $a$. |
| **Order of magnitude** | *Ordre de grandeur* | The power of 10 closest to the numerical value: e.g., $3.8 \times 10^5 \approx 10^5$ or $10^6$. | In French: *ordre de grandeur*. |

---

## SECTION C — SHARED CONCEPTUAL FOUNDATIONS

### Unit Theme: Parallel Lines, Transversals and Triangle Angle Sums

#### 1. Fundamental Theorem of Angles Cut by a Transversal
Let $(d_1)$ and $(d_2)$ be two parallel lines cut by a secant transversal line $(\Delta)$:
- Any pair of **alternate interior angles** (*angles alternes-internes*) are equal.
- Any pair of **corresponding angles** (*angles correspondants*) are equal.
- Conversely: If two lines cut by a transversal form equal alternate interior angles, then the lines are strictly parallel.

```
       (\Delta)
          /
  -------/------- (d1)
        / \ alpha
       /   \
  ----/-----\---- (d2)
     / beta
    /
```

#### 2. Universal Proof: The Angle Sum of a Triangle is $180^\circ$
Consider any triangle $ABC$:
1. Through vertex $A$, construct auxiliary line $(d)$ parallel to side $(BC)$.
2. Line $(d)$ forms two angles with sides $[AB]$ and $[AC]$:
   - Angle $\hat{1}$ is alternate interior to angle $\widehat{ABC}$.
   - Angle $\hat{2}$ is alternate interior to angle $\widehat{ACB}$.
3. Angles $\hat{1}$, $\widehat{BAC}$, and $\hat{2}$ together form a straight angle on line $(d)$:

$$\hat{1} + \widehat{BAC} + \hat{2} = 180^\circ$$

4. Substituting the equal alternate interior angles:

$$\widehat{ABC} + \widehat{BAC} + \widehat{ACB} = 180^\circ$$

This proof is identical in both the IB inquiry continuum and the Beninese NPE guide!

#### 3. Worked Example: Signed Numbers and Precedence
**Problem**: Calculate $A = -15 - (-8) + (+12) - (+20)$.
- **Step 1 (Transform subtractions into additions of opposites)**:
  $$A = -15 + (+8) + (+12) + (-20)$$
- **Step 2 (Group positive and negative integers)**:
  $$A = [(+8) + (+12)] + [(-15) + (-20)]$$
  $$A = (+20) + (-35)$$
- **Step 3 (Calculate final sum)**:
  $$A = -15$$

---

## SECTION D — CONTEXTUALISED BRIDGING ACTIVITIES

### Activity: The Tanguiéta Solar Farm Tracker Alignment

#### 1. Problem Situation
An electrical engineering team is installing dual-axis photovoltaic solar arrays in Tanguiéta (Atacora department).
- Rows of solar panels are mounted along parallel support girders $(L_1)$ and $(L_2)$.
- A sun-tracking mechanical linkage rod $(T)$ crosses girders $(L_1)$ and $(L_2)$ at pivot points $P$ and $Q$.
- A sensor at pivot $P$ records an interior angle between girder $(L_1)$ and linkage $(T)$ of $64^\circ$.
- A robotic actuator at pivot $Q$ must be calibrated to position the lower panel at angle $\theta$ such that the panels remain parallel to prevent shadowing.

#### 2. The IB Perspective (Inquiry into Geometric Models)
- Identify $(L_1)$ and $(L_2)$ as parallel lines.
- Identify linkage $(T)$ as the transversal.
- By geometric angle theorems, the alternate interior angle at $Q$ must equal $64^\circ$.
- If the actuator measures the co-interior (interior on the same side) angle $\phi$:
  $$\phi = 180^\circ - 64^\circ = 116^\circ$$

#### 3. The Beninese APC Perspective (Structured Proof / *Démonstration*)
- *Données* : Les poutres de support $(L_1)$ et $(L_2)$ sont parallèles : $(L_1) \parallel (L_2)$. La tige sécante $(T)$ coupe $(L_1)$ en $P$ et $(L_2)$ en $Q$. L'angle $\widehat{L_1 P Q} = 64^\circ$.
- *Propriété* : Si deux droites parallèles sont coupées par une sécante, alors les angles alternes-internes qu'elles forment ont la même mesure.
- *Calcul et Conclusion* : L'angle alterne-interne $\widehat{P Q L_2}$ et l'angle $\widehat{L_1 P Q}$ sont de même mesure. Donc $\theta = 64^\circ$.
- *Vérification supplémentaire* : Les angles intérieurs d'un même côté sont supplémentaires : $64^\circ + 116^\circ = 180^\circ$.

#### 4. Comparison of Methods
- Both programmes arrive at the exact same angular values ($64^\circ$ and $116^\circ$).
- The Beninese APC demands an explicit reference to the statutory property name (*angles alternes-internes*), while the IB emphasizes functional sensor orientation.

#### 5. Student Reflection Question
*Why is it physically impossible for solar panels mounted on parallel girders to have unequal alternate interior angles without bending the linkage rod?*  
*Espace de réponse:*  
____________________________________________________________________________________________________  
____________________________________________________________________________________________________  

#### 6. Application in a New Context
In an urban development in Abomey-Calavi, two parallel avenues are crossed diagonally by a railway line at an angle of $72^\circ$. Determine all eight angles formed at the two intersections.  
*Working space:*  
____________________________________________________________________________________________________  
____________________________________________________________________________________________________  

---

## SECTION E — PROGRESSIVE PRACTICE / EXERCICES PROGRESSIFS

### Level 1: Foundational Understanding (Signed Numbers & Index Laws)
1. Calculate:
   a) $(-14) + (+9) = $  
   b) $(-8) - (-15) = $  
   c) $(-6) \times (-7) = $  
   d) $(+48) \div (-8) = $  
2. Write in scientific notation ($a \times 10^k$):
   a) $450\ 000 = $  
   b) $0.000\ 78 = $  
   c) The speed of light: $300\ 000\ 000\text{ m/s} = $  
   d) $125 \times 10^4 = $  

### Level 2: Standard Application (Angles & Fractions with Unlike Denominators)
3. Calculate and give the irreducible fraction:
   a) $\frac{3}{4} + \frac{5}{6} = $  
   b) $\frac{7}{10} - \frac{4}{15} = $  
   c) $\frac{5}{8} \times \frac{16}{25} = $  
4. In triangle $KLM$, angle $\hat{K} = 58^\circ$ and angle $\hat{L} = 74^\circ$.
   a) Calculate the measure of angle $\hat{M}$.  
   b) Is triangle $KLM$ acute, right-angled, or obtuse? Justify.  

### Level 3: Multi-Step Problems (Central Symmetry & Parallelograms)
5. Let $ABCD$ be a parallelogram with centre $O$.
   a) What is the image of vertex $A$ under the central symmetry $S_O$?  
   b) What is the image of segment $[AB]$ under $S_O$?  
   c) Prove that line $(AB)$ is parallel to line $(CD)$ using the properties of central symmetry.  
6. **Proportionality and Journey Rates**:
   A refrigerated truck carrying fish from Cotonou to Malanville travels $720\text{ km}$.
   - The truck maintains a constant average speed of $60\text{ km/h}$.
   - Fuel consumption is directly proportional to distance: $18\text{ litres}$ per $100\text{ km}$.
   a) Calculate the total travel time in hours.  
   b) Calculate the total volume of diesel consumed.  
   c) If diesel costs $650\text{ CFA F}$ per litre, calculate the total fuel expenditure.  

### Level 4: Reasoning & Geometric Proof
7. In the figure below, lines $(AB)$ and $(CD)$ are parallel. Triangle $CDE$ is isosceles at $C$.
   Angle $\widehat{BAC} = 45^\circ$ and angle $\widehat{ACD} = 45^\circ$.
   Line $(AC)$ is a transversal.
   Angle $\widehat{CDE} = 70^\circ$.
   a) Prove that triangle $ACD$ is right-angled if $\widehat{ADC} = 45^\circ$.  
   b) Calculate the measures of all three interior angles of triangle $CDE$.  
   c) Write a structured proof for each deduced angle.  

### Level 5: Extension & 5ème National Examination Challenge
8. **Situation d'Évaluation Type 5ème (SA N°2 & N°4)**:
   Pour sécuriser un domaine agricole à Savè, un géomètre implante quatre bornes $M, N, P, Q$.
   Il vérifie sur le terrain que le point $I$ est le milieu commun des segments $[MP]$ et $[NQ]$.
   De plus, il mesure $MN = 145\text{ m}$ et $\widehat{MNP} = 65^\circ$.
   1. Fais une figure géométrique soignée représentant cette situation (échelle $1\text{ cm}$ pour $20\text{ m}$).
   2. Démontre que le quadrilatère $MNPQ$ est un parallélogramme.
   3. Déduis-en la longueur exacte du côté $[PQ]$ sans nouvelle mesure.
   4. Démontre que les droites $(MN)$ et $(PQ)$ sont strictement parallèles.
   5. Détermine la mesure de l'angle $\widehat{NPQ}$.

---

## SECTION F — INTEGRATED APPLICATION TASKS

### Task F-1: The Songhaï Bio-Gas Digester Network (MYP Criterion D & Benin SA 5)
**Context**: The Songhaï Agricultural Innovation Centre in Porto-Novo generates renewable bio-gas from agricultural biomass to power a collective bakery and dairy processing unit.
- The underground main gas pipe runs along straight line $(G_1)$.
- A branch line $(G_2)$ is laid parallel to $(G_1)$.
- A cross-connecting pipe $(C)$ intersects $(G_1)$ at valve $V_1$ and $(G_2)$ at valve $V_2$.
- At valve $V_1$, the connecting pipe forms an acute angle of $52^\circ$ with line $(G_1)$.
- The pipe length $V_1 V_2 = 85\text{ metres}$.

**Questions**:
1. Draw a schematic diagram of the pipe network labelling $(G_1)$, $(G_2)$, and transversal $(C)$.
2. State the measure of the alternate interior angle at valve $V_2$ and justify using the appropriate theorem.
3. Determine the obtuse angle formed by the cross-connector $(C)$ and line $(G_2)$.
4. Gas flows through the cross-connector at an average speed of $2.5\text{ m/s}$. Calculate how many seconds it takes for gas to travel from $V_1$ to $V_2$.
5. If the daily gas production is $450\text{ m}^3$ and the bakery consumes $\frac{5}{9}$ of this production, calculate the volume of gas remaining for the dairy unit.

---

## SECTION G — PROGRAMME-SPECIFIC REINFORCEMENT

### Part G-1: IB MYP 3 Criterion B Pattern Investigation
**Investigation: Consecutive Angle Bisector Grids**  
Consider a sequence of regular polygons:
- Equilateral triangle (3 sides): Interior angle sum = $180^\circ$.
- Quadrilateral (4 sides): Interior angle sum = $360^\circ$.
- Pentagon (5 sides): Interior angle sum = $540^\circ$.
1. Record values in a table for polygons with $n = 3, 4, 5, 6, 7, 8$ sides.
2. Formulate a general rule for the sum of interior angles $S$ in terms of number of sides $n$.
3. Test and justify your general rule using triangulation from a single vertex.
4. Calculate the interior angle sum of a polygon with 24 sides (icositetragon).

### Part G-2: Beninese NPE Formal Proof Exercise
**Exercice de Démonstration Formelle (Classe de 5ème)**  
Soit un triangle $ABC$. Soit $I$ le milieu de $[AB]$ et $J$ le milieu de $[AC]$.
Soit $K$ le symétrique de $I$ par rapport au point $J$.
1. Démontre que le quadrilatère $AICK$ est un parallélogramme.
2. Déduis-en que les segments $[CK]$ et $[AI]$ sont parallèles et de même longueur.
3. Démontre ensuite que le quadrilatère $BCKI$ est un parallélogramme.
*Rédige rigoureusement chaque étape avec les propriétés de la symétrie centrale.*

---

## SECTION H — ASSESSMENT, REFLECTION & WORKED SOLUTIONS

### Diagnostic Pre-Flight Check
- [ ] I can add and subtract negative numbers with confidence.
- [ ] I can find a common denominator for two fractions (e.g., 4 and 6 $\to$ 12).
- [ ] I know that alternate interior angles between parallel lines are equal.
- [ ] I know that the diagonals of a parallelogram bisect each other.

---

### COMPLETE WORKED SOLUTIONS & MARKING SCHEME

#### Solutions for Section E (Progressive Practice)
1. **Signed Operations** (1 mark each):
   a) $-14 + 9 = -5$  
   b) $-8 + 15 = +7$  
   c) $(-6) \times (-7) = +42$  
   d) $48 \div (-8) = -6$  
2. **Scientific Notation** (1 mark each):
   a) $4.5 \times 10^5$  
   b) $7.8 \times 10^{-4}$  
   c) $3.0 \times 10^8\text{ m/s}$  
   d) $1.25 \times 10^6$  
3. **Fractions Unlike Denominators** (1 mark each):
   a) $\frac{3 \times 3}{12} + \frac{5 \times 2}{12} = \frac{9+10}{12} = \frac{19}{12}$.  
   b) $\frac{7 \times 3}{30} - \frac{4 \times 2}{30} = \frac{21-8}{30} = \frac{13}{30}$.  
   c) $\frac{5 \times 16}{8 \times 25} = \frac{1 \times 2}{1 \times 5} = \frac{2}{5}$.  
4. **Triangle Angles** (2 marks):
   a) $\hat{M} = 180^\circ - (58^\circ + 74^\circ) = 180^\circ - 132^\circ = 48^\circ$.  
   b) All three angles are strictly less than $90^\circ$ ($58^\circ, 74^\circ, 48^\circ < 90^\circ$); therefore, triangle $KLM$ is an acute-angled triangle (*triangle acutangle*).  
5. **Parallelogram Central Symmetry** (3 marks):
   a) Under $S_O$, the image of $A$ is $C$ (since $O$ is the midpoint of $[AC]$).  
   b) Under $S_O$, the image of $B$ is $D$. Thus, the image of segment $[AB]$ is segment $[CD]$.  
   c) Central symmetry transforms any straight line into a line parallel to itself. Therefore, line $(AB)$ is strictly parallel to line $(CD)$.  
6. **Refrigerated Truck** (3 marks):
   a) Travel time: $t = \frac{d}{v} = \frac{720}{60} = 12\text{ hours}$.  
   b) Diesel volume: $\frac{720 \times 18}{100} = 7.2 \times 18 = 129.6\text{ litres}$.  
   c) Expenditure: $129.6 \times 650 = 84\ 240\text{ CFA F}$.  
7. **Angle Reasoning** (4 marks):
   a) In $\triangle ACD$, angles are $45^\circ, 45^\circ$. Sum = $90^\circ$. Remaining angle $\widehat{ADC} = 180^\circ - 90^\circ = 90^\circ$. Right-angled at $D$.  
   b) In $\triangle CDE$ isosceles at $C$, base angles $\widehat{CDE} = \widehat{CED} = 70^\circ$.  
      Vertex angle $\widehat{DCE} = 180^\circ - (70^\circ + 70^\circ) = 40^\circ$.  
8. **Savè Farm 5ème Task** (5 marks):
   1. Scale diagram ($145\text{ m} \to 7.25\text{ cm}$). [1 mark]
   2. Segments $[MP]$ and $[NQ]$ have the same midpoint $I$. A quadrilateral whose diagonals bisect each other is a parallelogram. Thus, $MNPQ$ is a parallelogram. [2 marks]
   3. In a parallelogram, opposite sides are equal in length. Hence $PQ = MN = 145\text{ m}$. [1 mark]
   4. In a parallelogram, opposite sides are parallel. Hence $(MN) \parallel (PQ)$. [1 mark]

#### Solutions for Section F (Task F-1: Songhaï Bio-Gas)
1. Labeled schematic diagram. [1 mark]
2. Alternate interior angle at $V_2 = 52^\circ$, because $(G_1) \parallel (G_2)$ cut by transversal $(C)$. [2 marks]
3. Obtuse supplementary angle: $180^\circ - 52^\circ = 128^\circ$. [1 mark]
4. Transit time: $t = \frac{d}{v} = \frac{85}{2.5} = 34\text{ seconds}$. [2 marks]
5. Gas remaining: $\frac{5}{9} \times 450 = 250\text{ m}^3$ used by bakery. Remaining = $450 - 250 = 200\text{ m}^3$. [2 marks]

#### Solutions for Section G-2 (Benin Formal Proof 5ème)
1. *Démonstration AICK* : $J$ est le milieu de $[AC]$ (par hypothèse) et $J$ est le milieu de $[IK]$ (car $K$ est le symétrique de $I$ par rapport à $J$). Le quadrilatère $AICK$ a ses diagonales $[AC]$ et $[IK]$ qui se coupent en leur milieu $J$ ; c'est donc un parallélogramme. [2 pts]
2. *Conséquence* : Puisque $AICK$ est un parallélogramme, ses côtés opposés $[CK]$ et $[AI]$ sont parallèles et de même longueur : $(CK) \parallel (AI)$ et $CK = AI$. [1 pt]
3. *Démonstration BCKI* : On sait que $I$ est le milieu de $[AB]$, donc $AI = IB$, et les points $A, I, B$ sont alignés. Comme $CK = AI$, on a aussi $CK = IB$. De plus, comme $(CK) \parallel (AI)$ et que $B \in (AI)$, on a $(CK) \parallel (IB)$. Le quadrilatère $BCKI$ possède deux côtés opposés $[CK]$ et $[IB]$ qui sont parallèles et de même longueur ; c'est donc un parallélogramme. [2 pts]

---
*End of Workbook 3 (Cinquième / MYP 3).*
