from distutils.core import setup

setup(
    name='SegLoss',
    version='0.1.08',
    author='Justin Harder',
    author_email='justin@algrthm.com',
    packages=['losses_pytorch'],
    description='Losses for pytorch segmentation models',
    long_description=open('README.md').read(),
    install_requires=[
        "numpy",
        "opencv-python",
        "albumentations",
        "dropblock",
        "torchvision",
        "opensimplex",
        "pytorch"
    ],
)
