# OAK INTERNATIONAL SCHOOL
# PREMIUM MATHEMATICS ACTIVITY WORKBOOK — CLASS 7
## Grade Level: Première (1ère) / IB DP 2 (Ages 16–17)
**Academic Year:** 2026–2027 | **Series Version:** OIS-WB-1ERE-DP2-V1.0  
**Programmes:** IB Diploma Programme (English - AA/AI HL & SL) & Beninese National APC (Séries C & D)  

---

## SECTION A — STUDENT INTRODUCTION / INTRODUCTION POUR L'ÉLÈVE

### The Pinnacle of Mathematical Rigour: Pre-University Mastery
*Le sommet de la rigueur mathématique et de la préparation universitaire à Oak International School !*

In Première / DP 2, you attain the apex of your secondary mathematical education:
- In **IB Diploma Programme 2 (DP 2)**, you master the core of differential and integral calculus, explore continuous and discrete probability distributions, model non-linear dynamic systems, and finalize your independent **Mathematical Exploration (Internal Assessment)**.
- In **Beninese Première C & D (APC)**, you engage with the demanding national curriculum defined by the MESTFP and *CIAM 1ère SM/SE*: comprehensive study and curve sketching of rational functions with oblique asymptotes, the powerful geometric algebra of **Barycentres of weighted points (*barycentres de points pondérés*)**, level curves (*lignes de niveau*), arithmetic/geometric sequences, and rigorous combinatorics (*dénombrement*).

This workbook provides seamless harmony between Anglo-Saxon analytical calculus and French axiomatic geometry, preparing you to achieve top scores on the IB Diploma exams and national Baccalauréat benchmarks.

---

## SECTION B — BILINGUAL MATHEMATICAL LANGUAGE / GLOSSAIRE BILINGUE

### Calculus, Sequences, Barycentres & Probability

