# hsqc-cosy-paper

Repository for a final paper from my PhD.

The paper itself (both main text and SI) is in the `hcosy.pdf` file.

## Scripts and raw data

Raw NMR data used for the paper can be downloaded from this GitHub release: https://github.com/yongrenjie/hsqc-cosy-paper/releases/tag/data.
(Look for the `hcosy_raw.zip` file.)

Scripts used to plot figures can be found in the `figures` subdirectory of the repository.
Instructions to run them are as follows:

1. Download the data and unzip it.
1. Set up a Python virtual environment with the appropriate dependencies:
   ```
   python -m venv venv
   source venv/bin/activate
   python -m pip install -r requirements.txt
   ```
1. Point the `$nmrd` environment variable (note: lowercase not uppercase) to the unzipped directory.
1. The scripts should now run without errors.

   NOTE: there will be lots of warnings from seaborn about keyword arguments that will be deprecated.
   This does not stop the scripts from working!
   In `aptenodytes==0.2` the version of `seaborn` is pinned to 0.13.x so as long as you managed to install that it should never use a version of `seaborn` that is too new.
