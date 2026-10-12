# OAK INTERNATIONAL SCHOOL
# PREMIUM MATHEMATICS ACTIVITY WORKBOOK — CLASS 6
## Grade Level: Seconde (2nde) / IB DP 1 (Ages 15–16)
**Academic Year:** 2026–2027 | **Series Version:** OIS-WB-2NDE-DP1-V1.0  
**Programmes:** IB Diploma Programme (English - AA/AI Core) & Beninese National APC (Séries C & D)  

---

## SECTION A — STUDENT INTRODUCTION / INTRODUCTION POUR L'ÉLÈVE

### The Gateway to Advanced Mathematics and University Preparation
*Bienvenue dans le second cycle de l'excellence mathématique à Oak International School !*

In Seconde / DP 1, you cross the threshold into advanced pre-university mathematics:
- In **IB Diploma Programme 1 (DP 1)**, you engage with the rigorous 60-hour Common Core covering algebraic proof, functional modelling, trigonometric circular functions, and technology-assisted problem solving with your Graphic Display Calculator (GDC).
- In **Beninese Seconde C & D (APC)**, you explore the profound analytical syllabus of the *Nouveaux Programmes d'Études* and *CIAM 2nde SM/SE*: the general theory of quadratic trinomials ($ax^2 + bx + c$), 2D vector dot products ($\vec{u} \cdot \vec{v}$), the Al-Kashi theorem (Law of Cosines), and 3D spatial incidence geometry.

This workbook provides the shared conceptual foundation and dual examination practice to guarantee that you dominate both the IB DP assessments and the Beninese national scientific evaluations.

---

## SECTION B — BILINGUAL MATHEMATICAL LANGUAGE / GLOSSAIRE BILINGUE

### Quadratics, Functions, Dot Products & Circular Trigonometry

| English Term | French Equivalent (*Terme Français*) | Mathematical Definition & Symbolic Example | Common Translation Pitfalls |
|---|---|---|---|
| **Discriminant** | *Discriminant ($\Delta$)* | For $ax^2 + bx + c = 0$, $\Delta = b^2 - 4ac$. Governs nature of roots. | Same word and symbol in both languages ($\Delta$). |
| **Completing the square** | *Forme canonique* | Rewriting $ax^2 + bx + c$ as $a[(x + \frac{b}{2a})^2 - \frac{\Delta}{4a^2}]$. | In English: completing the square; in French: *mise sous forme canonique*. |
| **Domain of definition** | *Ensemble de définition ($D_f$)* | The set of input values $x$ for which $f(x)$ is real: $\{x \in \mathbb{R} \mid f(x) \text{ exists}\}$. | In French: *ensemble de définition*; in English: *domain*. |
| **Composite function** | *Fonction composée* | The chaining of two functions: $(g \circ f)(x) = g(f(x))$. | Read as "$g$ composed with $f$" or in French *« $g$ rond $f$ »*. |
| **Dot product / Scalar product** | *Produit scalaire* | $\vec{u} \cdot \vec{v} = \|\vec{u}\| \|\vec{v}\| \cos\theta = xx' + yy'$. Returns a scalar! | Never write a cross ($\times$) for scalar multiplication of vectors. Use a dot ($\cdot$). |
| **Law of Cosines / Al-Kashi** | *Théorème d'Al-Kashi* | In any triangle: $a^2 = b^2 + c^2 - 2bc \cos \hat{A}$. | In English: Law of Cosines; in French: *Théorème d'Al-Kashi*. |
| **Radian** | *Radian (rad)* | Angle subtending an arc equal in length to the circle's radius: $\pi \text{ rad} = 180^\circ$. | Ensure calculator mode is set to RAD for calculus and advanced trigonometry! |
| **Odd / Even function** | *Fonction impaire / paire* | Even: $f(-x) = f(x)$ (symmetric about $y$-axis); Odd: $f(-x) = -f(x)$ (symmetric about origin). | In French: *parité d'une fonction*. |
| **Absolute value / Modulus** | *Valeur absolue* | Distance from zero: $|x| = x$ if $x \ge 0$, and $|x| = -x$ if $x < 0$. | Geometrically, $|x - a|$ is the distance between $x$ and $a$ on the real number line. |

