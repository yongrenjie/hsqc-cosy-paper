# hsqc-cosy-paper

Repository for a final paper from my PhD.

The paper itself (both main text and SI) is in the `hcosy.pdf` file.

## Scripts and raw data

Raw NMR data used for the paper can be downloaded from this GitHub release: https://github.com/yongrenjie/hsqc-cosy-paper/releases/tag/data.
(Look for the `hcosy_raw.zip` file.)

Scripts used to plot figures can be found in the `figures` subdirectory of the repository.
Instructions to run them are as follows:

1. Download the data and unzip it.
2. Clone the `v0.2` tag of [`yongrenjie/aptenodytes`](https://github.com/yongrenjie/aptenodytes):
   ```
   git clone --branch v0.2 git@github.com:yongrenjie/aptenodytes
   ```
3. `cd aptenodytes && pip install .`
4. Point the `$nmrd` environment variable (note: lowercase not uppercase) to the unzipped directory.
5. The scripts should now run without errors.

   NOTE: there will be lots of warnings from seaborn about keyword arguments that will be deprecated.
   This does not stop the scripts from working!
   In `aptenodytes` the version of `seaborn` is pinned to 0.13.x so as long as you managed to install that it should never use a version of `seaborn` that is too new.
