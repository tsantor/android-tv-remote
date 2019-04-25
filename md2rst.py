import pypandoc
import os

files = ["README.md", "HISTORY.md"]

for f in files:

    output_filename = os.path.splitext(f)[0] + ".rst"

    # Convert markdown to reStructured
    z = pypandoc.convert(open(f).read(), "rst", format="markdown").encode("utf-8")

    # Replace some RST underline chars that PyPI does not like
    # http://sphinx-doc.org/rest.html#sections
    z = z.replace("~", "^")

    # Write converted file
    with open(output_filename, "w") as outfile:
        outfile.write(z)