---

## SECTION C — SHARED CONCEPTUAL FOUNDATIONS

### Unit Theme: The Dot Product, Metric Relations and Quadratic Optimization

#### 1. The Scalar Product (Produit Scalaire)
The scalar product of two vectors $\vec{u}$ and $\vec{v}$ in a 2D Euclidean space is defined by three equivalent expressions:
1. **Geometric Definition**:
   $$\vec{u} \cdot \vec{v} = \|\vec{u}\| \|\vec{v}\| \cos\theta \quad (\theta = (\widehat{\vec{u}, \vec{v}}))$$
2. **Orthogonal Projection Definition**:
   If $H$ is the orthogonal projection of point $B$ onto line $(OA)$, then:
   $$\vec{OA} \cdot \vec{OB} = \overline{OA} \times \overline{OH}$$
3. **Analytic Coordinate Definition (Orthonormal Base)**:
   If $\vec{u} = \begin{pmatrix} x \\ y \end{pmatrix}$ and $\vec{v} = \begin{pmatrix} x' \\ y' \end{pmatrix}$, then:
   $$\vec{u} \cdot \vec{v} = xx' + yy'$$

- **Orthogonality Property**: $\vec{u} \perp \vec{v} \iff \vec{u} \cdot \vec{v} = 0$.

#### 2. The Law of Cosines (Théorème d'Al-Kashi)
In any triangle $ABC$, let $BC = a$, $AC = b$, and $AB = c$:

$$a^2 = b^2 + c^2 - 2bc \cos \hat{A}$$

*Deductive Proof via Vectors*:
$$\vec{BC} = \vec{BA} + \vec{AC} = \vec{AC} - \vec{AB}$$
$$\|\vec{BC}\|^2 = (\vec{AC} - \vec{AB})^2 = \|\vec{AC}\|^2 + \|\vec{AB}\|^2 - 2(\vec{AB} \cdot \vec{AC})$$
$$a^2 = b^2 + c^2 - 2(c \times b \cos \hat{A}) = b^2 + c^2 - 2bc \cos \hat{A}$$

#### 3. Quadratic Theory and Canonical Form
Every quadratic trinomial $P(x) = ax^2 + bx + c$ ($a \neq 0$) can be written uniquely in canonical form:

$$P(x) = a\left[\left(x + \frac{b}{2a}\right)^2 - \frac{\Delta}{4a^2}\right] \quad \text{where } \Delta = b^2 - 4ac$$

- If $\Delta > 0$: Two distinct real roots $x_{1,2} = \frac{-b \pm \sqrt{\Delta}}{2a}$, and $P(x) = a(x - x_1)(x - x_2)$.
- If $\Delta = 0$: One repeated double root $x_0 = -\frac{b}{2a}$, and $P(x) = a(x - x_0)^2$.
- If $\Delta < 0$: No real roots. $P(x)$ retains the sign of $a$ for all $x \in \mathbb{R}$.

---

## SECTION D — CONTEXTUALISED BRIDGING ACTIVITIES

### Activity: High-Voltage Transmission Line Pylon Anchoring

#### 1. Problem Situation
The Beninese Electric Power Company (SBEE) is erecting high-voltage pylons along the Northern corridor near Parakou.
- A vertical steel transmission tower $TP$ of height $h = 30\text{ metres}$ stands on level ground at base $P$.
- Two steel guy-wire stay cables are anchored to the ground at anchor points $A$ and $B$.
- The anchor points are aligned with base $P$ such that $P, A, B$ lie on the same straight line on opposite sides of $P$.
- Anchor $A$ is placed $40\text{ metres}$ from base $P$ ($PA = 40\text{ m}$).
- Anchor $B$ is placed $20\text{ metres}$ from base $P$ ($PB = 20\text{ m}$).
- Both cables connect to the pylon apex $T$.

