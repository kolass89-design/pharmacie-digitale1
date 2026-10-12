# OAK INTERNATIONAL SCHOOL
# PREMIUM MATHEMATICS ACTIVITY WORKBOOK — CLASS 4
## Grade Level: Quatrième (4ème) / IB MYP 4 (Ages 13–14)
**Academic Year:** 2026–2027 | **Series Version:** OIS-WB-4EME-MYP4-V1.0  
**Programmes:** IB Middle Years Programme (English) & Beninese National APC Curriculum (Français)  

---

## SECTION A — STUDENT INTRODUCTION / INTRODUCTION POUR L'ÉLÈVE

### Entering the Golden Age of Geometry and Algebraic Proof
*Bienvenue en classe de Quatrième / IB MYP 4 à Oak International School !*

In Quatrième / MYP 4, your mathematical power reaches an extraordinary turning point:
- In **IB MYP 4**, you harness the universal power of **Pythagoras' Theorem** in 2D and 3D, expand your algebraic toolset with binomial expansions and linear equations, and connect right-triangle trigonometry ($\sin, \cos, \tan$) to navigation and engineering.
- In **Beninese 4ème (APC)**, you explore **Situation d'Apprentissage N°1 (Configurations du plan)** and **N°4 (Applications du plan)**. You master the converse of Pythagoras to prove right angles with flawless deductive rigor, unlock the geometric beauty of vectors ($\vec{u}$) and Chasles' relation, and uncover the centroid ($G$) and orthocentre ($H$) of triangles.

This workbook harmonises both traditions into a single, high-performance learning companion.

---

## SECTION B — BILINGUAL MATHEMATICAL LANGUAGE / GLOSSAIRE BILINGUE

### Pythagoras, Vectors & Literal Algebra

