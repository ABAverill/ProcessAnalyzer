from distutils.core import setup
setup(
  name = 'ProcessAnalyzer',         # How you named your package folder (MyLib)
  packages = ['ProcessAnalyzer'],   # Chose the same as "name"
  version = '0.5',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Library for common process variable analysis tools',   # Give a short description about your library
  author = 'Andrew Averil',                   # Type in your name
  author_email = 'andrew.b.averill@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/ABAverill/ProcessAnalyzer',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/ABAverill/ProcessAnalyzer/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['Process', 'Manufacturing', 'Analysis', 'Control Chart'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'pandas',
'plotly.express',
'seaborn',
'numpy' ,
'sklearn',
'shap'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.9',      #Specify which pyhton versions that you want to support

  ],
)