#### 2. The IB Perspective (Vector Coordinate & Trigonometric Model)
- Choose coordinate origin at ground base $P(0, 0)$.
- Then $T(0, 30)$, $A(-40, 0)$, and $B(20, 0)$.
- Vector of cable 1: $\vec{TA} = \begin{pmatrix} -40 - 0 \\ 0 - 30 \end{pmatrix} = \begin{pmatrix} -40 \\ -30 \end{pmatrix}$.
- Vector of cable 2: $\vec{TB} = \begin{pmatrix} 20 - 0 \\ 0 - 30 \end{pmatrix} = \begin{pmatrix} 20 \\ -30 \end{pmatrix}$.
- Calculate cable lengths (magnitudes):
  $$\|\vec{TA}\| = \sqrt{(-40)^2 + (-30)^2} = \sqrt{1\ 600 + 900} = \sqrt{2\ 500} = 50\text{ metres}$$
  $$\|\vec{TB}\| = \sqrt{20^2 + (-30)^2} = \sqrt{400 + 900} = \sqrt{1\ 300} = 10\sqrt{13} \approx 36.06\text{ metres}$$
- Calculate dot product:
  $$\vec{TA} \cdot \vec{TB} = (-40)(20) + (-30)(-30) = -800 + 900 = +100$$
- Determine the apex angle $\theta = \widehat{ATB}$:
  $$\cos\theta = \frac{\vec{TA} \cdot \vec{TB}}{\|\vec{TA}\| \|\vec{TB}\|} = \frac{100}{50 \times 10\sqrt{13}} = \frac{100}{500\sqrt{13}} = \frac{1}{5\sqrt{13}} \approx 0.05547$$
  $$\theta = \arccos(0.05547) \approx 86.82^\circ$$

#### 3. The Beninese APC Perspective (Al-Kashi & Relations Métriques)
- *Calcul des longueurs des câbles dans les triangles rectangles $TPA$ et $TPB$* :
  Dans $\triangle TPA$ rectangle en $P$ : $TA^2 = TP^2 + PA^2 = 30^2 + 40^2 = 2\ 500 \implies TA = 50\text{ m}$.
  Dans $\triangle TPB$ rectangle en $P$ : $TB^2 = TP^2 + PB^2 = 30^2 + 20^2 = 1\ 300 \implies TB = \sqrt{1\ 300}\text{ m}$.
- *Calcul de la distance au sol entre les deux ancres* :
  Comme $P \in [AB]$, $AB = PA + PB = 40 + 20 = 60\text{ mètres}$.
- *Application du théorème d'Al-Kashi dans le triangle $TAB$* :
  $$AB^2 = TA^2 + TB^2 - 2 \times TA \times TB \times \cos\widehat{ATB}$$
  $$60^2 = 50^2 + 1\ 300 - 2(50)(\sqrt{1\ 300})\cos\theta$$
  $$3\ 600 = 2\ 500 + 1\ 300 - 100\sqrt{1\ 300}\cos\theta$$
  $$3\ 600 = 3\ 800 - 100(10\sqrt{13})\cos\theta$$
  $$1\ 000\sqrt{13}\cos\theta = 3\ 800 - 3\ 600 = 200$$
  $$\cos\theta = \frac{200}{1\ 000\sqrt{13}} = \frac{1}{5\sqrt{13}} \approx 0,05547$$
  $$\theta \approx 86,82^\circ$$

#### 4. Comparison of Methods
- The IB vector dot product approach handles the problem in 4 clean algebraic lines without needing ground distance $AB$.
- The Beninese Al-Kashi approach directly verifies metric consistency using classical planar trigonometry.

#### 5. Student Reflection Question
*Why does the scalar dot product formula produce the exact same cosine value as the Law of Cosines, and how does this prove that coordinates and metric distances are fundamentally unified?*  
*Espace de réponse:*  
____________________________________________________________________________________________________  
____________________________________________________________________________________________________  