| English Term | French Equivalent (*Terme Français*) | Mathematical Definition & Symbolic Example | Common Translation Pitfalls |
|---|---|---|---|
| **Derivative / Differentiation** | *Dérivée / Dérivation* | $f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$. Rate of change. | In French: *nombre dérivé* (value at a point) vs *fonction dérivée* (the function $f'$). |
| **Tangent line** | *Tangente à la courbe* | Line touching curve at $(x_0, f(x_0))$ with slope $f'(x_0)$: $y = f'(x_0)(x - x_0) + f(x_0)$. | Do not confuse geometric tangent with the trigonometric ratio $\tan\theta$. |
| **Asymptote** | *Asymptote (verticale, horizontale, oblique)* | A line approached by curve $(\mathcal{C}_f)$ as $x \to \pm\infty$ or $x \to x_0$: $\lim [f(x) - (ax+b)] = 0$. | In French: *asymptote oblique* is explicitly tested; in IB it appears in AA HL and AI. |
| **Barycentre / Center of mass** | *Barycentre de points pondérés* | Unique point $G$ such that $\sum_{i=1}^n \alpha_i \vec{GA_i} = \vec{0}$ with $\sum \alpha_i \neq 0$. | Central pillar of Beninese 1ère C/D; absent from standard IB DP mathematics. |
| **Level curve / Contour line** | *Ligne de niveau* | The set of points $M$ satisfying a scalar equation: e.g., $\|\alpha\vec{MA} + \beta\vec{MB}\| = k$. | In French: *lignes de niveau*. Highly tested in Beninese national exams. |
| **Sequence** | *Suite numérique* | A function defined on $\mathbb{N}$: $(u_n)_{n \in \mathbb{N}}$. | English "sequence" = French *suite*. English "series" = sum of terms (*somme des termes*). |
| **Combinations / Binomial coefficient** | *Combinaisons / Coefficient binomial* | $\binom{n}{k} = C_n^k = \frac{n!}{k!(n-k)!}$. Number of unordered subsets. | Note notation: $\binom{n}{k}$ is modern IB; $C_n^k$ or $C_n^p$ is traditional French/CIAM. |
| **Expected value / Mean** | *Espérance mathématique* | $E(X) = \sum x_i P(X = x_i)$. The long-term average outcome. | In French: *espérance mathématique*. |

---

## SECTION C — SHARED CONCEPTUAL FOUNDATIONS

### Unit Theme: Differential Calculus and Curve Analysis

#### 1. The Derivative: Foundation of Dynamic Analysis
Let $f$ be a real function defined on an open interval containing $x_0$:
- The difference quotient (*taux de variation*) is:
  $$\tau(h) = \frac{f(x_0 + h) - f(x_0)}{h} \quad (h \neq 0)$$
- Function $f$ is differentiable at $x_0$ if the limit exists and is finite as $h \to 0$:
  $$f'(x_0) = \lim_{h \to 0} \frac{f(x_0 + h) - f(x_0)}{h}$$
- **Geometric Interpretation**: $f'(x_0)$ is the gradient (slope) of the tangent line to the curve $(\mathcal{C}_f)$ at point $M_0(x_0, f(x_0))$.
- **Equation of the Tangent Line**:
  $$y = f'(x_0)(x - x_0) + f(x_0)$$

#### 2. Differentiation Rules (Universal Toolkit)
For differentiable functions $u$ and $v$ and constant $k \in \mathbb{R}$:
1. Constant: $(c)' = 0$
2. Power rule: $(x^n)' = n x^{n-1} \quad (n \in \mathbb{R}^*)$
3. Constant multiple: $(k u)' = k u'$
4. Sum rule: $(u + v)' = u' + v'$
5. Product rule: $(u \cdot v)' = u'v + uv'$
6. Quotient rule: $\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2} \quad (v(x) \neq 0)$
7. Chain rule: $(g(f(x)))' = g'(f(x)) \cdot f'(x)$, and specifically $(u^n)' = n u^{n-1} u'$ and $(\sqrt{u})' = \frac{u'}{2\sqrt{u}}$.

#### 3. Sign of the Derivative and Monotonicity
- If $f'(x) > 0$ on interval $I$, then $f$ is strictly increasing on $I$.
- If $f'(x) < 0$ on interval $I$, then $f$ is strictly decreasing on $I$.
- If $f'(x) = 0$ at $x_0$ and changes sign across $x_0$, then $f$ achieves a **local extremum** (maximum or minimum) at $x_0$.

---

## SECTION D — CONTEXTUALISED BRIDGING ACTIVITIES

### Activity: Optimization of an Industrial Bio-Ethanol Storage Vat

#### 1. Problem Situation
An agro-industrial refinery in the Zou department (Bohicon) manufactures stainless steel cylindrical storage vats for cassava-based bio-ethanol.
- Each vat must have a fixed interior volume of $V_0 = 54\pi\text{ m}^3$ (approx. $169.65\text{ m}^3$).
- The vat is composed of a vertical cylinder of radius $r$ and height $h$, closed by a flat circular bottom and a flat circular top.
- The company seeks to minimize the total surface area of stainless steel required, thereby minimizing material costs.

#### 2. The IB Perspective (Calculus Optimization & Modelling - Criterion D)
- Formulate the volume constraint:
  $$V = \pi r^2 h = 54\pi \implies r^2 h = 54 \implies h = \frac{54}{r^2} \quad (r > 0)$$
- Formulate the total surface area function $A(r)$:
  $$A(r) = 2\pi r^2 + 2\pi r h = 2\pi r^2 + 2\pi r \left(\frac{54}{r^2}\right) = 2\pi r^2 + \frac{108\pi}{r}$$
- Differentiate with respect to $r$:
  $$\frac{dA}{dr} = 4\pi r - \frac{108\pi}{r^2}$$
- Set derivative to zero for stationary point:
  $$4\pi r - \frac{108\pi}{r^2} = 0 \implies 4\pi r^3 = 108\pi \implies r^3 = \frac{108}{4} = 27 \implies r = \sqrt[3]{27} = 3\text{ metres}$$
- Verify minimum using second derivative:
  $$\frac{d^2A}{dr^2} = 4\pi + \frac{216\pi}{r^3} \implies \text{At } r = 3: \frac{d^2A}{dr^2} = 4\pi + \frac{216\pi}{27} = 4\pi + 8\pi = 12\pi > 0 \implies \text{Strict Minimum!}$$
- Calculate optimum height:
  $$h = \frac{54}{3^2} = \frac{54}{9} = 6\text{ metres}$$
- Notice the remarkable geometric result: optimal height equals the diameter ($h = 2r = 6\text{ m}$).

#### 3. The Beninese APC Perspective (Étude Complète & Démarche de Résolution)
- *Modélisation de la fonction coût matériel* :
  Soit $r \in ]0, +\infty[$ le rayon en mètres.
  La surface totale est donnée par $S(r) = 2\pi(r^2 + \frac{54}{r})$.
- *Calcul de la fonction dérivée* :
  La fonction $S$ est dérivable sur $]0, +\infty[$ comme somme de fonctions dérivables.
  $$S'(r) = 2\pi\left(2r - \frac{54}{r^2}\right) = 2\pi\left(\frac{2r^3 - 54}{r^2}\right) = \frac{4\pi(r^3 - 27)}{r^2}$$
- *Étude du signe de la dérivée* :
  Puisque pour tout $r > 0$, $\frac{4\pi}{r^2} > 0$, le signe de $S'(r)$ est celui de $r^3 - 27 = (r - 3)(r^2 + 3r + 9)$.
  Le trinôme $r^2 + 3r + 9$ a pour discriminant $\Delta = 9 - 36 = -27 < 0$, il est donc strictement positif pour tout $r$.
  Par conséquent :
  - Pour $r \in ]0, 3[$, $S'(r) < 0 \implies S$ est strictement décroissante.
  - Pour $r \in ]3, +\infty[$, $S'(r) > 0 \implies S$ est strictement croissante.
  - En $r = 3$, $S'(r) = 0$, la fonction admet un minimum absolu.
- *Tableau de variations complet* :
  $$\begin{array}{|c|lcccr|} \hline r & 0 & & 3 & & +\infty \\ \hline S'(r) & & - & 0 & + & \\ \hline & +\infty & & & & +\infty \\ S(r) & & \searrow & & \nearrow & \\ & & & 54\pi & & \\ \hline \end{array}$$
- *Conclusion dimensionnelle* :
  Le rayon optimal est $r = 3\text{ m}$, la hauteur est $h = 6\text{ m}$, et la surface minimale est $S(3) = 2\pi(9 + 18) = 54\pi\text{ m}^2 \approx 169,65\text{ m}^2$.

#### 4. Comparison of Methods
- The IB approach emphasizes algebraic compactness and the second derivative concavity test ($\frac{d^2A}{dr^2} > 0$).
- The Beninese APC enforces a full polynomial sign factorization and an explicit variation table (*tableau de variations*).

#### 5. Student Reflection Question
*Why does a cylinder with height equal to its diameter ($h = 2r$) enclose the maximum volume for a given surface area, and how does calculus prove this universal physical law?*  
*Espace de réponse:*  
____________________________________________________________________________________________________  
____________________________________________________________________________________________________  

#### 6. Application in a New Context
An open rectangular parcel at the Sèmè-Kpodji Free Trade Zone is to be fenced along three sides (one side bordered by a canal) using $600\text{ metres}$ of security fencing. Determine the dimensions that maximize the enclosed area.  
*Working space:*  
____________________________________________________________________________________________________  
____________________________________________________________________________________________________  

---

## SECTION E — PROGRESSIVE PRACTICE / EXERCICES PROGRESSIFS

### Level 1: Foundational Understanding (Derivatives & Sequences)
1. Calculate the derivative function $f'(x)$ for each function:
   a) $f(x) = 4x^3 - 5x^2 + 7x - 9$  
   b) $f(x) = \frac{3}{x} - 2\sqrt{x}$ ($x > 0$)  
   c) $f(x) = (3x - 2)^4$  