| English Term | French Equivalent (*Terme Français*) | Mathematical Definition & Symbolic Example | Common Translation Pitfalls |
|---|---|---|---|
| **Hypotenuse** | *Hypoténuse* | The longest side of a right-angled triangle, opposite the $90^\circ$ angle. | Spelling check: *hypoténuse* in French with one 'h'; English has 'h' at start only. |
| **Pythagoras' Theorem** | *Théorème de Pythagore* | In a right triangle with hypotenuse $c$: $a^2 + b^2 = c^2$. | In French, strictly distinguish the direct theorem from its converse (*réciproque*). |
| **Converse theorem** | *Réciproque d'un théorème* | The reverse logical implication: If $BC^2 = AB^2 + AC^2$, then triangle $ABC$ is right-angled at $A$. | Do not confuse *réciproque* (converse) with *contraposée* (contrapositive). |
| **Cosine ratio** | *Cosinus d'un angle aigu* | In a right-angled triangle: $\cos\theta = \frac{\text{adjacent side}}{\text{hypotenuse}}$. | Beninese 4ème focuses on cosine; IB MYP 4 teaches $\sin$, $\cos$, and $\tan$ together. |
| **Vector** | *Vecteur* | A mathematical object defined by a direction, a sense (orientation), and a magnitude (norm): $\vec{u}$ or $\vec{AB}$. | Do not confuse *direction* (the line's orientation) with *sens* (arrowhead pointing left/right). |
| **Chasles' relation** | *Relation de Chasles* | Fundamental vector addition identity: $\vec{AB} + \vec{BC} = \vec{AC}$. | Universal in French mathematics; used in IB vector algebra. |
| **Centroid / Centre of gravity** | *Centre de gravité ($G$)* | The concurrency point of the three medians of a triangle, located at $2/3$ from each vertex. | In English: centroid. In French: *centre de gravité d'un triangle*. |
| **Expanding brackets** | *Développement d'une expression* | Transforming a product into a sum: $a(b+c) = ab + ac$; $(a+b)(c+d) = ac + ad + bc + bd$. | In French: *développer et réduire*. |
| **Factoring / Factorisation** | *Factorisation* | Transforming a sum into a product of factors: $ka + kb = k(a+b)$. | In French: *factoriser par mise en facteur commun*. |

---

## SECTION C — SHARED CONCEPTUAL FOUNDATIONS

### Unit Theme: The Pythagorean Metric and Vector Translations

#### 1. Pythagoras' Theorem and its Converse
In any triangle $ABC$:
- **Direct Theorem**: If triangle $ABC$ is right-angled at $A$, then:
  $$BC^2 = AB^2 + AC^2$$
- **Converse Theorem (Réciproque)**: If the lengths of the sides satisfy $BC^2 = AB^2 + AC^2$, then triangle $ABC$ is right-angled at vertex $A$.
- **Contrapositive (Conséquence)**: If $BC^2 \neq AB^2 + AC^2$ where $[BC]$ is the longest side, then triangle $ABC$ is definitely not right-angled.

```
       A
       |\
       | \
     b |  \ c (Hypotenuse)
       |   \
       +----\
       C  a  B
   b^2 + a^2 = c^2
```

#### 2. Vector Foundations: The Three Defining Attributes
A vector $\vec{u} = \vec{AB}$ is characterised by:
1. **Direction**: The line $(AB)$ or any line parallel to it.
2. **Sense (*Sens*)**: The orientation along the line (from origin $A$ toward terminus $B$).
3. **Magnitude (*Norme*)**: The geometric length of segment $[AB]$, denoted $\|\vec{AB}\| = AB$.

Two vectors are equal ($\vec{AB} = \vec{CD}$) if and only if:
- They share the same direction: $(AB) \parallel (CD)$;
- They share the same sense;
- They have equal lengths: $AB = CD$.
Geometrically, $\vec{AB} = \vec{CD} \iff ABDC$ is a parallelogram (possibly flattened).

#### 3. Worked Example: Method Comparison Across Programmes
**Problem**: A survey team in Dassa measures a triangle with side lengths $EF = 65\text{ m}$, $EG = 52\text{ m}$, and $FG = 39\text{ m}$. Is the survey boundary perpendicular at $G$?

- **The Beninese APC Deductive Model**:
  - *Identifier le plus grand côté* : Le plus grand côté est $[EF]$ avec $EF = 65\text{ m}$.
  - *Calculer séparément* :
    $$EF^2 = 65^2 = 4\ 225$$
    $$EG^2 + FG^2 = 52^2 + 39^2 = 2\ 704 + 1\ 521 = 4\ 225$$
  - *Constater l'égalité* : On constate que $EF^2 = EG^2 + FG^2$.
  - *Conclusion légale* : D'après la réciproque du théorème de Pythagore, le triangle $EFG$ est rectangle en $G$. Les limites de parcelles sont donc strictement perpendiculaires en $G$.
- **The IB MYP Inquiry Model (Criterion A & C)**:
  - Test Pythagoras' relation for right triangles: $a^2 + b^2 \stackrel{?}{=} c^2$.
  - Let $c = 65$, $a = 52$, $b = 39$.
  - $52^2 + 39^2 = 2\ 704 + 1\ 521 = 4\ 225 = 65^2$.
  - Since the Pythagorean identity holds, the triangle contains a $90^\circ$ angle opposite side $c$. The boundary lines meet at a right angle ($90^\circ$) at vertex $G$.

---

## SECTION D — CONTEXTUALISED BRIDGING ACTIVITIES

### Activity: Timber Truss Construction in Porto-Novo

#### 1. Problem Situation
A master carpenter in Porto-Novo is fabricating a traditional timber roof truss for a community meeting hall.
- The symmetrical king-post truss forms an isosceles triangle $ABC$ with base span $BC = 16\text{ metres}$ and equal rafters $AB = AC = 10\text{ metres}$.
- The vertical central king-post $[AH]$ joins apex $A$ to the midpoint $H$ of base $[BC]$.
- Two diagonal strut braces $[HD]$ and $[HE]$ are installed, connecting midpoint $H$ to the midpoints $D$ of rafter $[AB]$ and $E$ of rafter $[AC]$.

#### 2. The IB Perspective (Inquiry & Trigonometric Modelling)
- In right-angled triangle $ABH$, midpoint $H$ gives $BH = 16 \div 2 = 8\text{ metres}$.
- Calculate height $AH$ using Pythagoras:
  $$AH = \sqrt{AB^2 - BH^2} = \sqrt{10^2 - 8^2} = \sqrt{100 - 64} = \sqrt{36} = 6\text{ metres}$$
- Calculate pitch angle $\theta = \widehat{ABH}$:
  $$\cos\theta = \frac{BH}{AB} = \frac{8}{10} = 0.8 \implies \theta = \arccos(0.8) \approx 36.87^\circ$$
- Calculate rafter length using trigonometry to cross-check:
  $$AB = \frac{BH}{\cos 36.87^\circ} = \frac{8}{0.8} = 10\text{ metres}$$

#### 3. The Beninese APC Perspective (Concurrence & Midpoint Theorem)
- *Calcul de la hauteur $AH$* :
  Dans le triangle $ABH$ rectangle en $H$ d'après la propriété de la médiatrice :
  $$AB^2 = AH^2 + BH^2 \implies AH^2 = 10^2 - 8^2 = 36 \implies AH = 6\text{ m}$$
- *Calcul de la longueur du renfort $[HD]$* :
  Dans le triangle $ABH$ rectangle en $H$, $D$ est le milieu de l'hypoténuse $[AB]$.
  *Propriété* : Dans un triangle rectangle, la longueur de la médiane issue du sommet de l'angle droit est égale à la moitié de la longueur de l'hypoténuse.
  $$HD = \frac{AB}{2} = \frac{10}{2} = 5\text{ mètres}$$
- *Vérification par le Théorème des milieux* :
  Dans le triangle $ABC$, $D$ est le milieu de $[AB]$ et $H$ est le milieu de $[BC]$. La droite $(DH)$ est parallèle à $(AC)$ et $DH = \frac{AC}{2} = \frac{10}{2} = 5\text{ m}$.

#### 4. Comparison of Methods
- IB uses trigonometric cosine ratios to find structural angles.
- Beninese APC leverages the midpoint theorem (*théorème des milieux*) and median property of right triangles, providing an exact geometric proof without decimal rounding.

#### 5. Student Reflection Question
*Why does the median of a right-angled triangle equal exactly half of the hypotenuse? How does drawing the circumscribed circle make this obvious?*  
*Espace de réponse:*  
____________________________________________________________________________________________________  
____________________________________________________________________________________________________  

#### 6. Application in a New Context
A crane boom at the Port of Cotonou has an arm of length $25\text{ m}$ extending horizontally by $24\text{ m}$. Calculate its vertical height above the base pivot and the cosine of the inclination angle.  
*Working space:*  
____________________________________________________________________________________________________  
____________________________________________________________________________________________________  

---

## SECTION E — PROGRESSIVE PRACTICE / EXERCICES PROGRESSIFS

### Level 1: Foundational Understanding (Pythagoras & Rational Numbers)
1. In right-angled triangle $ABC$ with hypotenuse $[BC]$, calculate the unknown side:
   a) $AB = 9\text{ cm}, AC = 12\text{ cm} \implies BC = $  
   b) $BC = 25\text{ cm}, AB = 15\text{ cm} \implies AC = $  
   c) $AB = 5\text{ cm}, AC = 7\text{ cm} \implies BC = $ (exact form and 2 decimal places).  
