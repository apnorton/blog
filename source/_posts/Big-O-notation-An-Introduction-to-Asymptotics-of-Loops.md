title: '"Big-O" notation: An Introduction to Asymptotics of Loops'
date: 2014-06-09 23:28:45
tags:
  - algorithms
  - math
categories:
  - computer-science
  - algorithms

---

Algorithmic efficiency is imperative for success in programming competitions; your programs must be accurate and fast.  To help evaluate algorithms for speed, computer scientists focus on what is called  "asymptotics," or "asymptotic analysis."  The key question answered by asymptotics is: **"When your input gets *really* big, how many steps does your program take?"**  This post seeks to explain basic asymptotic analysis and its application to computing simple program runtime.


The underlying principle of asymptotic analysis is that a program's runtime depends on the number of *elementary operations* it performs.  The fewer elementary operations, the faster the program (and vice-versa).  What do I mean by "elementary operation?"  By this, I refer to any operation such that the runtime is not affected by the input size.  This is more commonly referred to as a *constant-time* operation.  Examples of such operations are assignment, basic arithmetic operations (`+, -, *, /, %`), accessing an array element, increment/decrement operations, function returns, and boolean expressions. 


A First Example
--

So, a good way of gauging the runtime of a program is to count the number of elementary operations it performs.  Let's jump right in by analyzing a simple program. 

```
public static int test(int N) {
  int i = 0;

  while(i < N) {
    i++;
  }
  return i;
}
```

Obviously, this program always returns $N$, so the loop is unnecessary.  However, let's just analyze the method as-is.


Lines 2 and 7 each contribute one constant-time operation.  The loop contributes two constant-time operations per iteration (one for the comparison, one for the increment), plus one extra constant-time operation for the final comparison that terminates the loop.  So, the total number of operations is:


$$1 + 1 + \underbrace{\sum\_{i = 0}^N 2}\_{\text{loop operations}} + 1 = 3 + 2N$$

(Notice how I used sigma (summation) notation for counting a loop's operation. This is useful, because loops and sigma notation behave in much the same way.)


Thus, it will take $3+2N$ operations to perform that method, given an input $N$.  If each operation takes $2\times 10^{-9}$ (about the speed of a 2 GHz processor), it would take 5 seconds to run this program for an input of $N=10^{10}$.

<!-- more -->

Let's make that easier...
---

That was a lot of work for such a simple result; is there an easier way to get a similar answer?  Fortunately, the answer is ***yes!***

First, let us introduce something that we will call "Big-O notation."  This is a way of describing the long-term growth of a function.  The rigorous definition of Big-O is beyond the scope of this blog, but the following should suffice:

> We say $f(n)$ is $\mathcal{O}(g(n))$ if and only if a constant multiple of $g(n)$ is greater than $f(n)$, when $n$ is sufficiently large.  Simply put, this means that, in the long term, $g$ grows as fast or faster than $f$.

As an example, we can say that $f(n) = 3n+2$ is $\mathcal{O}(n)$, because the function $g(n) = n$ grows exactly as fast as $f(n)$.  Or, we can say, $f$ is $\mathcal{O}(n^2)$, because $n^2$ grows faster than $f$, for sufficiently large $n$.  Basically, this means we can ignore two things:

 1. We can ignore anything that is "small" in the long-term.  For example, if $f(x) = 4x^3 + 2x + 3 + \frac{1}{x}$, everything except the "$4x^3$" part becomes small (in comparison) as $x$ gets big.
 2. We can also ignore coefficients.  That is, we don't have to worry about the difference between $4x^3$ and $x^3$.  As $x$ gets really big, the two graphs are so close that it doesn't really matter.


To apply this to algorithm analysis, this means that we only have to worry about the "biggest time-user," rather than all the individual steps.  For most simple programs, this means focusing on loops.  (In advanced problems, you must account for recursion.)


Next, we recall that a single loop can be represented with a single summation sign.  One can fairly quickly see that a nested loop can be represented with a "sum of sums," or multiple, nested summation signs.  It can be proven that:

$$ \underbrace{\sum\_N\left(\sum\_N\left(\cdots\sum\_N f(N)\right)\right)}_{k \text{ summation signs}} = \mathcal{O}(N^k\cdot f(N)) $$

> **Important Result**     
> Interpreted into programmer-speak, this means that *a program with nested loops (each executing ~$N$ times) to a maximum depth of $k$ will take $\mathcal{O}(N^k)$ operations to complete said loops.*

Another Example
---


So, let's apply this idea to a bit more complicated program:

```
public static int test(int N) {
  int total = 0;
  
  for (int i = 0; i < N; i++) {
    for (int j = i; j < N; j++) {
      total++;
    }
  }
  
  return total;
}
```

Now we have a nested loop!  Looking at this program, we realize that the "deepest" nesting is only $2$ deep.  Thus, by our important result, we know that this program runs in $\mathcal{O}(N^2)$ time.


This means, that as $N$ gets very large, doubling the input will result in a *quadruple* increase in runtime.

Other Notes
---

Obviously, there are more cases that can arise in algorithm analysis, instead of the simple loops given above.  For example, recursion and atypical loops (e.g. loops that double the counter each iteration, rather than adding one) require other methods than the "Important Result" I gave here.  Fortunately, there are a few common designations that arise:

$$ \mathcal{O}(\log_2(n)),\;\mathcal{O}(n^k),\;\mathcal{O}(2^n),\;\mathcal{O}(n!),\;\mathcal{O}(n^n) $$

I will note that I have written the above in increasing order of runtime.  That is, an algorithm that runs in $\mathcal{O}(\log_2(n))$ is faster than one that runs in $\mathcal{O}(2^n)$, etc.


One can spend many hours studying asymptotic calculations.  In fact, there's an entire chapter devoted to this in Concrete Mathematics by Graham, Knuth, and Patashink.  (I *highly* recommend this book to anyone interested in programming; it is, quite literally, the best book I have ever opened related to computer science.)  For a thorough guide of the application of asymptotic calculations to programs, I recommend consulting a good Algorithms and Data Structures text.
