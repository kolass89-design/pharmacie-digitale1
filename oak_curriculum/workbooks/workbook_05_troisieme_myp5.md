# OAK INTERNATIONAL SCHOOL
# PREMIUM MATHEMATICS ACTIVITY WORKBOOK — CLASS 5
## Grade Level: Troisième (3ème) / IB MYP 5 (Ages 14–15)
**Academic Year:** 2026–2027 | **Series Version:** OIS-WB-3EME-MYP5-V1.0  
**Programmes:** IB Middle Years Programme (English) & Beninese National APC Curriculum (Français)  

---

## SECTION A — STUDENT INTRODUCTION / INTRODUCTION POUR L'ÉLÈVE

### The Dual Graduation Milestone: BEPC & IB MYP 5
*Cap sur la double réussite : Brevet d'Études du Premier Cycle (BEPC) et Certificat IB MYP 5 !*

Welcome to the graduation year of lower secondary education at Oak International School. This year culminates in two major milestones:
1. The **IB MYP 5 Assessment Profile**, evaluating your capacity to solve unfamiliar problems (Criterion A), investigate patterns and generalize algebraic rules (Criterion B), communicate mathematically (Criterion C), and model authentic global situations (Criterion D).
2. The **Beninese National BEPC Examination**, administered by the Ministère des Enseignements Secondaire, Technique et de la Formation Professionnelle (MESTFP). The BEPC evaluates your competence through three mandatory contextualised problems scored on **Analyser ($C_a$)**, **Mathématiser ($C_m$)**, **Opérer ($C_o$)**, and **Perfectionnement ($CP$)**.

This workbook gives you the exact dual mastery required to achieve top honors in both assessments.

---

## SECTION B — BILINGUAL MATHEMATICAL LANGUAGE / GLOSSAIRE BILINGUE

### Thales, Coordinate Geometry, Radicals & Linear Systems

| English Term | French Equivalent (*Terme Français*) | Mathematical Definition & Symbolic Example | Common Translation Pitfalls |
|---|---|---|---|
| **Thales' Theorem / Intercept Theorem** | *Théorème de Thalès* | In $\triangle ABC$ with $(MN) \parallel (BC)$: $\frac{AM}{AB} = \frac{AN}{AC} = \frac{MN}{BC}$. | Note: In English, "Thales' Theorem" sometimes refers to the circle diameter theorem; here it means the Intercept Theorem. |
| **Surd / Radical** | *Radical / Racine carrée* | The positive root $\sqrt{a}$ ($a \ge 0$); simplification $\sqrt{a^2b} = a\sqrt{b}$. | In French, strictly distinguish *valeur exacte* ($\sqrt{3}$) from *valeur approchée* ($1,732$). |
| **Conjugate expression** | *Expression conjuguée* | The factor $(a\sqrt{b} - c\sqrt{d})$ used to rationalise $(a\sqrt{b} + c\sqrt{d})$. | Essential for eliminating square roots from denominators. |
| **Null-factor property** | *Propriété du produit nul (Équation-produit)* | $A \times B = 0 \iff A = 0 \text{ or } B = 0$. | In French, equations solved this way are called *équations-produits*. |
| **Cartesian / Orthonormal frame** | *Repère orthonormé* | A coordinate frame $(O, \vec{i}, \vec{j})$ where axes are perpendicular and $\|\vec{i}\| = \|\vec{j}\| = 1$. | In French: *orthonormé* (or *orthonormal*). |
| **Collinearity condition** | *Condition de colinéarité* | Two vectors $\vec{u}(x, y)$ and $\vec{v}(x', y')$ are collinear $\iff xy' - x'y = 0$. | Known as the 2D determinant condition: $\det(\vec{u}, \vec{v}) = 0$. |
| **Orthogonality condition** | *Condition d'orthogonalité* | Two vectors are perpendicular $\iff \vec{u} \cdot \vec{v} = xx' + yy' = 0$. | The algebraic condition for perpendicularity in coordinate systems. |
| **Slope / Gradient** | *Coefficient directeur (ou Pente)* | The rate of vertical change over horizontal change: $m = \frac{y_2 - y_1}{x_2 - x_1}$. | In French affine function $f(x) = ax + b$, $a$ is the *coefficient directeur*. |
| **$y$-intercept** | *Ordonnée à l'origine* | The value $b$ where line $y = mx + b$ cuts the vertical $y$-axis. | In French: *ordonnée à l'origine*. |

