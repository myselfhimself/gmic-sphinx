from html5lib import parse
import pytest

import os
import os.path
import subprocess
import re


@pytest.mark.parametrize("gmic_sphinx_expression,expected_image_path_pattern,expected_caption",
                         [(".. gmicpic:: sp leno blur 4", r"_images/[a-z0-9\-]+.png", "sp leno blur 4"),
                          (".. gmicpic:: sp earth blur 4 output hey.png", r"_images/hey\.png",
                           "sp earth blur 4 output hey.png")])
def test_gmicpic(gmic_sphinx_expression, expected_image_path_pattern, expected_caption):
    with open("docs/index.rst", "w") as index_rst:
        index_rst.write(gmic_sphinx_expression)

    subprocess.run(["make", "html"], cwd=os.path.join(os.getcwd(), "docs"), capture_output=True)
    print(os.listdir("docs"))

    with open("docs/_build/html/index.html") as index_html:
        html = index_html.read()
        root = parse(html)
        print(root)

        figure_divs = root.findall(".//*[@class='figure align-default']")
        assert len(figure_divs) == 1
        img = figure_divs[0][0]
        assert img.tag.split('}')[1] == 'img'

        src = img.get('src')
        path_regex = re.compile(expected_image_path_pattern)
        assert path_regex.match(src)
        assert os.path.isfile(os.path.join("docs/_build/html", src))

        caption = figure_divs[0][1]
        assert caption.tag.split('}')[1] == 'p'

        caption_text = caption[0]
        assert caption_text.text == expected_caption
