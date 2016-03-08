title: 'Deranged Exams: An ICPC Problem'
date: 2015-10-15 20:24:00
tags:
  - algorithms
  - math
  - contests
categories:
  - computer-science
  - contests
---
This past week, my ICPC team worked the 2013 Greater New York Regional problem packet.  One of my favorite problems in this set was Problem E: Deranged Exams.  The code required to solve this problem isn't that complicated, but the math behind it is a little unusual.  In this post, I aim to explain the math and provide a solution to this problem.


Problem Description
---

The [full problem statement](http://acmgnyr.org/year2013/e.pdf) is archived online; in shortened form, we can consider the problem to be:

> Given a "matching" test of $n$ questions (each question maps to exactly one answer, and no two questions have the same answer), how many possible ways are there to answer at least the first $k$ questions wrong?

It turns out that there's a really nice solution to this problem using a topic from combinatorics called "derangements."  (Note that the problem title was a not-so-subtle hint towards the solution.)


Derangements
---

While the idea of a permutation should be familiar to most readers, the closely related topic of a derangement is rarely discussed in most undergraduate curriculum.  So, it is reasonable to start with a definition:

> A derangement is a permutation in which no element is in its original place.  The number of derangements on $n$ elements is denoted $D_n$; this is also called the subfactorial of $n$, denoted $!n$. 

The sequence $\langle D_n\rangle$ is [A000166](https://oeis.org/A000166) in OEIS (a website with which, by the way, every competitive programmer should familiarize themselves).


It turns out that there is both a recursive and an explicit formula for $D_n$:

{% math %}
\begin{aligned}
D_n &= (-1)^n \sum_k\binom{n}{k} (-1)^k k! \\
&= n\cdot D_{n-1} + (-1)^n;\;(D_0=1)
\end{aligned}
{% endmath %}

This is significant because we can use the explicit formulation for computing single values of derangements, or we can use dynamic programming to rapidly compute $D_n$ for relatively small $n$.

Problem Approach
---

The key observation here is that, using the derangement formula, we may compute the number of ways to answer a given set of questions incorrectly, using only the answers corresponding to those questions.  Instead of focusing on the first $k$ questions, which we must answer incorrectly, let us look to the remaining $n-k$ questions.


Consider the case when we answer $r$ questions correctly.  There are $\binom{n-k}{r}$ ways of choosing which $r$ questions we answer correctly (since the first $k$ must be wrong).


The remaining $n-r$ questions must be answered incorrectly using only the answers to the same $n-r$ questions.  Using our knowledge of derangements, there are $!(n-r)$ ways to assign those incorrect answers.


Finally, note that the number of correct answers, $r$ is bounded by $n-k$; summing over all possible values of $r$, we obtain:

$$S(n, k) = \sum_{r=0}^{n-k} \binom{n-k}{r}\cdot !(n-r)$$

Code
---

Equations are great, but implementation is required for ICPC.  First, we must consider input/output size.  The problem statement gives the following ranges for $n$ and $k$:

$$\begin{aligned}
  1 \leq n \leq 17 \\\\
  0 \leq k \leq n 
\end{aligned}$$


We can expect that this will fit in a 64-bit integer, as $n! \leq 2^{63}-1$ for $n\leq 20$.  Thus, we don't even need to be careful in computing binomial coefficients due to intermediate overflow!  I'll let the code (and comments) speak for itself:

```
import java.util.*;
 

public class Test {
  // Basic iterative factorial; just multiply all
  // the numbers less than or equal to n.
  // returns 1 if n < 1 (which is important for n=0)
  private static long fact(int n) {
    long retval = 1; 
    while(n > 0) 
      retval *= n--;
    return retval;
  }

  // Naive binomial coefficient computation 
  // Generally, you need to watch overflow.  But,
  // we can ignore that here because fact(17) < 2^63-1
  private static long binom(int n, int k) {
    return fact(n)/(fact(k)*fact(n-k));
  }
 
  public static void main(String[] args) { 
    //While not recommended in general, we can use 
    // a scanner because we're not reading a lot of input.
    Scanner cin = new Scanner(System.in);
 
    // Precompute the derangement numbers
    long[] d = new long[18]; // we might need values of D_n up to n=17
    d[0] = 1;
    for (int i = 1, j=-1; i < d.length; i++, j*=-1)
      d[i] = i*d[i-1] + j;
    //Process the input
    int P = cin.nextInt();
    for (int caseNum = 0; caseNum < P; caseNum++) {
      cin.nextInt();
      int n = cin.nextInt();
      int k = cin.nextInt();
 
      //S(n, k) = sum(binom(n-k, r)*d[n-r], r=0..n-k)
      long ans = 0;
      for (int r = 0; r <= n-k; r++)
         ans += binom(n-k, r)*d[n-r];
 
      System.out.printf("%d %d\n", caseNum+1, ans);
    }
  }
}
```

Further Reference
---

Derangements are discussed in Concrete Mathematics by Graham, Knuth, and Patashnik on pages 193-196.  In those pages, the identities shown in this blog entry are derived.  Also discussed is a closely related problem that may be called $r$-derangements.


In the $r$-derangement problem, we seek the number of arrangements in which exactly $r$ elements are in their original place.  (The number of $0$-derangements, then, is just $D_n$.)