2. An arithmetic sequence has first term $u_1 = 7$ and common difference $d = 3$.
   a) Calculate the $15^{\text{th}}$ term: $u_{15}$.  
   b) Calculate the sum of the first 15 terms: $S_{15} = \sum_{k=1}^{15} u_k$.  

### Level 2: Standard Application (Rational Functions & Tangents)
3. Let $f(x) = \frac{2x + 1}{x - 3}$ defined on $D_f = \mathbb{R} \setminus \{3\}$.
   a) Calculate $f'(x)$ using the quotient rule.  
   b) Determine the equation of the tangent line $(T)$ to the curve $(\mathcal{C}_f)$ at point $x_0 = 4$.  
   c) Show that $f'(x) < 0$ for all $x \in D_f$. What can you conclude about the monotonicity of $f$?  
4. In a school of 120 students in Cotonou, 10 student delegates are to be chosen from a committee of 25 candidates.
   a) How many distinct delegations can be formed?  
   b) If 15 candidates are girls and 10 are boys, how many delegations consist of exactly 6 girls and 4 boys?  

### Level 3: Multi-Step Problems (Barycentres & Partial Barycentres)
5. **Barycentres in Plane Geometry (Benin 1ère C/D Standard)**:
   Let $ABC$ be a triangle. Let $G$ be the barycentre of the weighted points $\{(A, 2), (B, 3), (C, 1)\}$.
   a) Verify the existence condition for $G$.  
   b) Express $\vec{AG}$ as a linear combination of vectors $\vec{AB}$ and $\vec{AC}$.  
   c) Let $I$ be the partial barycentre of $\{(A, 2), (B, 3)\}$.  
      Show that $G$ is the barycentre of $\{(I, 5), (C, 1)\}$.  
      Deduce that point $G$ lies on segment $[IC]$.  

