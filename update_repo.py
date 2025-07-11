"""This script copies all notebooks from the vgrid and vgridpandas repos and replaces the vgrid installation instructions with JupyterLite instructions.
"""


import glob
import os
import shutil
from vgrid.utils.download import download_file

# Download vgrid repository
url_vgrid = 'https://github.com/opengeoshub/vgrid/archive/refs/heads/main.zip'
out_zip_vgrid = 'vgrid-main.zip'
download_file(url_vgrid, out_zip_vgrid)

# Download vgridpandas repository
url_vgridpandas = 'https://github.com/opengeoshub/vgridpandas/archive/refs/heads/main.zip'
out_zip_vgridpandas = 'vgridpandas-main.zip'
download_file(url_vgridpandas, out_zip_vgridpandas)

# Setup directories
out_dir = 'content'
notebook_dir = os.path.abspath(os.path.join(out_dir, 'notebooks'))
vgrid_dir = os.path.abspath(os.path.join(notebook_dir, 'vgrid'))
vgridpandas_dir = os.path.abspath(os.path.join(notebook_dir, 'vgridpandas'))

# Copy vgrid notebooks
in_dir_vgrid = 'vgrid-main/docs'
shutil.copytree(in_dir_vgrid + '/notebooks', vgrid_dir, dirs_exist_ok=True)

# Copy vgridpandas notebooks
in_dir_vgridpandas = 'vgridpandas-main/docs'
shutil.copytree(in_dir_vgridpandas + '/notebooks', vgridpandas_dir, dirs_exist_ok=True)

cwd = os.getcwd()

# Convert vgrid notebooks
os.chdir(vgrid_dir)
cmd = "jupytext --to myst *.ipynb"
os.system(cmd)

# Convert vgridpandas notebooks
os.chdir(vgridpandas_dir)
cmd = "jupytext --to myst *.ipynb"
os.system(cmd)

os.chdir(cwd)

# Process all notebooks
notebooks_vgrid = glob.glob(vgrid_dir + '/*.md')
notebooks_vgridpandas = glob.glob(vgridpandas_dir + '/*.md')

files = notebooks_vgrid + notebooks_vgridpandas

for file in files:
    with open(file, 'r') as f:
        lines = f.readlines()

    out_lines = []
    for index, line in enumerate(lines):
        if line.strip() == '# !pip install vgrid' or line.strip() == '# !pip install -U vgrid':
            out_lines.append('%pip install -q vgrid\n')
        
        if line.strip() == '# !pip install vgridpandas' or line.strip() == '# !pip install -U vgridpandas':
            out_lines.append('%pip install -q vgridpandas\n')

        elif (
            line.strip()
            == 'Uncomment the following line to install [vgrid](https://vgrid.vn) if needed.'
        ):
            pass
        elif 'colab-badge.svg' in line and 'jupyterlite' not in lines[index-1]:
            badge = (
                '[![image](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)]'
            )
            baseurl = 'https://demo.vgrid.vn/lab/index.html?path='
            base_dir = os.path.basename(os.path.dirname(file))
            basename = os.path.basename(file).replace('.md', '.ipynb')
            url = baseurl + base_dir + '/' + basename
            badge_url = f"{badge}({url})\n"
            out_lines.append(badge_url)
            out_lines.append(line)
        else:
            out_lines.append(line)

    with open(file, 'w') as f:
        f.writelines(out_lines)

# Convert back to ipynb for vgrid
os.chdir(vgrid_dir)
cmd = "jupytext --to ipynb *.md"
os.system(cmd)

# Convert back to ipynb for vgridpandas
os.chdir(vgridpandas_dir)
cmd = "jupytext --to ipynb *.md"
os.system(cmd)

os.chdir(cwd)

# Remove markdown files
for file in files:
    os.remove(file)

files = [file.replace('.md', '.ipynb') for file in files]

for file in files:
    with open(file, 'r') as f:
        lines = f.readlines()

    out_lines = []
    for index, line in enumerate(lines):
        if '"id":' in line:
            pass
        else:
            out_lines.append(line)

    with open(file, 'w') as f:
        f.writelines(out_lines)

# Clean up downloaded files
shutil.rmtree('vgrid-main')
os.remove('vgrid-main.zip')
shutil.rmtree('vgridpandas-main')
os.remove('vgridpandas-main.zip')