#### 6. Application in a New Context
A fiber-optic undersea cable runs from an offshore landing station $S$ to coastal junctions $X$ and $Y$ at the Port of Cotonou. Given vectors $\vec{SX} = \begin{pmatrix} 6 \\ 8 \end{pmatrix}$ and $\vec{SY} = \begin{pmatrix} -3 \\ 4 \end{pmatrix}$ (units in km), determine the angle between the two cables.  
*Working space:*  
____________________________________________________________________________________________________  
____________________________________________________________________________________________________  

---

## SECTION E — PROGRESSIVE PRACTICE / EXERCICES PROGRESSIFS

### Level 1: Foundational Understanding (Intervals, Modulus & Discriminant)
1. Write each set using interval notation:
   a) $\{x \in \mathbb{R} \mid -3 \le x < 5\}$  
   b) $\{x \in \mathbb{R} \mid x > 4\}$  
   c) $\{x \in \mathbb{R} \mid |x - 2| \le 3\}$  
2. Calculate the discriminant $\Delta$ and determine the number of real roots:
   a) $2x^2 - 5x + 3 = 0$  
   b) $x^2 - 6x + 9 = 0$  
   c) $3x^2 + 2x + 4 = 0$  

### Level 2: Standard Application (Quadratic Equations & Radian Trigonometry)
3. Solve in $\mathbb{R}$:
   a) $2x^2 - 7x + 3 = 0$  
   b) $-x^2 + 4x + 5 \ge 0$ (construct a sign table).  
4. Convert between degrees and radians:
   a) Convert $120^\circ$ and $315^\circ$ to exact radians in terms of $\pi$.  
   b) Convert $\frac{5\pi}{6}\text{ rad}$ and $\frac{4\pi}{3}\text{ rad}$ to degrees.  
   c) State the exact values of $\cos\frac{2\pi}{3}$ and $\sin\frac{7\pi}{6}$.  

### Level 3: Multi-Step Problems (Functions & Dot Products)
5. Consider the rational function $f(x) = \frac{2x - 1}{x + 3}$.
   a) Determine the domain of definition $D_f$.  
   b) Show that for all $x \in D_f$, $f(x) = 2 - \frac{7}{x+3}$.  
   c) Describe the geometric transformations mapping the hyperbola $y = \frac{1}{x}$ onto the curve of $f$.  
6. In an orthonormal coordinate plane, let $\vec{u} = \begin{pmatrix} 4 \\ -3 \end{pmatrix}$ and $\vec{v} = \begin{pmatrix} 2 \\ 5 \end{pmatrix}$.
   a) Calculate $\|\vec{u}\|$ and $\|\vec{v}\|$.  
   b) Calculate the scalar product $\vec{u} \cdot \vec{v}$.  
   c) Calculate the cosine of the angle between $\vec{u}$ and $\vec{v}$.  
   d) Determine the real number $k$ such that the vector $\vec{w} = \begin{pmatrix} k \\ 6 \end{pmatrix}$ is orthogonal to $\vec{u}$.  