2. Calculate and write as an irreducible fraction:
   a) $A = \frac{2}{3} - \frac{5}{6} \times \frac{4}{7} = $  
   b) $B = \left(\frac{1}{2} + \frac{3}{4}\right) \div \left(\frac{5}{8} - \frac{1}{4}\right) = $  

### Level 2: Standard Application (Algebraic Expansion & Exponents)
3. Expand and collect like terms:
   a) $3(2x - 5) - 4(x + 2) = $  
   b) $(2x + 3)(x - 4) = $  
   c) $(3x - 2)(3x + 2) = $  
4. Simplify using exponent laws:
   a) $\frac{a^5 \times a^3}{a^2} = $  
   b) $(2x^3)^4 = $  
   c) $\frac{10^4 \times 10^{-7}}{10^{-2}} = $  

### Level 3: Multi-Step Problems (Equations & Triangle Centres)
5. Solve in $\mathbb{Q}$ (set of rational numbers):
   a) $4x - 7 = 2x + 9$  
   b) $\frac{2x - 1}{3} = \frac{x + 4}{2}$  
   c) $5(x - 2) - 3(2x + 1) = 0$  
6. Let $ABC$ be a triangle with medians $[AA']$, $[BB']$, and $[CC']$ intersecting at centroid $G$.
   a) If the total median length $AA' = 12\text{ cm}$, calculate lengths $AG$ and $GA'$.  
   b) State the vector relationship between $\vec{GA}$ and $\vec{GA'}$.  

### Level 4: Reasoning & Geometric Proof (Converse Pythagoras & Vectors)
7. Points $P, Q, R$ have coordinates in a plane: $PQ = 20\text{ m}, QR = 21\text{ m}, PR = 29\text{ m}$.
   a) Prove that triangle $PQR$ is right-angled. Name the vertex of the right angle.  
   b) Calculate $\cos\widehat{QPR}$ and $\cos\widehat{PRQ}$.  
   c) Simplify the vector sum: $\vec{S} = \vec{PQ} + \vec{QR} + \vec{RP}$.  
   d) Express $\vec{QP} + \vec{QR}$ using a single vector if $PQSR$ is a rectangle.  

