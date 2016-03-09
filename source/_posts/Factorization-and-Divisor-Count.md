title: Factorization and Divisor Count
date: 2014-07-14 11:59:15
tags:
  - algorithms
  - math
  - number-theory
  - project-euler
categories:
  - math
  - number-theory
---

How many divisors are there of the number $1281942112$?  It turns out that determining the answer to this problem is (at most) only as difficult as determining the prime factorization of the number.  In this blog post, I will outline a solution to this (and similar) problems.


The Math
---

The [Fundamental Theorem of Arithmetic](http://mathworld.wolfram.com/FundamentalTheoremofArithmetic.html) guarantees each positive integer greater than $1$ a unique prime factorization.  We write this factorization as:

$$N = p\_0^{e\_0}p\_1^{e\_1}\cdots p\_n^{e\_n}$$

where $p\_k$ is a prime number, and $e\_k$ is its corresponding exponent.  This provides us with useful information regarding divisors of $N$: any divisor of $N$ must be comprised of some combination of those prime factors (and exponents).  Specifically, we can define the divisor, $D$, as:

$$D = p\_0^{a\_0}p\_1^{a\_1}\cdots p\_n^{a\_n}$$

where the $p\_k$ are the same as in the factorization of $N$ and $a\_k \in \{0, 1, \ldots, e\_k\}$.  To find the total number of divisors, we multiply together the number of options we have for each exponent.  That is,

$$\text{Number of Divisors}\; = (e\_0+1)(e\_1+1)\cdots(e\_n + 1)$$


Example:  Consider $N = 20$.  In this case, $N$ has $6$ divisors; to determine this without needing to list them all, we may note that $N = 2^2\cdot 5^1$.  Using the notation described above, this means that $p\_0 = 2,\;p\_1 = 5$ and $e\_0 = 2\;e\_1 = 1$.  Each of our divisors will be of the form $2^{a\_0}\cdot 5^{a\_1}$, where $a\_0$ could be $0, 1,$ or $2$ and $a\_1$ could be $0$ or $1$.  Since we have $e\_0+1 = 3$ options for $a\_0$ and $e\_1+1 = 2$ options for $a\_1$, we have $3\cdot 2 = 6$ total divisors.  In case you were wondering, the list of divisors is:

$$\{2^0 5^0, 2^1 5^0,2^2 5^0,2^0 5^1,2^1 5^1,2^2 5^1\}$$

<!-- more -->

The Program
---

We're not out of the woods yet--we have a formula, but we need to write a program to make use of it.  The first thing our program needs is a list of primes.  I'm going to assume you have a function already that can generate a list of primes.  A prime-listing function is an important tool in any programmer's toolkit, but I'll save that for a future post.


The pseudocode for our program is below:

```
numberOfDivisors: int N -> int divisorCount
  divisorCount = 1
  for (p = 1 to floor(sqrt(N)) && p prime):
    exponent = 0 

    //Determine exponent of p in prime factorization
    while (p divides N):
      exponent++
      N = N / p


     //Update divisorCount
     divisorCount = divisorCount * (exponent + 1)


    //In this case, there is one prime factor greater than the square root of N
    if (N != 1) divisorCount = divisorCount * 2


  return divisorCount
```

This is mostly straightforward: We iterate through all prime numbers less than the square root of N.  For each prime, we determine how many times it divides N--this is that prime's exponent.  We then multiply the current divisor count by one more than the exponent.  I have pushed an update to my [math GitHub repository](https://github.com/apnorton/math) that includes a Java version of this algorithm in NumberTheory.java.


If we kept track of which primes divide $N$ (for example, adding them to a List whenever we enter the while loop) this program is easily modified to output the prime factorization of a number.

The Analysis
---

Before analyzing the performance of the algorithm, it would be best to explain why we only need to use primes less than $\sqrt{N}$, not primes less than $N$.  This is because **there can only be one prime factor of $N$ greater than $\sqrt{N}$, and (if there is one) it must have only be raised to the $1$st power.**  A proof by contradiction works well here (I'm skipping some rigor, please don't kill me):


> Assume that there are two prime factors (not necessarily unique) $p$ and $q$ of $N$, such that $p,q \gt \sqrt{N}$.  Let the product of the remaining prime factors be some integer $m$.  Then we have:
>
>    $$\begin{align}
       N &= p\cdot q\cdot m \\
         &\le p\cdot q \\
         &\lt \sqrt{N}\sqrt{N}\\
         &\lt N\end{align}$$
>
> This is clearly a contradiction, thus we have proven that there cannot be at least two prime factors of $N$ greater than $\sqrt{N}$.  Equivalently, there may only at most one prime factor of $N$ greater than $\sqrt{N}$.


This explains why we don't need to use primes greater than $\sqrt{N}$: if, after "dividing out" all primes less than $\sqrt{N}$, we are left with a number, then that number must be the single prime factor of $N$ greater than $\sqrt{N}$.


On to the performance of the algorithm.  Assuming we are *given* a list of prime numbers (and don't have to compute them), this procedure has a time complexity of $\mathcal{O}\left(\pi\left(\sqrt{N}\right)\text{lg}(N)\right)$ and $\Omega\left(\pi\left(\sqrt{N}\right)\right)$, where $\pi(x)$ is the [prime counting function](http://mathworld.wolfram.com/PrimeCountingFunction.html) and $N$ is the input number.  ($\Omega$ provides a lower bound, and $\mathcal{O}$ provides an upper bound.)  Let's see why.


We have an outer-most for loop that makes one iteration for each prime less than $\sqrt{N}$.  This gives us the "$\pi\left(\sqrt{N}\right)$" part of the bounds.  For the lower bound, we would assume the inside of the for loop executes in constant time, every time.  (That is, we never enter the while loop.)  This occurs when $N$ is a prime number.  For the upper bound, we may assume that we execute the while loop at most $\text{lg}(N)$ times each iteration.  This is because $\text{lg}(N) = \log\_2(N) \gt \log\_b(N)$ for $N \gt 2$ and integer $b\gt 2$, and $\lfloor\log\_{p\_k}(N)\rfloor$ provides a fairly close upper bound on the exponent of $p\_k$ in the prime factorization of $N$.


The upper bound can be improved by performing some summation and simplification, but it's close enough to show how fast this algorithm is.