### Level 4: Reasoning & Complete Functional Curve Sketching
6. Consider the rational function $f$ defined on $\mathbb{R} \setminus \{1\}$ by:
   $$f(x) = \frac{x^2 - 3x + 6}{x - 1}$$
   a) Determine real numbers $a, b, c$ such that for all $x \neq 1$:
      $$f(x) = ax + b + \frac{c}{x - 1}$$
   b) Calculate $\lim_{x \to 1^-} f(x)$ and $\lim_{x \to 1^+} f(x)$. Deduce the equation of the vertical asymptote.  
   c) Calculate $\lim_{x \to \pm\infty} [f(x) - (ax + b)]$. Deduce the equation of the oblique asymptote $(\Delta)$.  
   d) Calculate $f'(x)$, determine its roots, and construct the complete variation table of $f$.  

### Level 5: Extension & Baccalauréat Première C Examination Challenge
7. **Situation d'Évaluation Type 1ère C (Baccalauréat Épreuve Nationale)**:
   Dans un repère orthonormé $(O, \vec{i}, \vec{j})$, on donne les points $A(-1, 2)$ et $B(3, -2)$.
   1. Détermine les coordonnées du barycentre $G$ des points pondérés $(A, 3)$ et $(B, 1)$.
   2. Démontre que pour tout point $M$ du plan :
      $$3\vec{MA} + \vec{MB} = 4\vec{MG}$$
   3. Détermine et construis l'ensemble $(\mathcal{L}_1)$ des points $M$ du plan vérifiant :
      $$\|3\vec{MA} + \vec{MB}\| = 16$$
   4. Détermine et construis l'ensemble $(\mathcal{L}_2)$ des points $M$ du plan vérifiant :
      $$(3\vec{MA} + \vec{MB}) \cdot (\vec{MA} - \vec{MB}) = 0$$

---

## SECTION F — INTEGRATED APPLICATION TASKS