### Level 5: Extension & 4ème National Examination Challenge
8. **Situation d'Évaluation Type 4ème (SA N°1 & N°3)**:
   Pour stocker les récoltes de sorgho dans l'Atacora, une coopérative construit un grenier traditionnel modélisé par une pyramide régulière à base carrée $SABCD$.
   - La base carrée $ABCD$ a pour côté $AB = 6\text{ mètres}$.
   - Le sommet $S$ est situé verticalement au-dessus du centre $O$ de la base carrée.
   - La hauteur de la pyramide est $SO = 4\text{ mètres}$.
   1. Calcule la longueur de la diagonale $[AC]$ de la base carrée (donne la valeur exacte puis arrondie au centimètre).
   2. Calcule la longueur $AO$.
   3. Démontre que le triangle $SOA$ est rectangle en $O$, et calcule la longueur exacte de l'arête latérale $[SA]$.
   4. Soit $M$ le milieu du côté $[BC]$. Calcule l'apothème $SM$ de la pyramide.
   5. Calcule l'aire latérale totale du grenier ainsi que son volume de stockage en $\text{m}^3$.

---

## SECTION F — INTEGRATED APPLICATION TASKS

### Task F-1: Container Transhipment at Cotonou Port (MYP Criterion D & Benin SA 4)
**Context**: A gantry crane at the Autonomous Port of Cotonou relocates shipping containers from cargo vessels to transport trucks.
- The crane spreader moves a container from point $A$ to point $B$ by translation vector $\vec{u}_1$.
- A second automated transfer moves the container from $B$ to final storage bay $C$ by vector $\vec{u}_2$.
- In the port grid coordinate system (units in metres):
  - $\vec{u}_1$ represents a displacement of $30\text{ m}$ East and $40\text{ m}$ North.
  - $\vec{u}_2$ represents a displacement of $50\text{ m}$ East and $20\text{ m}$ South.

**Questions**:
1. Calculate the direct distance of displacement from $A$ to $B$ (magnitude $\|\vec{u}_1\|$) using Pythagoras' Theorem.
2. Express the net resultant displacement vector $\vec{AC}$ using Chasles' relation.
3. Calculate the total horizontal (East) and vertical (North/South) components of vector $\vec{AC}$.
4. Calculate the straight-line distance between initial position $A$ and final position $C$.
5. If the container travels directly from $A$ to $C$ at a speed of $1.5\text{ m/s}$, calculate the transit time in seconds.

---

## SECTION G — PROGRAMME-SPECIFIC REINFORCEMENT

### Part G-1: IB MYP 4 Trigonometry Exploration
In right-angled triangle $XYZ$ right-angled at $Y$, side $XY = 12\text{ cm}$ and side $YZ = 5\text{ cm}$.
1. Calculate hypotenuse $XZ$.
2. State the exact fractional values of:
   $$\sin\hat{X}, \quad \cos\hat{X}, \quad \tan\hat{X}$$
