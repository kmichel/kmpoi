#!/usr/bin/env python3
import os
import sys
import zipfile


output_dir = os.path.realpath(sys.argv[1])
with zipfile.ZipFile(os.path.join(output_dir, 'output.zip'), 'w') as archive:
    for filename in os.listdir(output_dir):
        if filename.endswith('.ger') or filename.endswith('xln'):
            archive.write(
                os.path.join(output_dir, filename),
                filename)