### Task F-1: Renewable Energy Output and Storage Modeling (DP & Baccalauréat)
**Context**: A hybrid solar-biomass minigrid installed in the commune of Kalalé supplies electrical energy to an off-grid hospital.
The power output in kilowatts ($kW$) over a 24-hour cycle ($0 \le t \le 24$, in hours) is modelled by:
$$P(t) = -t^3 + 36t^2 - 288t + 800 \quad (0 \le t \le 24)$$

**Questions**:
1. Calculate the power derivative function $P'(t) = \frac{dP}{dt}$.
2. Factorise $P'(t)$ completely and find all stationary points where $P'(t) = 0$.
3. Determine the times of the day at which power output reaches its local minimum and its absolute maximum.
4. Calculate the maximum electrical power output in kilowatts.
5. In DP 2, calculate the total energy delivered over the 24-hour cycle by finding the definite integral:
   $$E = \int_0^{24} P(t)\,dt$$
   (Recall that $\int t^n\,dt = \frac{t^{n+1}}{n+1}$).

---

## SECTION G — PROGRAMME-SPECIFIC REINFORCEMENT

### Part G-1: IB DP 2 Mathematics Examination Practice (AA / AI Focus)
**Question G-1.1 (Calculus & Normal Distribution)**:  
The lifespan $X$ (in thousands of hours) of LED streetlights in Cotonou is normally distributed with mean $\mu = 50$ and standard deviation $\sigma = 8$:
$$X \sim N(50, 8^2)$$
1. Find the probability that a randomly chosen streetlight lasts longer than 60 thousand hours: $P(X > 60)$.
2. A shipment contains 500 streetlights. How many are expected to fail before 40 thousand hours?

### Part G-2: Beninese National Curriculum (Baccalauréat 1ère C/D Practicum)
**Exercice de Dénombrement et Probabilités (Série D)**  
Une urne contient 4 boules rouges, 5 boules vertes et 3 boules blanches, indiscernables au toucher.
On tire simultanément 3 boules de l'urne.
1. Calcule le nombre total de tirages possibles.
2. Calcule la probabilité de chacun des événements suivants :
   - $A$ : « Les trois boules tirées sont de la même couleur ».
   - $B$ : « Les trois boules tirées sont de trois couleurs différentes ».
   - $C$ : « Le tirage contient au moins une boule blanche ».
3. Soit $X$ la variable aléatoire désignant le nombre de boules blanches tirées.
   - Détermine la loi de probabilité de $X$.
   - Calcule l'espérance mathématique $E(X)$.

---

## SECTION H — ASSESSMENT, REFLECTION & WORKED SOLUTIONS

### Diagnostic Pre-Flight Check
- [ ] I can apply the product rule $(uv)' = u'v + uv'$ and quotient rule.
- [ ] I can find the coordinates of a barycentre: $x_G = \frac{\sum \alpha_i x_i}{\sum \alpha_i}$.
- [ ] I can calculate combinations: $\binom{n}{k} = \frac{n!}{k!(n-k)!}$.
- [ ] I can find limits and equations of vertical and oblique asymptotes.

---

### COMPLETE WORKED SOLUTIONS & MARKING SCHEME

#### Solutions for Section E (Progressive Practice)
1. **Derivatives** (1 mark each):
   a) $f'(x) = 12x^2 - 10x + 7$.  
   b) $f'(x) = -\frac{3}{x^2} - \frac{1}{\sqrt{x}}$.  
   c) $f'(x) = 4(3)(3x - 2)^3 = 12(3x - 2)^3$.  
2. **Arithmetic Sequences** (1 mark each):
   a) $u_{15} = 7 + (15 - 1) \times 3 = 7 + 42 = 49$.  
   b) $S_{15} = \frac{15}{2}(u_1 + u_{15}) = \frac{15}{2}(7 + 49) = \frac{15}{2} \times 56 = 15 \times 28 = 420$.  
