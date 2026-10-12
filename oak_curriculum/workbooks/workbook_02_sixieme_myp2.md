# OAK INTERNATIONAL SCHOOL
# PREMIUM MATHEMATICS ACTIVITY WORKBOOK — CLASS 2
## Grade Level: Sixième (6ème) / IB MYP 2 (Ages 11–12)
**Academic Year:** 2026–2027 | **Series Version:** OIS-WB-6EME-MYP2-V1.0  
**Programmes:** IB Middle Years Programme (English) & Beninese National APC Curriculum (Français)  

---

## SECTION A — STUDENT INTRODUCTION / INTRODUCTION POUR L'ÉLÈVE

### Stepping into Secondary Mathematics Excellence
*Entrée dans l'excellence mathématique du premier cycle secondaire à Oak International School !*

In Sixième / MYP 2, mathematics shifts from simple arithmetic into the wonderful realm of deductive reasoning and formal geometry:
- In **IB MYP 2**, you explore how symmetry and spatial relations govern natural structures and architecture, learning to communicate lines of reasoning (Criterion C) and investigate general algebraic patterns (Criterion B).
- In **Beninese 6ème (APC)**, you discover the statutory power of **Situation d'Apprentissage N°1 (Configurations du plan)** and **N°5 (Symétrie orthogonale)**. You learn the formal structure of geometric proof (*démonstration géométrique*), moving from simple observation to absolute mathematical proof.

This workbook unites both traditions: you will master precise French axiomatic phrasing alongside versatile English mathematical inquiry.

---

## SECTION B — BILINGUAL MATHEMATICAL LANGUAGE / GLOSSAIRE BILINGUE

### Planar Geometry, Symmetry & Number Theory

