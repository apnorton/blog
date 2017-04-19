title: A Brief Exploration of a Möbius Transformation
tags:
  - math
categories:
  - math 
    - calculus
date: 2017-04-18 20:05:42
---


As part of a recent homework set in my complex analysis course, I was tasked with a problem that required a slight generalization on part of [Schwarz's Lemma][schwarz]:

> **Lemma (Schwarz):** Let $f$ be analytic on the unit disk with $|f(z)| \leq 1$ for all $z$ on the disk and $f(0) = 0$.  Then $|f(z)| < |z|$ and $f'(0)\leq 1$.  
> If either $|f(z)|=|z|$ for some $z\neq0$ or if $|f'(0)|=1$, then $f$ is a rotation, i.e., $f(z)=az$ for some complex constant $a$ with $|a|=1$. 

The homework assignment asked us (within the context of a larger problem) to consider the case when $f(\zeta) = 0$ for some $\zeta \neq 0$ on the interior of the unit disk.  The secret to this problem was to find some analytic function $\varphi$ that maps the unit disk to itself, but *swaps* $0$ and $\zeta$.  Then, we may consider $\varphi^{-1}\circ f\circ \varphi$ and apply Schwarz's Lemma.

<!-- more -->

## Properties of the transformation

The appropriate map, which is a particular Möbius transformation, is given by the following:

$$\varphi\_\zeta(z) = \frac{\zeta - z}{1-\overline{\zeta}z}$$

Now, if $|z| = 1$, then $|\varphi\_\zeta(z)| = |\overline{z} \varphi\_\zeta(z)| = \left|\frac{\overline{z}\zeta-1}{1-\overline{\zeta}z}\right| = 1$.  Therefore, this map takes the boundary of the unit disk to itself.

Further, this $\varphi\_\zeta$ is analytic within the unit disk, as its only singularity occurs when $|z| > 1$ (since this occurs when $z = \frac{1}{\overline{\zeta}}$ and $\left|\overline{\zeta}\right| < 1$).  And, finally, since $\varphi\_\zeta$ is non-constant, the [maximum modulus principle][maxmod] tells us that $|\varphi\_\zeta(z)| < 1$ when $|z| < 1$.  

Therefore, $\varphi\_\zeta$ maps the unit disk onto itself, where $\varphi\_\zeta(\zeta) = 0$ and $\varphi\_\zeta(0) = \zeta$.

Another useful feature of this map is that it is an involution.   That is, $\varphi\_\zeta^{-1} = \varphi\_\zeta$.  An application of Schwarz's Lemma shows this immediately: since $\varphi\circ\varphi$ fixes *two* points in the unit disk (one of them zero) and satisfies the modulus bound, we can conclude that $\varphi\circ\varphi$ is the identity.  Therefore, $\varphi$ is its own inverse.

## Impact of this map on the unit disk
I was curious what this mapping does to the values on the unit disk.  We've clearly swapped $\zeta$ and $0$, but the map must maintain analyticity on the unit disk, so it must do more than just that.  I wanted to know how this distortion affects the rest of the values on the disk.  So, I wrote a quick Python program to generate a couple of plots:


```python
import numpy as np
import matplotlib.pyplot as plt

from math import pi
from cmath import phase as arg

# Create a 2D grid on which to evaluate the function
xs = np.linspace(-1, 1, num = 700)
ys = np.linspace(-1, 1, num = 700)
X, Y = np.meshgrid(xs, ys)

# Round it off to be only the unit circle
r = np.sqrt(X**2 + Y**2)
X = np.ma.masked_where(r > 1, X)
Y = np.ma.masked_where(r > 1, Y)

# The new "zeta" value
zeta = 0.2 + 0.38j

# The involution, phi
@np.vectorize
def phi(z):
    return (zeta - z) / (1-zeta.conjugate()*z)

vabs = np.vectorize(abs)
varg = np.vectorize(arg)

# Determine the argument and modulus of points on the unit circle
Z  = X+Y*1.0j

F1 = vabs(phi(Z))
F2 = vabs(Z)
F3 = varg(phi(Z))
F4 = varg(Z)

# Plot them all!
F = [F1, F2, F3, F4]
fig, axes = plt.subplots(2, 2)
titles = [
    '|$\\varphi_\\zeta(z)$|', 
    '|$z$|',
    'Arg$(\\varphi_\\zeta(z))$',
    'Arg$(z)$',
]

t = np.linspace(0, 2*pi, 100)

for i, ax in enumerate(np.reshape(axes, (-1,))):
    # draw the heatmap
    ax.pcolormesh(X, Y, F[i])
    
    # draw bounding circle
    ax.plot(np.cos(t), np.sin(t), linewidth=2, color='black')
    
    # adjust the axis labels
    ax.set_aspect('equal')
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    ax.set_title(titles[i])
    
plt.tight_layout() # helps with spacing
plt.show()
```

Below, we've plotted the magnitude and argument (angle) of $z$ and $\varphi\_\zeta(z)$ side-by-side.  We can now see that, in terms of magnitude, it's just as if the map "shifted" over the origin, squeezing and pulling the surrounding values to maintain analyticity.  However, it also *twisted and reflected* the values of $z$ on each circle around the origin.  (This can be seen through the curve of the $\mathrm{Arg}(\varphi\_\zeta(z))$ plot.)

{% asset_img plots.png "Resulting plots" %}

## Conclusion

This doesn't really serve much purpose in and of itself, but it helped build my intuition of what is happening when I apply the function $\varphi$ and developed my abilities in `numpy` and `matplotlib` usage.  The Schwarz Lemma is an interesting topic in Complex Analysis, and I based some of my initial work on a 2010 paper by Dr. Harold P. Boas, entitled [*Julius and Julia: Mastering the art of the Schwarz lemma*][boas].  Of particular note is "Section 3: Change of Base Point," where he develops and discusses the map $\varphi$.

[schwarz]: http://mathworld.wolfram.com/SchwarzsLemma.html
[maxmod]: http://mathworld.wolfram.com/MaximumModulusPrinciple.html
[boas]: https://arxiv.org/abs/1001.0559
