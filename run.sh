# Description: Run the reconstruction pipeline
# Author: Tingrui Guo

set -e
export LANG=en_US.UTF-8

eval "$(conda shell.bash hook)"
conda activate pnp

# download images
python crawler.py

# filter images by shape (min(shape) < 480)
python filter.py

# renumber images
python renumber.py