| English Term | French Equivalent (*Terme Français*) | Mathematical Definition & Symbolic Example | Common Translation Pitfalls |
|---|---|---|---|
| **Straight line** | *Droite* | An infinite one-dimensional set of points: $(d)$ or $(AB)$. | Do not confuse with "line segment" (*segment*) $[AB]$ which has finite length. |
| **Ray** | *Demi-droite* | A portion of a line starting at endpoint $A$ and extending infinitely through $B$: $[AB)$. | Note bracket convention: square bracket at closed origin $[$, parenthesis at infinite end $)$. |
| **Perpendicular bisector** | *Médiatrice d'un segment* | The line perpendicular to a segment at its midpoint: $(\Delta) \perp [AB]$ at $I$ with $IA = IB$. | False friend: do not confuse with *médiane* (median) or *bissectrice* (angle bisector). |
| **Axial symmetry / Reflection** | *Symétrie axiale / orthogonale* | Transformation across line $(d)$ where $(d)$ is the perpendicular bisector of $[MM']$: $S_{(d)}(M) = M'$. | In French, specifically designated *symétrie orthogonale par rapport à une droite*. |
| **Collinear points** | *Points alignés* | Three or more points that lie on the same straight line: $A, B, C \in (d)$. | In French, always say *« les points sont alignés »*, not "collinéaires". |
| **Prime number** | *Nombre premier* | An integer $p > 1$ whose only positive divisors are $1$ and $p$: $2, 3, 5, 7, 11, 13, \dots$. | 1 is neither prime nor composite in both languages! |
| **Highest Common Factor (HCF)** | *Plus Grand Commun Diviseur (PGCD)* | The greatest integer that divides each of two or more numbers: $\text{HCF}(24, 36) = 12$. | Note abbreviation inversion: HCF (or GCD) in English vs PGCD in French. |
| **Lowest Common Multiple (LCM)** | *Plus Petit Commun Multiple (PPCM)* | The smallest positive integer divisible by both numbers: $\text{LCM}(4, 6) = 12$. | In French: PPCM. |

---

## SECTION C — SHARED CONCEPTUAL FOUNDATIONS

### Unit Theme: Perpendicular Bisectors, Circles and Axial Symmetry

#### 1. The Perpendicular Bisector: Dual Definitions
In both curricula, the perpendicular bisector $(\Delta)$ of a segment $[AB]$ possesses two equivalent definitions:
1. **Geometric Definition**: The straight line perpendicular to segment $[AB]$ passing through its midpoint $I$.
2. **Locus of Equidistance (Caractérisation par l'équidistance)**: The set of all points $M$ in the plane that are equidistant from the endpoints $A$ and $B$:

$$M \in (\Delta) \iff MA = MB$$

This property is the foundation of circle circumscription: the centre of the circle passing through three non-collinear points is the intersection of their perpendicular bisectors.

#### 2. Axial Symmetry (Orthogonal Reflection) and Invariance
When a plane figure is reflected across an axis of symmetry $(d)$:
- Distances are conserved: $A'B' = AB$ (isometry).
- Alignment is conserved: if $A, B, C$ are collinear, their images $A', B', C'$ are collinear.
- Angles are conserved: $\widehat{A'B'C'} = \widehat{ABC}$.
- Surface areas are conserved: $\text{Area}(F') = \text{Area}(F)$.

#### 3. Worked Example: Constructing and Proving Symmetries
**Problem**: Let $(d)$ be a straight line and $A$ a point not on $(d)$. $A'$ is the symmetric image of $A$ with respect to $(d)$. Point $M$ lies on $(d)$. Prove that triangle $MAA'$ is isosceles.

- **The Beninese APC Deductive Proof Format (*Démonstration en 3 étapes*)**:
  - *Données (On sait que)* : $A'$ est le symétrique de $A$ par rapport à la droite $(d)$, et le point $M$ appartient à $(d)$.
  - *Propriété (Or si)* : La symétrie orthogonale par rapport à une droite conserve les distances, et tout point situé sur l'axe de symétrie est son propre symétrique ($S_{(d)}(M) = M$).
  - *Conclusion (Donc)* : $MA = MA'$, ce qui prouve que le triangle $MAA'$ est un triangle isocèle en $M$.
- **The IB MYP Reasoning Format (Criterion C)**:
  - By definition of reflection across axis $(d)$, $(d)$ is the perpendicular bisector of segment $[AA']$.
  - Since point $M$ lies on the perpendicular bisector $(d)$, it is equidistant from both endpoints: $MA = MA'$.
  - Therefore, triangle $MAA'$ has two equal sides, which satisfies the definition of an isosceles triangle with vertex $M$.

---

## SECTION D — CONTEXTUALISED BRIDGING ACTIVITIES

### Activity: Designing an Eco-Tourism Dock in Ganvié (Lake Nokoué)

#### 1. Problem Situation
The community council of Ganvié (the stilt village on Lake Nokoué) wishes to construct a solar-powered charging dock $D$ along a straight water channel $(L)$ to service two schools of watercraft stationed at locations $A$ and $B$ on the same side of the channel.
To minimise electrical cabling and transit times, the council must determine the exact point $D$ on line $(L)$ such that the sum of distances $DA + DB$ is minimized.

#### 2. The IB Perspective (Inquiry into Geometric Transformation)
- Reflect point $B$ across the channel line $(L)$ to create its mirror image $B'$.
- For any point $X$ on $(L)$, $XB = XB'$.
- Therefore, $XA + XB = XA + XB'$.
- The shortest distance between two points $A$ and $B'$ in a Euclidean plane is a straight line segment $[AB']$.
- The optimal dock location $D$ is the intersection of line $(AB')$ and channel line $(L)$.

#### 3. The Beninese APC Perspective (Construction & Formal Justification)
- *Construction géométrique* :
  1. Construire le point $B'$, symétrique orthogonal du point $B$ par rapport à la droite $(L)$.
  2. Tracer la droite $(AB')$.
  3. Marquer le point d'intersection $D = (AB') \cap (L)$.
- *Démonstration de minimalité* :
  - Soit $M$ un point quelconque de la droite $(L)$ distinct de $D$.
  - Puisque $M \in (L)$ et que $(L)$ est l'axe de symétrie échangeant $B$ et $B'$, on a $MB = MB'$.
  - De même, $D \in (L)$, donc $DB = DB'$.
  - La longueur du trajet passant par $D$ est $DA + DB = DA + DB' = AB'$ (car $A, D, B'$ sont alignés dans cet ordre).
  - La longueur du trajet passant par $M$ est $MA + MB = MA + MB'$.
  - D'après l'inégalité triangulaire dans le triangle $AMB'$ : $MA + MB' \ge AB' = DA + DB$.
  - Le point $D$ réalise donc le minimum absolu de la distance totale.

#### 4. Comparison of Methods
- IB guides students through an intuitive spatial transformation and shortest-path principle.
- Beninese APC requires formal construction commands with ruler and compass and an explicit triangular inequality proof.

#### 5. Student Reflection Question
*Why does replacing $B$ with its symmetric image $B'$ allow us to transform a bent two-part path ($AD + DB$) into a single straight line ($AB'$)?*  
*Espace de réponse:*  
____________________________________________________________________________________________________  
____________________________________________________________________________________________________  

#### 6. Application in a New Context
Two telecom relay antennas $P$ and $Q$ in the Collines department are situated on the same side of the National Interstate Highway RNIE 2 (modelled as line $H$). Find the location on $H$ for a shared solar generator that minimizes cable installation costs.  
*Working space:*  
____________________________________________________________________________________________________  
____________________________________________________________________________________________________  

---

## SECTION E — PROGRESSIVE PRACTICE / EXERCICES PROGRESSIFS

### Level 1: Foundational Understanding (Terminology & Divisibility)
1. Complete with the appropriate mathematical symbol ($\in, \notin, \perp, \parallel$):
   a) Point $M$ lies on line $(d)$: $M \_\_\_\_\_ (d)$  
   b) Point $P$ does not belong to segment $[AB]$: $P \_\_\_\_\_ [AB]$  
   c) Line $(d_1)$ is perpendicular to line $(d_2)$: $(d_1) \_\_\_\_\_ (d_2)$  
   d) Line $(L_1)$ is parallel to line $(L_2)$: $(L_1) \_\_\_\_\_ (L_2)$  
2. Divisibility criteria: Among the numbers $135$, $240$, $312$, $505$, $729$:
   a) Which are divisible by $2$?  
   b) Which are divisible by $3$?  
   c) Which are divisible by $5$?  
   d) Which are divisible by $9$?  