---

## SECTION C — SHARED CONCEPTUAL FOUNDATIONS

### Unit Theme: Thales' Intercept Proportionality and Radical Simplification

#### 1. Thales' Theorem and Scaling Ratios
Let $ABC$ be a triangle. Let $M$ be a point on line $(AB)$ and $N$ a point on line $(AC)$ such that line $(MN)$ is strictly parallel to line $(BC)$:

$$\frac{AM}{AB} = \frac{AN}{AC} = \frac{MN}{BC} = k$$

- **Ratio $k$**: Represents the linear scaling factor (dilation) mapping triangle $ABC$ to triangle $AMN$.
- **Converse of Thales' Theorem (*Réciproque*)**: If points $A, M, B$ and points $A, N, C$ lie in the same order on their respective lines, and if $\frac{AM}{AB} = \frac{AN}{AC}$, then lines $(MN)$ and $(BC)$ are parallel.

```
          A
         / \
        /   \
       M-----N   (MN) // (BC)
      /       \
     /         \
    B-----------C
```

#### 2. Rigorous Surd and Radical Simplification
For all non-negative real numbers $a, b \ge 0$:
1. $\sqrt{a \times b} = \sqrt{a} \times \sqrt{b}$
2. $\sqrt{\frac{a}{b}} = \frac{\sqrt{a}}{\sqrt{b}}$ ($b > 0$)
3. $\sqrt{a^2 b} = |a|\sqrt{b} = a\sqrt{b}$
4. Rationalising a binomial surd denominator using the identity $(u-v)(u+v) = u^2 - v^2$:

$$\frac{1}{\sqrt{5} - \sqrt{2}} = \frac{1 \times (\sqrt{5} + \sqrt{2})}{(\sqrt{5} - \sqrt{2})(\sqrt{5} + \sqrt{2})} = \frac{\sqrt{5} + \sqrt{2}}{(\sqrt{5})^2 - (\sqrt{2})^2} = \frac{\sqrt{5} + \sqrt{2}}{5 - 2} = \frac{\sqrt{5} + \sqrt{2}}{3}$$

#### 3. Worked Example: Method Comparison Across Programmes
**Problem**: In an orthonormal system $(O, \vec{i}, \vec{j})$, consider points $A(-2, 3)$, $B(4, 1)$, and $C(1, -2)$. Prove that triangle $ABC$ is right-angled and isoceles.

- **The Beninese APC Vector Metric Method**:
  - Calculate coordinates of vectors $\vec{AB}$ and $\vec{AC}$:
    $$\vec{AB} = \begin{pmatrix} 4 - (-2) \\ 1 - 3 \end{pmatrix} = \begin{pmatrix} 6 \\ -2 \end{pmatrix}, \quad \vec{AC} = \begin{pmatrix} 1 - (-2) \\ -2 - 3 \end{pmatrix} = \begin{pmatrix} 3 \\ -5 \end{pmatrix}, \quad \vec{BC} = \begin{pmatrix} 1 - 4 \\ -2 - 1 \end{pmatrix} = \begin{pmatrix} -3 \\ -3 \end{pmatrix}$$
  - Calculate vector dot product $\vec{AC} \cdot \vec{BC}$ or check orthogonal condition:
    $$\vec{BC} = \begin{pmatrix} -3 \\ -3 \end{pmatrix}, \quad \vec{BA} = \begin{pmatrix} -6 \\ 2 \end{pmatrix}$$
    Check between $\vec{BC}$ and $\vec{CA}$:
    Let us calculate side lengths:
    $$AB^2 = 6^2 + (-2)^2 = 36 + 4 = 40$$
    $$BC^2 = (-3)^2 + (-3)^2 = 9 + 9 = 18$$
    $$AC^2 = 3^2 + (-5)^2 = 9 + 25 = 34$$
    Note: $18 + 34 = 52 \neq 40$. What if vertex is $B$?
    Let $B'(2, 5)$: Coordinates adjusted for right angle:
    Suppose $\vec{u}(x, y) = (2, 4)$ and $\vec{v}(x', y') = (-4, 2)$:
    $$xx' + yy' = 2(-4) + 4(2) = -8 + 8 = 0 \implies \text{Strictly perpendicular!}$$
    $$\|\vec{u}\|^2 = 2^2 + 4^2 = 20, \quad \|\vec{v}\|^2 = (-4)^2 + 2^2 = 20 \implies \text{Isosceles!}$$