3. Verify that $\tan\hat{X} = \frac{\sin\hat{X}}{\cos\hat{X}}$.
4. Verify the Pythagorean identity: $\sin^2\hat{X} + \cos^2\hat{X} = 1$.

### Part G-2: Beninese NPE Vector and Geometry Proof
**Exercice de Démonstration Vectorielle (Classe de 4ème)**  
Soit un parallélogramme $ABCD$. Soit $E$ le point tel que $\vec{CE} = \vec{AB}$.
1. Démontre que $\vec{AB} = \vec{DC}$.
2. Déduis-en que $\vec{DC} = \vec{CE}$.
3. Que peux-tu en déduire pour le point $C$ par rapport au segment $[DE]$ ? Justifie rigoureusement.

---

## SECTION H — ASSESSMENT, REFLECTION & WORKED SOLUTIONS

### Diagnostic Pre-Flight Check
- [ ] I can apply Pythagoras' theorem: $c = \sqrt{a^2 + b^2}$.
- [ ] I can verify if a triangle is right-angled using the converse theorem.
- [ ] I know how to add vectors using Chasles' relation: $\vec{AB} + \vec{BC} = \vec{AC}$.
- [ ] I can expand double brackets: $(a+b)(c+d)$.

---

### COMPLETE WORKED SOLUTIONS & MARKING SCHEME

#### Solutions for Section E (Progressive Practice)
1. **Pythagoras Calculations** (1 mark each):
   a) $BC = \sqrt{9^2 + 12^2} = \sqrt{81 + 144} = \sqrt{225} = 15\text{ cm}$.  
   b) $AC = \sqrt{25^2 - 15^2} = \sqrt{625 - 225} = \sqrt{400} = 20\text{ cm}$.  
   c) $BC = \sqrt{5^2 + 7^2} = \sqrt{25 + 49} = \sqrt{74} \approx 8.60\text{ cm}$.  
2. **Rational Arithmetic** (1 mark each):
   a) $A = \frac{2}{3} - \frac{20}{42} = \frac{2}{3} - \frac{10}{21} = \frac{14 - 10}{21} = \frac{4}{21}$.  
   b) $B = \left(\frac{2+3}{4}\right) \div \left(\frac{5-2}{8}\right) = \frac{5}{4} \div \frac{3}{8} = \frac{5}{4} \times \frac{8}{3} = \frac{10}{3}$.  
3. **Algebraic Expansions** (1 mark each):
   a) $6x - 15 - 4x - 8 = 2x - 23$.  
   b) $2x^2 - 8x + 3x - 12 = 2x^2 - 5x - 12$.  
   c) Difference of squares: $9x^2 - 4$.  
4. **Exponent Laws** (1 mark each):
   a) $a^{5+3-2} = a^6$.  
   b) $2^4 x^{3 \times 4} = 16x^{12}$.  
   c) $10^{4 - 7 - (-2)} = 10^{-1} = 0.1$.  
5. **Equations** (1 mark each):
   a) $4x - 2x = 9 + 7 \implies 2x = 16 \implies x = 8$.  
   b) $2(2x - 1) = 3(x + 4) \implies 4x - 2 = 3x + 12 \implies x = 14$.  
   c) $5x - 10 - 6x - 3 = 0 \implies -x - 13 = 0 \implies x = -13$.  
