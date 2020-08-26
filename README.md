# gmic-sphinx
A [Sphinx](https://www.sphinx-doc.org/) extension for displaying [G'MIC](https://gmic.eu/) command results as images using the [gmic-py](https://github.com/dtschump/gmic-py) Python binding.

## Usage
This Sphinx extension adds a new directive name `gmicpic` that takes any gmic expression as input and outputs an image and the gmic command below as caption (other could come later). It has been tested with Sphinx's `html` builder only for now.

It works only with the [reStructuredText (aka ReST) documentation format](https://fr.wikipedia.org/wiki/ReStructuredText), not Markdown or others.

In any of your `.rst` file, add the following:
```rst
.. gmicpic:: your gmic command
```

For example:
```rst
.. gmicpic:: sp earth blur 4 output earthy.png
```
will yield a picture file-named `earthy.png` followed by the command as caption:

![Image of gmic-library-blurred earth](https://github.com/myselfhimself/gmic-sphinx/raw/master/github_images/earthy.png)

sp earth blur 4 output earthy.png

### G'MIC command pre-processing
1. that the `output` parameter is optional.
1. In order to prevent proxy-blocking issues at docs build-time, G'MIC's samples are stored in this extension:
```rst
.. gmicpic:: sp leno blur 4
```
will yield a picture file-named with a unique id `cce2fce2-e6fc-11ea-9e0e-8cec4b8c0881.png` followed by the command as caption:

![Image of gmic-library-blurred leno](https://github.com/myselfhimself/gmic-sphinx/raw/master/github_images/cce2fce2-e6fc-11ea-9e0e-8cec4b8c0881.png)

sp leno blur 4

...implies that leno.png exists in the `gmic_samples` directory (we have done it for you for <=2020 image samples already). 
The resulting implicit `output` image will be pre-stored in gmic-images/ with a unique-id generated `.png` filename.


## Installing & set-up
Install this Python module from pypi.org (in the same virtual environment as Sphinx):
```sh
pip install gmic-sphinx
```

Edit your Sphinx documentation project's `conf.py` file and ensure you have line like:
```python
extensions = ['gmic-sphinx']
```
You might need to add gmic-sphinx to your Python path.

## Projects using this
This extension is used in the following projects:
* [gmic-py](https://github.com/dtschump/gmic-py) // [readthedocs.io documentation](https://gmic-py.readthedocs.io/en/latest/)
* PR to add your project here :)

# License
This project is under the [CeCILL License](https://github.com/myselfhimself/gmic-sphinx/blob/master/LICENSE).