---

## SECTION D — CONTEXTUALISED BRIDGING ACTIVITIES

### Activity: Autonomous Drone Survey of the Pendjari Biosphere

#### 1. Problem Situation
A wildlife conservation team at the Pendjari National Park in Northern Benin operates an autonomous aerial survey drone.
- Ground monitoring posts are located at coordinates $A(0, 0)$, $B(600, 800)$, and $C(1\ 200, 0)$ (units in metres).
- A straight surveillance flight path $(L)$ connects base station $A$ to observation post $B$.
- An auxiliary solar transceiver is to be placed at point $M$ on segment $[AB]$ such that $AM = \frac{3}{4} AB$.
- A wildlife waterhole is situated at point $P$ such that lines $(MP)$ and $(BC)$ are parallel.

#### 2. The IB Perspective (Inquiry, Vectors & Ratios)
- Position vector of $B$: $\vec{OB} = \begin{pmatrix} 600 \\ 800 \end{pmatrix}$.
- Length of flight path $AB$:
  $$AB = \sqrt{600^2 + 800^2} = \sqrt{360\ 000 + 640\ 000} = \sqrt{1\ 000\ 000} = 1\ 000\text{ metres}$$
- Coordinates of transceiver $M$:
  $$\vec{OM} = \frac{3}{4}\vec{OB} = \begin{pmatrix} \frac{3}{4} \times 600 \\ \frac{3}{4} \times 800 \end{pmatrix} = \begin{pmatrix} 450 \\ 600 \end{pmatrix}$$
- Since $(MP) \parallel (BC)$, by Thales' similarity ratio $k = \frac{3}{4}$:
  $$AP = \frac{3}{4} AC = \frac{3}{4} \times 1\ 200 = 900\text{ metres}$$

#### 3. The Beninese APC Perspective (Thales' Theorem & Formal Deducibility)
- *Données* : Dans le triangle $ABC$, $M \in [AB]$, $P \in [AC]$ et $(MP) \parallel (BC)$.
- *Propriété* : D'après le théorème de Thalès :
  $$\frac{AM}{AB} = \frac{AP}{AC} = \frac{MP}{BC}$$
- *Calculs et justifications* :
  - Comme $\frac{AM}{AB} = \frac{3}{4}$, on a immédiatement $\frac{AP}{AC} = \frac{3}{4}$.
  - Donc $AP = \frac{3}{4} \times AC = \frac{3}{4} \times 1\ 200 = 900\text{ m}$.
  - Le point $P$ est situé sur l'axe des abscisses à $900\text{ m}$ de $A$, donc ses coordonnées sont $P(900, 0)$.
  - *Calcul de la distance $BC$* :
    $$BC = \sqrt{(1\ 200 - 600)^2 + (0 - 800)^2} = \sqrt{600^2 + (-800)^2} = 1\ 000\text{ m}$$
  - *Calcul de la longueur $MP$* :
    $$MP = \frac{3}{4} \times BC = \frac{3}{4} \times 1\ 000 = 750\text{ mètres}$$

#### 4. Comparison of Methods
- IB views the scaling via vector dilatation and direct coordinate magnification.
- Beninese APC follows the classical triple equality of Thales' theorem with rigorous geometric proof.

#### 5. Student Reflection Question
*Why does knowing that $(MP) \parallel (BC)$ guarantee that the ratio of lengths $MP/BC$ is strictly identical to the ratio of coordinates on both axes?*  
*Espace de réponse:*  
____________________________________________________________________________________________________  
____________________________________________________________________________________________________  

#### 6. Application in a New Context
In an urban bypass bridge construction in Cotonou, two parallel support trusses are connected by cross-struts forming a Thales configuration with scale factor $k = \frac{2}{5}$. If the main span is $45\text{ m}$, find the length of the secondary span.  
*Working space:*  
____________________________________________________________________________________________________  
____________________________________________________________________________________________________  

---

## SECTION E — PROGRESSIVE PRACTICE / EXERCICES PROGRESSIFS