### Level 2: Standard Application (Constructions & Prime Decomposition)
3. Decompose into a product of prime factors:
   a) $72 = $  
   b) $108 = $  
   c) Determine $\text{PGCD}(72, 108)$ and $\text{PPCM}(72, 108)$.  
4. On a blank sheet or in your notebook:
   a) Draw a segment $[AB]$ of length $6\text{ cm}$.  
   b) Using a compass and straightedge, construct the perpendicular bisector $(\Delta)$ of $[AB]$.  
   c) Mark a point $P$ on $(\Delta)$ such that $IP = 4\text{ cm}$, where $I$ is the midpoint of $[AB]$.  
   d) Measure $PA$ and $PB$. State their values and verify the equidistance property.  

### Level 3: Multi-Step Problems (Fractions & Directed Numbers Bridging)
5. Calculate and give the answer in simplest form:
   a) $\frac{5}{12} \times \frac{18}{25} = $  
   b) $\frac{7}{4} \div \frac{21}{8} = $  
   c) $\frac{3}{5} + \frac{2}{5} \times \frac{1}{4} = $ (Remember order of operations!).  
6. **Bridging Module: Directed Integers**:
   Evaluate:
   a) $(+8) + (-5) = $  
   b) $(-12) + (-7) = $  
   c) $(+6) - (+14) = $  
   d) $(-9) - (-15) = $  

### Level 4: Reasoning & Geometric Proof
7. Let $[AB]$ be a line segment with midpoint $O$. Line $(d)$ is perpendicular to $(AB)$ at $O$.
   Let $M$ be a point on $(d)$ distinct from $O$.
   Let $M'$ be the symmetric image of $M$ with respect to the line $(AB)$.
   a) What is the nature of quadrilateral $MAM'B$?  
   b) Write a structured geometric proof showing that the four sides of $MAM'B$ have equal lengths.  
   c) Deduce the specific geometric name of this quadrilateral.  