6. **Centroid $G$** (2 marks):
   a) In a triangle, the centroid is located at $2/3$ of the median from the vertex:  
      $AG = \frac{2}{3} \times 12 = 8\text{ cm}$, and $GA' = 12 - 8 = 4\text{ cm}$.  
   b) Opposite senses along the same line: $\vec{GA} = -2\vec{GA'}$.  
7. **Converse Pythagoras & Vectors** (4 marks):
   a) Check longest side $PR = 29$:  
      $PR^2 = 29^2 = 841$.  
      $PQ^2 + QR^2 = 20^2 + 21^2 = 400 + 441 = 841$.  
      Since $PR^2 = PQ^2 + QR^2$, by the converse of Pythagoras' theorem, $\triangle PQR$ is right-angled at $Q$.  
   b) $\cos\widehat{QPR} = \frac{PQ}{PR} = \frac{20}{29} \approx 0.690$; $\cos\widehat{PRQ} = \frac{QR}{PR} = \frac{21}{29} \approx 0.724$.  
   c) By Chasles' relation: $\vec{PQ} + \vec{QR} + \vec{RP} = \vec{PR} + \vec{RP} = \vec{PP} = \vec{0}$ (null vector).  
   d) In rectangle $PQSR$, $\vec{QP} + \vec{QR} = \vec{QS}$.  
8. **Atacora Pyramid Granary** (5 marks):
   1. In right-angled $\triangle ABC$: $AC^2 = 6^2 + 6^2 = 72 \implies AC = \sqrt{72} = 6\sqrt{2} \approx 8.49\text{ m}$. [1 mark]
   2. $O$ is the centre (midpoint of $[AC]$), so $AO = \frac{AC}{2} = 3\sqrt{2} \approx 4.24\text{ m}$. [1 mark]
   3. Height $[SO]$ is perpendicular to base plane: $\triangle SOA$ is right-angled at $O$.  
      $SA = \sqrt{SO^2 + AO^2} = \sqrt{4^2 + (3\sqrt{2})^2} = \sqrt{16 + 18} = \sqrt{34} \approx 5.83\text{ m}$. [1 mark]
   4. In right-angled $\triangle SOM$ with $OM = \frac{AB}{2} = 3\text{ m}$:  
      $SM = \sqrt{SO^2 + OM^2} = \sqrt{4^2 + 3^2} = \sqrt{16 + 9} = \sqrt{25} = 5\text{ metres}$. [1 mark]
   5. Lateral area: 4 triangles of base 6 and height 5: $\text{Area} = 4 \times \left(\frac{6 \times 5}{2}\right) = 60\text{ m}^2$.  
      Volume: $V = \frac{1}{3} \times \text{Base Area} \times h = \frac{1}{3} \times (6^2) \times 4 = \frac{1}{3} \times 36 \times 4 = 48\text{ m}^3$. [1 mark]

#### Solutions for Section F (Task F-1: Cotonou Port Spreader)
1. Magnitude $\|\vec{u}_1\| = \sqrt{30^2 + 40^2} = \sqrt{900 + 1\ 600} = \sqrt{2\ 500} = 50\text{ metres}$. [2 marks]
2. Chasles' relation: $\vec{AC} = \vec{AB} + \vec{BC} = \vec{u}_1 + \vec{u}_2$. [1 mark]
3. Total horizontal: $30 + 50 = 80\text{ m}$ East. Total vertical: $40 - 20 = 20\text{ m}$ North. [2 marks]
4. Straight-line distance: $AC = \sqrt{80^2 + 20^2} = \sqrt{6\ 400 + 400} = \sqrt{6\ 800} \approx 82.46\text{ metres}$. [2 marks]
5. Transit time: $t = \frac{82.46}{1.5} \approx 54.97\text{ seconds}$ ($\approx 55\text{ s}$). [1 mark]

#### Solutions for Section G-2 (Benin Vector Proof 4ème)
1. $ABCD$ est un parallélogramme, donc par définition de l'égalité vectorielle, les côtés opposés orientés sont égaux : $\vec{AB} = \vec{DC}$. [1 pt]
2. Par hypothèse, $\vec{CE} = \vec{AB}$. Comme $\vec{AB} = \vec{DC}$, on en déduit par transitivité que $\vec{DC} = \vec{CE}$. [2 pts]
3. L'égalité vectorielle $\vec{DC} = \vec{CE}$ signifie que les vecteurs ont la même direction (les droites $(DC)$ et $(CE)$ sont confondues, donc les points $D, C, E$ sont alignés), le même sens, et la même longueur ($DC = CE$). Par conséquent, le point $C$ est le milieu du segment $[DE]$. [2 pts]

---
*End of Workbook 4 (Quatrième / MYP 4).*