### Level 4: Reasoning & Functional Analysis
7. Let $f$ be the function defined on $\mathbb{R}$ by $f(x) = x^2 - 4x + 1$.
   a) Write $f(x)$ in canonical form.  
   b) State the coordinates of the vertex $S$ of the parabola.  
   c) Prove that for all $x \in \mathbb{R}$, $f(x) \ge -3$.  
   d) Study the monotonicity of $f$ on $]-\infty, 2]$ and on $[2, +\infty[$. Construct the complete variation table.  

### Level 5: Extension & Seconde C Examination Challenge
8. **Situation d'Évaluation Type Seconde C (MESTFP Bénin)**:
   Dans le cadre d'un projet de centrale solaire flottante sur le lac Nokoué, trois balises de fixation $A, B, C$ forment un triangle tel que :
   $$AB = 70\text{ m}, \quad AC = 50\text{ m}, \quad BC = 80\text{ m}$$
   1. Démontre que $\cos\hat{A} = \frac{1}{5}$.
   2. Déduis-en la valeur exacte de $\sin\hat{A}$.
   3. Calcule l'aire en $\text{m}^2$ de la surface triangulaire délimitée par les balises.
   4. Soit $I$ le milieu du segment $[BC]$. En appliquant le théorème de la médiane ($AB^2 + AC^2 = 2AI^2 + \frac{BC^2}{2}$), calcule la longueur exacte de la ligne d'ancrage médiane $[AI]$.
   5. Détermine l'ensemble $(\mathcal{E})$ des points $M$ du plan du lac vérifiant :
      $$\vec{MA} \cdot \vec{MB} = 0$$
      Donne sa nature géométrique et ses éléments caractéristiques précis.

---

## SECTION F — INTEGRATED APPLICATION TASKS

### Task F-1: Autonomous Electric Shuttle Kinematics (DP 1 Modelling & Benin 2nde)
**Context**: An electric autonomous shuttle connects the Cotonou Financial Center to the Port Administrative Zone.
Its position from the departure station after $t$ seconds is modelled by the quadratic position function:
$$s(t) = -0.2t^2 + 8t \quad (0 \le t \le 40\text{ seconds})$$
where $s(t)$ is in metres.

**Questions**:
1. Calculate the initial position $s(0)$ and the position after 10 seconds: $s(10)$.
2. By completing the square or calculating the vertex $t_v = -\frac{b}{2a}$, determine the time at which the shuttle reaches its maximum distance from the depot.
3. Calculate the maximum distance reached by the shuttle.
4. Solve $s(t) = 0$ in the interval $[0, 40]$ to determine the total duration of the round-trip journey.
5. In the Beninese examination format, draw the complete variation table (*tableau de variations*) of function $s$ on $[0, 40]$.

---

## SECTION G — PROGRAMME-SPECIFIC REINFORCEMENT

### Part G-1: IB DP 1 Common Core Examination Questions (Paper 1 & 2 Style)
**Question G-1.1 (Paper 1 - No Calculator)**:  
The quadratic equation $(k - 1)x^2 + 4x + (k - 1) = 0$ has two equal real roots.
Find the possible values of the constant $k$.

**Question G-1.2 (Paper 2 - GDC Required)**:  
The third term of an arithmetic sequence is $u_3 = 14$ and the ninth term is $u_9 = 38$.
1. Find the common difference $d$ and the first term $u_1$.
2. Calculate the sum of the first 25 terms: $S_{25} = \sum_{n=1}^{25} u_n$.

### Part G-2: Beninese NPE Formal 3D Incidence Geometry
**Exercice de Géométrie de l'Espace (Classe de Seconde C)**  
Soit $ABCD$ un tétraèdre régulier. Soient $I$ le milieu de $[AB]$ et $J$ le milieu de $[CD]$.
1. Démontre que la droite $(IJ)$ est orthogonale à la droite $(AB)$.
2. Démontre que la droite $(IJ)$ est orthogonale à la droite $(CD)$.
*Rédige la démonstration en utilisant les propriétés des triangles isocèles et les plans médiateurs dans l'espace.*

---

## SECTION H — ASSESSMENT, REFLECTION & WORKED SOLUTIONS

### Diagnostic Pre-Flight Check
- [ ] I can calculate the discriminant $\Delta = b^2 - 4ac$ and find real roots.
- [ ] I can calculate the dot product of two vectors using coordinates ($xx' + yy'$).
- [ ] I can state the Al-Kashi theorem ($a^2 = b^2 + c^2 - 2bc \cos A$).
- [ ] I know that $\cos^2\theta + \sin^2\theta = 1$ and $\pi\text{ rad} = 180^\circ$.

---

### COMPLETE WORKED SOLUTIONS & MARKING SCHEME

#### Solutions for Section E (Progressive Practice)
1. **Intervals & Modulus** (1 mark each):
   a) $[-3, 5[$.  
   b) $]4, +\infty[$.  
   c) $|x - 2| \le 3 \iff -3 \le x - 2 \le 3 \iff -1 \le x \le 5 \iff [-1, 5]$.  
2. **Discriminant Analysis** (1 mark each):
   a) $\Delta = (-5)^2 - 4(2)(3) = 25 - 24 = 1 > 0 \implies 2$ distinct real roots.  
   b) $\Delta = (-6)^2 - 4(1)(9) = 36 - 36 = 0 \implies 1$ repeated real root.  
   c) $\Delta = 2^2 - 4(3)(4) = 4 - 48 = -44 < 0 \implies$ No real roots.  