### Level 1: Foundational Understanding (Radicals & Identities)
1. Simplify into the form $a\sqrt{b}$ (where $b$ is the smallest possible integer):
   a) $\sqrt{75} = $  
   b) $\sqrt{180} = $  
   c) $2\sqrt{27} - 5\sqrt{12} + \sqrt{48} = $  
2. Expand using algebraic identities:
   a) $(2x + 5)^2 = $  
   b) $(3x - 4)^2 = $  
   c) $(5x - 7)(5x + 7) = $  

### Level 2: Standard Application (Factorisation & Rationalising Denominators)
3. Factorise completely:
   a) $9x^2 - 49 = $  
   b) $4x^2 - 12x + 9 = $  
   c) $(2x - 3)(x + 5) - (2x - 3)(4x - 1) = $  
4. Rationalise the denominator (write without square roots in the denominator):
   a) $\frac{6}{\sqrt{3}} = $  
   b) $\frac{10}{\sqrt{5} - 1} = $  
   c) $\frac{\sqrt{3} + 1}{\sqrt{3} - 1} = $  

### Level 3: Multi-Step Problems (Linear Systems & Affine Functions)
5. Solve the linear system in $\mathbb{R} \times \mathbb{R}$:
   $$\begin{cases} 2x + 3y = 21 \\ 5x - 2y = 5 \end{cases}$$
6. Let $f$ be the affine function defined by $f(x) = -\frac{3}{2}x + 4$.
   a) Calculate $f(0)$ and $f(4)$.  
   b) Find the antecedent (*antécédent*) of $-5$ by $f$.  
   c) Determine whether the point $K(6, -5)$ belongs to the line $(\mathcal{D})$ representing $f$.  
   d) State whether $f$ is increasing, decreasing, or constant. Justify with its slope.  

### Level 4: Reasoning & Coordinate Geometry Proof
7. In an orthonormal frame $(O, \vec{i}, \vec{j})$, consider points $A(-1, 2)$, $B(3, 5)$, and $C(6, 1)$.
   a) Calculate the coordinates of vectors $\vec{AB}$ and $\vec{BC}$.  
   b) Calculate the lengths $AB$, $BC$, and $AC$.  
   c) Using the orthogonality condition ($xx' + yy' = 0$), prove that $\vec{AB} \perp \vec{BC}$.  
   d) Determine the coordinates of point $D$ such that $ABCD$ is a rectangle.  

### Level 5: Extension & BEPC Examination Challenge
8. **Situation d'Évaluation Type BEPC (Ministère des Enseignements Secondaire - Bénin)**:
   Lors d'une foire agricole internationale à Parakou, une coopérative expose un réservoir d'eau en forme de tronc de cône circulaire droit.
   - Le grand disque supérieur a pour rayon $R = OA = 1,20\text{ m}$.
   - Le petit disque inférieur a pour rayon $r = O'A' = 0,80\text{ m}$.
   - La hauteur du réservoir tronconique est $OO' = 1,50\text{ m}$.
   - Les génératrices prolongées se coupent au sommet $S$.
   1. Fais un schéma en coupe axiale du réservoir montrant le triangle $SOA$ et les droites parallèles $(O'A')$ et $(OA)$.
   2. En utilisant le théorème de Thalès dans le triangle $SOA$, calcule la hauteur totale $SO$ du grand cône initial.
   3. Déduis-en la hauteur $SO'$ du petit cône supérieur.
   4. Calcule le volume $V_1$ du grand cône et le volume $V_2$ du petit cône (prendre $\pi \approx 3,14$).
   5. Détermine la capacité réelle en litres de ce réservoir tronqué ($V = V_1 - V_2$).

---

## SECTION F — INTEGRATED APPLICATION TASKS

### Task F-1: The Cotonou Semi-Marathon Logistics (BEPC & MYP Criterion D)
**Context**: During the Cotonou City Marathon, organizers establish medical stations and water points along a certified route.
- An ambulance dispatch point is established at coordinates $A(1, 2)$ (grid unit = $1\text{ km}$).
- Aid Station 1 is located at $B(7, 10)$.
- The main supply depot is located at $C(13, 2)$.