3. **Rational Function Tangent** (3 marks):
   a) $f'(x) = \frac{2(x-3) - (2x+1)(1)}{(x-3)^2} = \frac{2x - 6 - 2x - 1}{(x-3)^2} = \frac{-7}{(x-3)^2}$.  
   b) At $x_0 = 4$: $f(4) = \frac{8+1}{4-3} = 9$.  
      $f'(4) = \frac{-7}{(4-3)^2} = -7$.  
      Tangent: $y - 9 = -7(x - 4) \implies y = -7x + 28 + 9 \implies y = -7x + 37$.  
   c) For all $x \in D_f$, $(x-3)^2 > 0$, so $f'(x) = \frac{-7}{(x-3)^2} < 0$. Therefore, $f$ is strictly decreasing on $]-\infty, 3[$ and on $]3, +\infty[$.  
4. **Combinatorics** (2 marks):
   a) $\binom{25}{10} = \frac{25!}{10!15!} = 3\ 268\ 760$ delegations.  
   b) $\binom{15}{6} \times \binom{10}{4} = 5\ 005 \times 210 = 1\ 051\ 050$ delegations.  
5. **Barycentres 1ère C** (3 marks):
   a) $\sum \alpha_i = 2 + 3 + 1 = 6 \neq 0$. Existence guaranteed.  
   b) By definition: $2\vec{GA} + 3\vec{GB} + \vec{GC} = \vec{0} \implies 2\vec{GA} + 3(\vec{GA} + \vec{AB}) + (\vec{GA} + \vec{AC}) = \vec{0}$  
      $6\vec{GA} + 3\vec{AB} + \vec{AC} = \vec{0} \implies 6\vec{AG} = 3\vec{AB} + \vec{AC} \implies \vec{AG} = \frac{1}{2}\vec{AB} + \frac{1}{6}\vec{AC}$.  
   c) By partial barycentres theorem: $I = \text{bar}\{(A, 2), (B, 3)\}$ has weight $2+3=5$.  
      Therefore, $G = \text{bar}\{(I, 5), (C, 1)\}$.  
      This implies $5\vec{GI} + \vec{GC} = \vec{0} \implies \vec{CG} = \frac{5}{6}\vec{CI}$. Points $C, G, I$ are collinear; $G$ lies on segment $[CI]$.  
6. **Curve Sketching with Asymptotes** (4 marks):
   a) Polynomial division: $\frac{x^2 - 3x + 6}{x - 1} = x - 2 + \frac{4}{x - 1}$. So $a = 1, b = -2, c = 4$.  
   b) $\lim_{x \to 1^-} f(x) = -\infty$ and $\lim_{x \to 1^+} f(x) = +\infty \implies$ Vertical asymptote $x = 1$.  
   c) $\lim_{x \to \pm\infty} [f(x) - (x - 2)] = \lim_{x \to \pm\infty} \frac{4}{x - 1} = 0 \implies$ Oblique asymptote $y = x - 2$.  
   d) $f'(x) = 1 - \frac{4}{(x-1)^2} = \frac{(x-1)^2 - 4}{(x-1)^2} = \frac{(x - 3)(x + 1)}{(x-1)^2}$.  
      Roots of $f'(x)$ are $x = -1$ (local max $f(-1) = -5$) and $x = 3$ (local min $f(3) = 3$).  
7. **Baccalauréat Level Curves 1ère C** (5 marks):
   1. $G = \text{bar}\{(A, 3), (B, 1)\}$:  
      $x_G = \frac{3(-1) + 1(3)}{3+1} = \frac{0}{4} = 0$; $y_G = \frac{3(2) + 1(-2)}{4} = \frac{4}{4} = 1$. Point $G(0, 1)$. [1 pt]
   2. Fundamental reduction: $3\vec{MA} + \vec{MB} = (3+1)\vec{MG} = 4\vec{MG}$. [1 pt]
   3. $\|3\vec{MA} + \vec{MB}\| = 16 \iff \|4\vec{MG}\| = 16 \iff 4 MG = 16 \iff MG = 4$.  
      The set $(\mathcal{L}_1)$ is the circle with centre $G(0, 1)$ and radius $R = 4$. [1.5 pts]
   4. Note that $\vec{MA} - \vec{MB} = \vec{BA}$ (independent of $M$).  
      The equation becomes: $4\vec{MG} \cdot \vec{BA} = 0 \iff \vec{MG} \cdot \vec{BA} = 0$.  
      The set $(\mathcal{L}_2)$ is the straight line perpendicular to line $(AB)$ passing through point $G$. [1.5 pts]

