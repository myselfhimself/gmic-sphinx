import os
import os.path
import re
import uuid
import tempfile

from docutils import nodes
from docutils.parsers.rst import Directive

import gmic

CURRENT_SCRIPT_DIR_NAME = os.path.dirname(os.path.realpath(__file__))

class GmicPic(Directive):
    required_arguments = 1
    optional_arguments = 25
    has_content = False
    #OUTPUT_DIR_NAME = os.path.join(CURRENT_SCRIPT_DIR_NAME, "output")
    OUTPUT_DIR_NAME = os.path.relpath(tempfile.mkdtemp(prefix="gmic_sphinx", dir=os.getcwd()))
    SAMPLES_DIR_NAME = os.path.join(CURRENT_SCRIPT_DIR_NAME, "samples")

    def run(self):
        original_command = " ".join(self.arguments)

        gmic_command = self.replace_gmic_sp(original_command)
        gmic_command, output_filename = self.replace_and_get_gmic_output(gmic_command)
        print("OUTPUT FILENAME", output_filename)

        print("WILL RUN", gmic_command)
        gmic.run(gmic_command)
        image_node = nodes.image(uri=output_filename)
        return [image_node, nodes.paragraph(text=original_command)]

    def replace_gmic_sp(self, gmic_command):
        pattern = re.compile(r'sp ([a-z]+)')
        search = pattern.search(gmic_command)
        if search:
            sample_name = search.group(1)
            related_sample_file = os.path.join(self.SAMPLES_DIR_NAME, "sample_" + sample_name + ".png")
            gmic_command = re.sub(pattern, related_sample_file, gmic_command)

        return gmic_command

    def replace_and_get_gmic_output(self, gmic_command):
        pattern = re.compile(r'output ([^\s]+)')
        search = pattern.search(gmic_command)
        if search:
            output_filename = search.group(1)
            real_filename = os.path.join(self.OUTPUT_DIR_NAME, output_filename)
            gmic_command = re.sub(pattern, "output " + real_filename, gmic_command)
        else:
            real_filename = os.path.join(self.OUTPUT_DIR_NAME, str(uuid.uuid1()) + ".png")
            gmic_command = "{} output {}".format(gmic_command, real_filename)

        return gmic_command, real_filename


    def generate_gmic_output(self, gmic_command):
        gmic.run(gmic_command)

def setup(app):
    app.add_directive("gmicpic", GmicPic)

    return {
        'version': '0.2',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