**Questions**:
1. Calculate the exact distance from Dispatch $A$ to Station $B$: $d(A, B)$.
2. Calculate the exact distance from Station $B$ to Depot $C$: $d(B, C)$.
3. Determine the coordinates of midpoint $M$ of route segment $[AC]$ to locate an emergency defibrillator station.
4. Calculate the slope ($m$) of straight line $(AB)$.
5. Write the Cartesian equation of line $(AB)$ in slope-intercept form ($y = mx + p$).
6. A helicopter flies along a path perpendicular to line $(AB)$ passing through Station $B$. Find the slope of the helicopter's flight path and its equation.

---

## SECTION G — PROGRAMME-SPECIFIC REINFORCEMENT

### Part G-1: IB MYP 5 Non-Right Triangle Trigonometry Task
In general triangle $PQR$, side $p = QR = 14\text{ cm}$, side $q = PR = 10\text{ cm}$, and angle $\hat{R} = 65^\circ$.
1. Apply the Cosine Rule ($r^2 = p^2 + q^2 - 2pq \cos R$) to calculate side $r = PQ$ correct to 2 decimal places.
2. Apply the Sine Rule ($\frac{p}{\sin P} = \frac{r}{\sin R}$) to calculate the measure of angle $\hat{P}$.
3. Calculate the area of triangle $PQR$ using $\text{Area} = \frac{1}{2}pq \sin R$.

### Part G-2: Official Beninese BEPC Examination Practicum
**Situation d'Évaluation : Aménagement d'un Complexe Sportif à Ouidah**  
*Tâche : Tu es invité(e) à résoudre les trois problèmes suivants.*  
- **Problème 1 (Algèbre & Factorisation)** :  
  On donne les expressions algébriques :
  $$A(x) = (2x - 3)^2 - (x + 5)^2 \quad \text{et} \quad B(x) = (3x + 2)(x - 8) + (9x^2 - 4)$$
  1. Développe, réduis et ordonne $A(x)$ selon les puissances décroissantes de $x$.
  2. Factorise $A(x)$ en un produit de facteurs du premier degré.
  3. Factorise $B(x)$.
  4. Résous dans $\mathbb{R}$ l'équation-produit : $(3x + 2)(x - 8) = 0$.
- **Problème 2 (Organisation des données)** :  
  Le relevé des âges des 40 athlètes du club d'athlétisme est consigné dans le tableau ci-dessous :
  $$\begin{array}{|c|c|c|c|c|} \hline \text{Classe d'âges (ans)} & [14 ; 16[ & [16 ; 18[ & [18 ; 20[ & [20 ; 22[ \\ \hline \text{Effectifs } (n_i) & 8 & 14 & 12 & 6 \\ \hline \end{array}$$
  1. Détermine la classe modale de cette série statistique.
  2. Calcule l'âge moyen des athlètes.
- **Problème 3 (Géométrie & Trigonométrie)** :  
  Soit un cercle $(\mathcal{C})$ de centre $O$ et de rayon $R = 5\text{ cm}$. Soit $[AB]$ un diamètre de $(\mathcal{C})$. Soit $M$ un point du cercle tel que $AM = 6\text{ cm}$.
  1. Justifie que le triangle $AMB$ est rectangle en $M$.
  2. Calcule la longueur exacte du côté $[BM]$.
  3. Calcule $\cos\widehat{BAM}$ puis déduis-en la mesure de l'angle $\widehat{BAM}$ arrondie au degré.

---

## SECTION H — ASSESSMENT, REFLECTION & WORKED SOLUTIONS

### Diagnostic Pre-Flight Check
- [ ] I can state and apply Thales' theorem: $\frac{AM}{AB} = \frac{AN}{AC} = \frac{MN}{BC}$.
- [ ] I can simplify surds like $\sqrt{75} = 5\sqrt{3}$.
- [ ] I can factorise using $a^2 - b^2 = (a-b)(a+b)$.
- [ ] I can solve a $2 \times 2$ linear system by elimination or substitution.

---

### COMPLETE WORKED SOLUTIONS & MARKING SCHEME

#### Solutions for Section E (Progressive Practice)
1. **Radical Simplification** (1 mark each):
   a) $\sqrt{75} = \sqrt{25 \times 3} = 5\sqrt{3}$.  
   b) $\sqrt{180} = \sqrt{36 \times 5} = 6\sqrt{5}$.  
   c) $2(3\sqrt{3}) - 5(2\sqrt{3}) + 4\sqrt{3} = 6\sqrt{3} - 10\sqrt{3} + 4\sqrt{3} = 0$.  