### Level 5: Extension & 6ème National Examination Challenge
8. **Situation d'Évaluation Type 6ème (SA N°1 & N°5)**:
   Dans la commune de Savalou, un artisan forgeron conçoit une grille de portail décorative.
   Sur sa feuille de dessin, il trace une droite $(d)$ et place deux points $E$ et $F$ de part et d'autre de $(d)$ tels que la droite $(EF)$ coupe $(d)$ au point $K$ non perpendiculairement.
   Il construit ensuite les points $E'$ et $F'$, symétriques respectifs de $E$ et $F$ par rapport à $(d)$.
   1. Fais une figure géométrique soignée respectant les consignes ci-dessus.
   2. Démontre que le point $K$ est son propre symétrique par rapport à la droite $(d)$.
   3. Démontre que les points $E', K, F'$ sont alignés.
   4. Sachant que $EF = 8,5\text{ cm}$, détermine la longueur du segment $[E'F']$ en justifiant par la propriété appropriée.

---

## SECTION F — INTEGRATED APPLICATION TASKS

### Task F-1: The Traditional Kanvo Weaving Loom (MYP Criterion B & C)
**Context**: In Abomey, traditional weavers produce *Kanvo* (royal woven fabric) using geometric strip patterns with reflectional symmetries.
A master weaver creates a border design by repeating a symmetrical motif:
- Pattern 1 uses 4 white threads and 1 red central core.
- Pattern 2 uses 8 white threads and 2 red central cores.
- Pattern 3 uses 12 white threads and 3 red central cores.

**Questions**:
1. Organize the data into a table showing Pattern Number ($n$), Red Cores ($R$), and White Threads ($W$) for $n = 1, 2, 3, 4, 5$.
2. State the mathematical relationship between the pattern number $n$ and the number of white threads $W$.
3. Write a general formula for $W$ in terms of $n$.
4. The weaver uses a spool containing 160 white threads. What is the maximum pattern size $n$ that can be completed?
5. Explain how axial symmetry ensures that the fabric maintains balanced tension along both edges.

---

## SECTION G — PROGRAMME-SPECIFIC REINFORCEMENT

### Part G-1: IB MYP 2 Criterion C Communication Task
Write a formal, mathematically rigorous explanation (using full English sentences and standard symbols) explaining why a circle has an infinite number of axes of symmetry, whereas a regular hexagon has exactly six axes of symmetry.

### Part G-2: Beninese National Curriculum Geometric Proof
**Exercice de Démonstration Formelle**  
Soit un triangle $ABC$ isocèle en $A$. Soit $(d)$ la médiatrice de la base $[BC]$.
1. Démontre que le point $A$ appartient à la droite $(d)$.
2. Démontre que la droite $(d)$ est également la bissectrice de l'angle $\widehat{BAC}$.
*Rédige la démonstration selon le modèle officiel : Données / Propriété / Conclusion.*

---

## SECTION H — ASSESSMENT, REFLECTION & WORKED SOLUTIONS

### Diagnostic Pre-Flight Check
- [ ] I can construct a perpendicular bisector using a compass and straightedge.
- [ ] I know the divisibility rule for 9 (sum of digits is a multiple of 9).
- [ ] I can find the symmetric point of $A$ across a line $(d)$.
- [ ] I can calculate with negative numbers on a number line.

---

### COMPLETE WORKED SOLUTIONS & MARKING SCHEME

#### Solutions for Section E (Progressive Practice)
1. **Mathematical Symbols** (1 mark each):
   a) $M \in (d)$  
   b) $P \notin [AB]$  
   c) $(d_1) \perp (d_2)$  
   d) $(L_1) \parallel (L_2)$  
2. **Divisibility Tests** (1 mark each):
   a) Divisible by 2 (even unit digit): $240, 312$.  
   b) Divisible by 3 (sum of digits multiple of 3): $135$ ($1+3+5=9$), $240$ ($6$), $312$ ($6$), $729$ ($18$). All four!  
   c) Divisible by 5 (ends in 0 or 5): $135, 240, 505$.  
   d) Divisible by 9 (sum of digits multiple of 9): $135$ ($9$), $729$ ($18$).  
3. **Prime Factorisation** (1 mark each):
   a) $72 = 2^3 \times 3^2$.  
   b) $108 = 2^2 \times 3^3$.  
   c) $\text{PGCD}(72, 108) = 2^2 \times 3^2 = 4 \times 9 = 36$.  
      $\text{PPCM}(72, 108) = 2^3 \times 3^3 = 8 \times 27 = 216$. [2 marks]