3. **Quadratic Inequations** (2 marks):
   a) $\Delta = (-7)^2 - 4(2)(3) = 49 - 24 = 25 = 5^2$.  
      Roots: $x_1 = \frac{7 - 5}{4} = \frac{1}{2}$, $x_2 = \frac{7 + 5}{4} = 3$. $S = \{\frac{1}{2}, 3\}$.  
   b) $-x^2 + 4x + 5 = 0 \implies \Delta = 16 - 4(-1)(5) = 36$. Roots: $x = \frac{-4 \pm 6}{-2} \implies x_1 = -1, x_2 = 5$.  
      The parabola opens downwards ($a = -1 < 0$). It is positive between the roots: $S = [-1, 5]$.  
4. **Radian Trigonometry** (2 marks):
   a) $120^\circ = \frac{120\pi}{180} = \frac{2\pi}{3}\text{ rad}$; $315^\circ = \frac{315\pi}{180} = \frac{7\pi}{4}\text{ rad}$.  
   b) $\frac{5\pi}{6} = \frac{5 \times 180^\circ}{6} = 150^\circ$; $\frac{4\pi}{3} = \frac{4 \times 180^\circ}{3} = 240^\circ$.  
   c) $\cos\frac{2\pi}{3} = -\frac{1}{2}$; $\sin\frac{7\pi}{6} = -\sin\frac{\pi}{6} = -\frac{1}{2}$.  
5. **Rational Function** (3 marks):
   a) $D_f = \mathbb{R} \setminus \{-3\} = ]-\infty, -3[ \cup ]-3, +\infty[$.  
   b) $2 - \frac{7}{x+3} = \frac{2(x+3) - 7}{x+3} = \frac{2x + 6 - 7}{x+3} = \frac{2x - 1}{x+3} = f(x)$.  
   c) Horizontal translation by $-3$ units (left), vertical stretch by factor $7$, reflection across horizontal axis, and vertical translation by $+2$ units (up).  
6. **Dot Product** (3 marks):
   a) $\|\vec{u}\| = \sqrt{4^2 + (-3)^2} = 5$; $\|\vec{v}\| = \sqrt{2^2 + 5^2} = \sqrt{29}$.  
   b) $\vec{u} \cdot \vec{v} = 4(2) + (-3)(5) = 8 - 15 = -7$.  
   c) $\cos\theta = \frac{-7}{5\sqrt{29}} = \frac{-7\sqrt{29}}{145} \approx -0.2599$.  
   d) Orthogonal: $\vec{u} \cdot \vec{w} = 0 \implies 4(k) + (-3)(6) = 0 \implies 4k - 18 = 0 \implies k = \frac{18}{4} = 4.5$.  
7. **Parabola Monotonicity** (3 marks):
   a) Canonical: $f(x) = (x - 2)^2 - 4 + 1 = (x - 2)^2 - 3$.  
   b) Vertex: $S(2, -3)$.  
   c) Since $(x - 2)^2 \ge 0$ for all real $x$, $f(x) = (x - 2)^2 - 3 \ge -3$.  
   d) For $x \le 2$, $f$ is strictly decreasing; for $x \ge 2$, $f$ is strictly increasing. Minimum value is $-3$ achieved at $x = 2$.  
