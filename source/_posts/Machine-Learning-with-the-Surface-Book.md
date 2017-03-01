title: TensorFlow with the Surface Book
tags:
  - computer-science
  - data
categories:
  - computer-science
  - tools
date: 2017-01-04 15:32:45
---


While interning at Microsoft over the summer, I received a first-generation Surface Book with an i5-6300U CPU (2.4 GHz dual core with up to 3.0 GHz), 8GB RAM, and a "GeForce GPU" (officially unnamed, but believed to be equivalent to a GT 940).  This is a huge step up from my older laptop, so I wanted to set it up for my ML work.  In this post, I'll outline how I set it up with TensorFlow and GPU acceleration.

## CUDA + cuDNN

If you want to use GPU acceleration, the typical way to do so is with NVIDIA's CUDA API.  CUDA 8.0 is compatible with the Surface Book and is (as of this writing) the most up-to-date version of CUDA.  Download it [from the NVIDIA website][5] and run their installer.

For work with deep learning, you'll also want to install cuDNN.  To install, just [download][4] the library from NVIDIA's website and unzip it in a convenient place (I chose `C:\cudnn`).  The only "installation" you need to do is to add `C:\cudnn\bin` to your `PATH` environment variable.

<!-- more -->

## Python

GPU acceleration is where you're going to get the best performance improvements when running TensorFlow.  However, we might as well set up Python in a way that will run as fast as we can.  

I installed the [*Intel Distribution for Python*][1].  This is a clone of Python 3.5, but compiled with optimizations for Intel CPUs and packaged with optimized versions of common libraries like `sklearn`, `pandas`, `numpy`, and more.  It's a free download from Intel, but it is officially still in Beta.  Thus far, I haven't run into any problems using it with TensorFlow (but will update this post if I do).

To install Intel Python, just download and run the installer; I installed this to `C:\IntelPython35`.  If you install it in this location, add `C:\IntelPython35\` and `C:\IntelPython35\Scripts` to your `PATH` environment variable.  (Adding `\Scripts` to your path allows you to use `pip` or `jupyter` directly from the commandline.)

If you decide to use a different installation of Python, make sure you're installing Python 3.5 and not the recent release of Python 3.6; as of this writing, installing TensorFlow on Windows with Python 3.6 and above is [not supported][3]. 

## TensorFlow

My understanding is that compiling TensorFlow from source using Intel's `icc` and BLAS/LAPACK libraries will give you the best performance, but I  don't have a permanent license to these, and so just installed with `pip`.

The version of `pip` included with Intel Python is quite old, so the first step here is to upgrade it using `python -m pip install --upgrade pip`.  Following this, we need to download the TensorFlow wheel from Google.  The up-to-date link can be found [here][6], but the current link is for [v0.12.1 with GPU support][7].  (I found that downloading the wheel has better success than running `pip` directly on the URL.)

Finally, execute `pip install --upgrade [TF-downloaded-file]` to install TensorFlow.  This should finish somewhat quickly, and then you are done!

When I first installed TensorFlow, I had some issues with an existing `setuptools` installation and was getting an error similar to:

```
Installing collected packages: six, setuptools, protobuf, numpy, tensorflow
  Found existing installation: setuptools 19.1.1
  **Cannot remove entries from nonexistent file C:\IntelPython35\Lib\site-packages\easy-install.pth**
```

This was [raised as an issue][8] ([and another issue][9]) on the TensorFlow GitHub.  The solution that worked for me was to run the following:

```
pip install -I --upgrade setuptools
pip install --upgrade [TF-downloaded-file]
```

## Testing the Installation

Open up your terminal, and we'll run a few commands: 

```
$ python
...
>>> import tensorflow as tf
...
>>> a = tf.constant(12)
>>> b = tf.constant(30)
>>> sess = tf.Session()
...
>>> print(sess.run(a+b))
42
>>>
```

If it printed 42 at the end, then it works!  I recommend taking a look at the [TensorFlow MNIST tutorials][10] after this, as they introduce TensorFlow's capabilities quite nicely.

At one point, I had a problem where any call to `tf.Session()` or `tf.InteractiveSession()` would cause Python to crash without displaying any error (Windows would display a "This process has stopped responding" dialog box and kill Python after a minute or so).  I never found out *why* this happened, but restarting my computer resolved the issue and I haven't experienced it again.

If you're curious whether your GPU utilized, look at the debug information that was printed after running `tf.Session()`.  If it includes lines like the below (some unnecessary path names trimmed), then the GPU was used:

```
Found device 0 with properties:
name: GeForce GPU
major: 5
minor: 0
memoryClockRate (GHz) 0.993
pciBusID 0000:01:00.0
Total memory: 1.00GiB
```



*Credit where credit is due! When I was performing my install, I was greatly aided by [this blog post][2] from Heaton Research.*

[1]: https://software.intel.com/intel-distribution-for-python
[2]: http://www.heatonresearch.com/2017/01/01/tensorflow-windows-gpu.html
[3]: https://github.com/tensorflow/tensorflow/issues/6533
[4]: https://developer.nvidia.com/cudnn
[5]: https://developer.nvidia.com/cuda-downloads
[6]: https://www.tensorflow.org/get_started/os_setup#pip_installation_on_windows
[7]: https://storage.googleapis.com/tensorflow/windows/gpu/tensorflow_gpu-0.12.1-cp35-cp35m-win_amd64.whl
[8]: https://github.com/tensorflow/tensorflow/issues/622
[9]: https://github.com/tensorflow/tensorflow/issues/135
[10]: https://www.tensorflow.org/get_started/