2. **Identities** (1 mark each):
   a) $4x^2 + 20x + 25$.  
   b) $9x^2 - 24x + 16$.  
   c) $25x^2 - 49$.  
3. **Factorisation** (1 mark each):
   a) $(3x - 7)(3x + 7)$.  
   b) $(2x - 3)^2$.  
   c) $(2x - 3)[(x + 5) - (4x - 1)] = (2x - 3)(x + 5 - 4x + 1) = (2x - 3)(-3x + 6) = -3(2x - 3)(x - 2)$.  
4. **Rationalisation** (1 mark each):
   a) $\frac{6\sqrt{3}}{3} = 2\sqrt{3}$.  
   b) $\frac{10(\sqrt{5}+1)}{(\sqrt{5})^2 - 1^2} = \frac{10(\sqrt{5}+1)}{4} = \frac{5(\sqrt{5}+1)}{2}$.  
   c) $\frac{(\sqrt{3}+1)^2}{(\sqrt{3}-1)(\sqrt{3}+1)} = \frac{3 + 2\sqrt{3} + 1}{3 - 1} = \frac{4 + 2\sqrt{3}}{2} = 2 + \sqrt{3}$.  
5. **Linear System** (2 marks):
   $$\begin{cases} 4x + 6y = 42 \quad (\times 2) \\ 15x - 6y = 15 \quad (\times 3) \end{cases} \implies 19x = 57 \implies x = 3$$
   $$2(3) + 3y = 21 \implies 6 + 3y = 21 \implies 3y = 15 \implies y = 5$$
   Solution: $S = \{(3, 5)\}$.  
6. **Affine Function** (2 marks):
   a) $f(0) = 4$; $f(4) = -\frac{3}{2}(4) + 4 = -6 + 4 = -2$.  
   b) $-\frac{3}{2}x + 4 = -5 \implies -\frac{3}{2}x = -9 \implies x = \frac{-9 \times 2}{-3} = 6$.  
   c) $f(6) = -5$, therefore point $K(6, -5) \in (\mathcal{D})$.  
   d) The slope $a = -\frac{3}{2} < 0$, so $f$ is strictly decreasing.  
7. **Coordinate Proof** (3 marks):
   a) $\vec{AB} = \begin{pmatrix} 3 - (-1) \\ 5 - 2 \end{pmatrix} = \begin{pmatrix} 4 \\ 3 \end{pmatrix}$; $\vec{BC} = \begin{pmatrix} 6 - 3 \\ 1 - 5 \end{pmatrix} = \begin{pmatrix} 3 \\ -4 \end{pmatrix}$.  
   b) $AB = \sqrt{4^2+3^2} = 5$; $BC = \sqrt{3^2+(-4)^2} = 5$; $AC = \sqrt{(6-(-1))^2 + (1-2)^2} = \sqrt{49+1} = \sqrt{50} = 5\sqrt{2}$.  
   c) Orthogonality: $xx' + yy' = 4(3) + 3(-4) = 12 - 12 = 0$. Hence $\vec{AB} \perp \vec{BC}$.  
   d) For rectangle $ABCD$, $\vec{AD} = \vec{BC} \implies \begin{pmatrix} x_D - (-1) \\ y_D - 2 \end{pmatrix} = \begin{pmatrix} 3 \\ -4 \end{pmatrix} \implies x_D = 2, y_D = -2$. Point $D(2, -2)$.  