#### Solutions for Section F (Task F-1: Kalalé Minigrid)
1. $P'(t) = -3t^2 + 72t - 288$. [2 marks]
2. Factoring: $P'(t) = -3(t^2 - 24t + 96)$.  
   Discriminant: $\Delta = (-24)^2 - 4(1)(96) = 576 - 384 = 192 = (8\sqrt{3})^2 \approx (13.856)^2$.  
   Roots: $t = \frac{24 \pm 8\sqrt{3}}{2} = 12 \pm 4\sqrt{3}$.  
   $t_1 = 12 - 4\sqrt{3} \approx 12 - 6.93 = 5.07\text{ hours}$ (approx. 05:04).  
   $t_2 = 12 + 4\sqrt{3} \approx 12 + 6.93 = 18.93\text{ hours}$ (approx. 18:56). [2 marks]
3. Since leading coefficient is $-3 < 0$, $P'$ changes from negative to positive at $t_1 = 5.07$ (local minimum: pre-dawn) and from positive to negative at $t_2 = 18.93$ (local maximum: evening peak). [2 marks]
4. Maximum power output: evaluate $P(18.93) \approx 1\ 132.55\text{ kW}$. [1 mark]
5. Total energy by integration:  
   $E = \int_0^{24} (-t^3 + 36t^2 - 288t + 800)\,dt = \left[ -\frac{t^4}{4} + 12t^3 - 144t^2 + 800t \right]_0^{24}$  
   $-\frac{24^4}{4} + 12(24^3) - 144(24^2) + 800(24) = -82\ 944 + 165\ 888 - 82\ 944 + 19\ 200 = 19\ 200\text{ kWh}$. [2 marks]

#### Solutions for Section G-2 (Baccalauréat 1ère D Practicum)
1. Total possible draws: $\binom{12}{3} = \frac{12 \times 11 \times 10}{3 \times 2 \times 1} = 220$ outcomes. [1 pt]
2. Probabilities:  
   - $P(A) = \frac{\binom{4}{3} + \binom{5}{3} + \binom{3}{3}}{220} = \frac{4 + 10 + 1}{220} = \frac{15}{220} = \frac{3}{44}$. [1 pt]
   - $P(B) = \frac{\binom{4}{1} \times \binom{5}{1} \times \binom{3}{1}}{220} = \frac{4 \times 5 \times 3}{220} = \frac{60}{220} = \frac{3}{11}$. [1 pt]
   - $P(C) = 1 - P(\text{No white balls}) = 1 - \frac{\binom{9}{3}}{220} = 1 - \frac{84}{220} = \frac{136}{220} = \frac{34}{55}$. [1 pt]
3. Random variable $X \in \{0, 1, 2, 3\}$:  
   - $P(X=0) = \frac{84}{220}$; $P(X=1) = \frac{\binom{3}{1}\binom{9}{2}}{220} = \frac{3 \times 36}{220} = \frac{108}{220}$;  
   - $P(X=2) = \frac{\binom{3}{2}\binom{9}{1}}{220} = \frac{3 \times 9}{220} = \frac{27}{220}$; $P(X=3) = \frac{\binom{3}{3}}{220} = \frac{1}{220}$.  
   - Sum check: $84 + 108 + 27 + 1 = 220$.  
   - Expected value: $E(X) = 0 \times \frac{84}{220} + 1 \times \frac{108}{220} + 2 \times \frac{27}{220} + 3 \times \frac{1}{220} = \frac{108 + 54 + 3}{220} = \frac{165}{220} = \frac{3}{4} = 0.75$. [2 pts]

---
*End of Workbook 7 (Première / DP 2).*