4. **Constructions**: Correct verified construction of perpendicular bisector with arcs, $PA = PB = 5\text{ cm}$ (by Pythagoras $\sqrt{3^2+4^2}=5$). [3 marks]
5. **Fraction Operations** (1 mark each):
   a) $\frac{5 \times 18}{12 \times 25} = \frac{1 \times 3}{2 \times 5} = \frac{3}{10}$.  
   b) $\frac{7}{4} \times \frac{8}{21} = \frac{1 \times 2}{1 \times 3} = \frac{2}{3}$.  
   c) $\frac{3}{5} + \frac{2}{20} = \frac{3}{5} + \frac{1}{10} = \frac{6+1}{10} = \frac{7}{10}$.  
6. **Directed Numbers** (1 mark each):
   a) $+3$  
   b) $-19$  
   c) $-8$  
   d) $-9 + 15 = +6$  
7. **Geometric Proof for Quadrilateral $MAM'B$** (4 marks):
   - $M$ lies on $(d)$, which is the perpendicular bisector of $[AB]$, so $MA = MB$.
   - $M'$ is the reflection of $M$ across $(AB)$, so $(AB)$ is the perpendicular bisector of $[MM']$. Hence $AM = AM'$ and $BM = BM'$.
   - Therefore, $MA = MB = AM' = BM'$.
   - A quadrilateral with four equal sides is a rhombus (*losange*).
8. **Savalou Artisan 6ème Task** (5 marks):
   1. Accurate geometric diagram. [1 mark]
   2. $K = (EF) \cap (d)$, therefore $K \in (d)$. Any point lying on the axis of symmetry is invariant (its own symmetric image): $S_{(d)}(K) = K$. [1 mark]
   3. The reflection of point $E$ is $E'$, the reflection of $F$ is $F'$, and the reflection of $K$ is $K$. Since $E, K, F$ are collinear (lying on the same line), and orthogonal symmetry preserves alignment, their symmetric images $E', K, F'$ are collinear. [2 marks]
   4. Orthogonal symmetry preserves distances. Therefore, $E'F' = EF = 8.5\text{ cm}$. [1 mark]

#### Solutions for Section F (Task F-1: Kanvo Loom)
1. Table values: $n=1 \to W=4$; $n=2 \to W=8$; $n=3 \to W=12$; $n=4 \to W=16$; $n=5 \to W=20$. [2 marks]
2. The number of white threads is directly proportional to $n$, with a constant factor of 4. [1 mark]
3. Formula: $W = 4n$. [1 mark]
4. Setting $4n \le 160 \implies n \le 40$. The weaver can complete up to Pattern 40. [2 marks]
5. Axial symmetry balances thread tension equally across both sides of the central core, preventing warping or curling of the fabric edges. [2 marks]

#### Solutions for Section G-2 (Benin Formal Geometric Proof)
- *Données* : Le triangle $ABC$ est isocèle en $A$, donc $AB = AC$. $(d)$ est la médiatrice de $[BC]$. [1 pt]
- *Propriété* : La médiatrice d'un segment est le lieu géométrique des points équidistants des extrémités de ce segment. [1 pt]
- *Conclusion 1* : Comme $AB = AC$, le point $A$ est équidistant de $B$ et $C$, donc $A$ appartient à la médiatrice $(d)$. [1 pt]
- *Démonstration bissectrice* : Soit $I$ le milieu de $[BC]$. La droite $(d)$ passe par $A$ et $I$. Dans le triangle $ABC$ isocèle en $A$, la médiatrice de la base est aussi un axe de symétrie du triangle. Par symétrie orthogonale d'axe $(d)$, la demi-droite $[AB)$ a pour image $[AC)$. La symétrie conservant la mesure des angles, elle partage l'angle $\widehat{BAC}$ en deux angles de même mesure: $\widehat{BAI} = \widehat{CAI}$. La droite $(d)$ est donc la bissectrice de $\widehat{BAC}$. [2 pts]

---
*End of Workbook 2 (Sixième / MYP 2).*