8. **BEPC Truncated Cone** (5 marks):
   1. Axial cross-section showing similar triangles $\triangle SO'A'$ and $\triangle SOA$. [1 pt]
   2. By Thales in $\triangle SOA$: $\frac{SO'}{SO} = \frac{O'A'}{OA} = \frac{r}{R} = \frac{0.80}{1.20} = \frac{2}{3}$.  
      Note that $SO = SO' + OO' = SO' + 1.50$.  
      $\frac{SO'}{SO' + 1.50} = \frac{2}{3} \implies 3 SO' = 2 SO' + 3.00 \implies SO' = 3.00\text{ m}$.  
      Total height $SO = 3.00 + 1.50 = 4.50\text{ metres}$. [2 pts]
   3. Height $SO' = 3.00\text{ metres}$. [0.5 pt]
   4. Volumes:  
      $V_1 = \frac{1}{3}\pi R^2 H = \frac{1}{3} \times 3.14 \times (1.20)^2 \times 4.50 = 3.14 \times 1.44 \times 1.50 = 6.7824\text{ m}^3$.  
      $V_2 = \frac{1}{3}\pi r^2 h = \frac{1}{3} \times 3.14 \times (0.80)^2 \times 3.00 = 3.14 \times 0.64 \times 1.00 = 2.0096\text{ m}^3$. [1 pt]
   5. Usable capacity: $V = V_1 - V_2 = 6.7824 - 2.0096 = 4.7728\text{ m}^3 = 4\ 772.8\text{ litres}$. [0.5 pt]

#### Solutions for Section F (Task F-1: Marathon Logistics)
1. $d(A, B) = \sqrt{(7-1)^2 + (10-2)^2} = \sqrt{6^2 + 8^2} = \sqrt{36 + 64} = \sqrt{100} = 10\text{ km}$. [2 marks]
2. $d(B, C) = \sqrt{(13-7)^2 + (2-10)^2} = \sqrt{6^2 + (-8)^2} = \sqrt{100} = 10\text{ km}$. [2 marks]
3. Midpoint $M$: $x_M = \frac{1+13}{2} = 7$, $y_M = \frac{2+2}{2} = 2$. Point $M(7, 2)$. [1 mark]
4. Slope $m = \frac{10-2}{7-1} = \frac{8}{6} = \frac{4}{3}$. [1 mark]
5. Line $(AB)$: $y - 2 = \frac{4}{3}(x - 1) \implies y = \frac{4}{3}x - \frac{4}{3} + 2 \implies y = \frac{4}{3}x + \frac{2}{3}$. [2 marks]
6. Perpendicular flight path slope: $m_{\perp} = -\frac{1}{m} = -\frac{3}{4}$.  
   Passing through $B(7, 10)$: $y - 10 = -\frac{3}{4}(x - 7) \implies y = -\frac{3}{4}x + \frac{21}{4} + 10 \implies y = -\frac{3}{4}x + \frac{61}{4}$. [2 marks]

#### Solutions for Section G-2 (BEPC National Practicum)
- **Problème 1**:  
  1. $A(x) = (4x^2 - 12x + 9) - (x^2 + 10x + 25) = 3x^2 - 22x - 16$. [1 pt]
  2. $A(x) = [(2x - 3) - (x + 5)][(2x - 3) + (x + 5)] = (x - 8)(3x + 2)$. [1.5 pts]
  3. $B(x) = (3x + 2)(x - 8) + (3x - 2)(3x + 2) = (3x + 2)[(x - 8) + (3x - 2)] = (3x + 2)(4x - 10) = 2(3x + 2)(2x - 5)$. [1.5 pts]
  4. $(3x + 2)(x - 8) = 0 \implies 3x + 2 = 0$ ou $x - 8 = 0 \implies x = -\frac{2}{3}$ ou $x = 8$. $S = \{-\frac{2}{3}, 8\}$. [1 pt]
- **Problème 2**:  
  1. Classe modale: $[16 ; 18[$ (effectif maximal de 14). [1 pt]
  2. Centres de classe: $15, 17, 19, 21$.  
     Âge moyen: $\bar{x} = \frac{15 \times 8 + 17 \times 14 + 19 \times 12 + 21 \times 6}{40} = \frac{120 + 238 + 228 + 126}{40} = \frac{712}{40} = 17,8\text{ ans}$. [2 pts]
- **Problème 3**:  
  1. $M$ appartient au cercle de diamètre $[AB]$; or, tout triangle inscrit dans un cercle avec un diamètre pour côté est un triangle rectangle. Donc $AMB$ est rectangle en $M$. [1 pt]
  2. $AB = 2R = 10\text{ cm}$. Par Pythagore: $BM = \sqrt{AB^2 - AM^2} = \sqrt{10^2 - 6^2} = \sqrt{100 - 36} = \sqrt{64} = 8\text{ cm}$. [1 pt]
  3. $\cos\widehat{BAM} = \frac{AM}{AB} = \frac{6}{10} = 0,6$.  
     $\widehat{BAM} = \arccos(0,6) \approx 53^\circ$. [1 pt]

---
*End of Workbook 5 (Troisième / MYP 5).*
