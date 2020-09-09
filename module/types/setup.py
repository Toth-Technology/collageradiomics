import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

with open('VERSION') as version_file:
    version = version_file.read().strip()

setuptools.setup(
    name='collageradiomicstypes',
    version=version,
    author='Toth Technology',
    author_email='toth-tech@hillyer.me',
    description='CoLliage Implementation',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/radxtools/collageradiomics',
    project_urls={
        'Docker Examples': 'https://hub.docker.com/repository/docker/ccipd/collageradiomics-examples',
        'Docker Module': 'https://hub.docker.com/repository/docker/ccipd/collageradiomics-pip',
        'GitHub': 'https://github.com/radxtools/collageradiomics'
    },
    py_modules=['collageradiomicstypes'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Operating System :: MacOS',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ],
    python_requires='>=3.6',
    keywords='radiomics cancerimaging medicalresearch computationalimaging',
)
