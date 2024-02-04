# hsqc-cosy-paper

Repository for a final paper from my PhD.

The paper itself (both main text and SI) is in the `hcosy.pdf` file.

TODO:

- upload all raw NMR data to a gitHub release
- put the link here
- make sure all scripts can be run with aptenodytes-0.1

THE BELOW IS OUT OF DATE

## Scripts and raw data

Raw NMR data used for the paper can be downloaded from this GitHub release: https://github.com/yongrenjie/abbs-paper/releases/tag/data.
(Look for the `abbs_raw.zip` file.)

Scripts used to plot figures can be found in the `figures` subdirectory of the repository.
Instructions to run them are as follows:

1. Download the data and unzip it.
2. Clone the `v0.1` tag of [`yongrenjie/aptenodytes`](https://github.com/yongrenjie/aptenodytes):
   ```
   git clone --branch v0.1 git@github.com:yongrenjie/aptenodytes
   ```
3. `cd aptenodytes && pip install .`
4. Point the `$nmrd` environment variable (note: lowercase not uppercase) to the unzipped directory.
5. The scripts should now run without errors.