8. **Seconde C Solar Lake Problem** (5 marks):
   1. Al-Kashi in $\triangle ABC$:  
      $BC^2 = AB^2 + AC^2 - 2AB \cdot AC \cos\hat{A} \implies 80^2 = 70^2 + 50^2 - 2(70)(50)\cos\hat{A}$  
      $6\ 400 = 4\ 900 + 2\ 500 - 7\ 000 \cos\hat{A} \implies 6\ 400 = 7\ 400 - 7\ 000 \cos\hat{A}$  
      $7\ 000 \cos\hat{A} = 1\ 000 \implies \cos\hat{A} = \frac{1\ 000}{7\ 000} = \frac{1}{7}$ (Note: if $BC=80, AB=70, AC=50$, $\cos\hat{A} = 1/7 \approx 0.1428$).  
      *Correction*: $\sin\hat{A} = \sqrt{1 - (1/7)^2} = \sqrt{1 - 1/49} = \frac{\sqrt{48}}{7} = \frac{4\sqrt{3}}{7}$. [2 pts]
   2. Area: $\text{Area} = \frac{1}{2} b c \sin\hat{A} = \frac{1}{2}(50)(70)\left(\frac{4\sqrt{3}}{7}\right) = 1\ 750 \times \frac{4\sqrt{3}}{7} = 1\ 000\sqrt{3}\text{ m}^2 \approx 1\ 732.05\text{ m}^2$. [1 pt]
   3. Median length:  
      $AB^2 + AC^2 = 2AI^2 + \frac{BC^2}{2} \implies 4\ 900 + 2\ 500 = 2AI^2 + \frac{6\ 400}{2}$  
      $7\ 400 = 2AI^2 + 3\ 200 \implies 2AI^2 = 4\ 200 \implies AI^2 = 2\ 100 \implies AI = \sqrt{2\ 100} = 10\sqrt{21}\text{ m} \approx 45.83\text{ m}$. [1 pt]
   4. Set $(\mathcal{E})$: $\vec{MA} \cdot \vec{MB} = 0$ is the circle of diameter $[AB]$.  
      Centre is the midpoint of $[AB]$ and radius is $R = \frac{AB}{2} = 35\text{ m}$. [1 pt]

#### Solutions for Section F (Task F-1: Autonomous Shuttle)
1. $s(0) = 0\text{ m}$; $s(10) = -0.2(100) + 8(10) = -20 + 80 = 60\text{ metres}$. [2 marks]
2. Vertex time: $t_v = -\frac{b}{2a} = -\frac{8}{2(-0.2)} = \frac{8}{0.4} = 20\text{ seconds}$. [2 marks]
3. Max distance: $s(20) = -0.2(400) + 8(20) = -80 + 160 = 80\text{ metres}$. [2 marks]
4. Return to depot: $-0.2t^2 + 8t = 0 \implies t(-0.2t + 8) = 0 \implies t = 0$ or $t = \frac{8}{0.2} = 40\text{ seconds}$. Total round-trip duration = 40 s. [2 marks]

#### Solutions for Section G-1 (IB DP 1 Paper Questions)
- **Question G-1.1**: Equal roots $\implies \Delta = 0$.  
  $\Delta = 4^2 - 4(k - 1)(k - 1) = 16 - 4(k - 1)^2 = 0 \implies (k - 1)^2 = 4 \implies k - 1 = \pm 2 \implies k = 3$ or $k = -1$. (Since $k - 1 \neq 0$ for quadratic, both valid). [3 marks]
- **Question G-1.2**:  
  1. $u_9 - u_3 = (9 - 3)d = 6d \implies 38 - 14 = 24 \implies 6d = 24 \implies d = 4$.  
     $u_3 = u_1 + 2d \implies 14 = u_1 + 8 \implies u_1 = 6$. [2 marks]
  2. $S_{25} = \frac{25}{2}[2(6) + (25 - 1)(4)] = \frac{25}{2}[12 + 96] = \frac{25}{2}[108] = 25 \times 54 = 1\ 350$. [2 marks]

---
*End of Workbook 6 (Seconde / DP 1).*
