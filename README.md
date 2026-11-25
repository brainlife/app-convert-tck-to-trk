[![Abcdspec-compliant](https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg)](https://github.com/brain-life/abcd-spec)
[![Run on Brainlife.io](https://img.shields.io/badge/brainlife.app.133-blue.svg)](https://doi.org/10.25663/brainlife.app.133)

# app-convert-tck-to-trk

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

**Converts an MRtrix .tck tractogram to TrackVis .trk format with nibabel, using a T1-weighted image as the reference space for the trk header; a format conversion utility.**

Loads the .tck streamlines with nibabel and saves them as track.trk with the voxel-to-RAS affine, voxel sizes, dimensions and voxel order taken from the T1-weighted NIfTI. Use it when a downstream tool needs .trk; the streamlines are not transformed, so the tractogram must already be in the space of the T1-weighted image.

Run it on brainlife.io: [https://doi.org/10.25663/brainlife.app.133](https://doi.org/10.25663/brainlife.app.133)

| Input | Datatype | Required | Description |
|---|---|---|---|
| `t1` | `neuro/anat/t1w` | yes | T1-weighted NIfTI image that provides the reference space (affine, voxel size, dimensions) for the output trk header. The tck streamlines must already be in the space of this T1 image. |
| `tck` | `neuro/track/tck` | yes | A tractogram encoded according to the Mrtrix specifications. |

| Output | Datatype | Description |
|---|---|---|
| `trk` | `neuro/track/trk` | The tractogram encoded following the TRK specifications. The reference space of streamlines is redefined according to the space of the T1 file given in input. |

Runtime: container `brainlife/dipy:0.13`; 8 CPUs; 0.17 h walltime.

Please cite:
- Avesani P, McPherson B, Hayashi S, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. Sci Data 6, 69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

<!-- brainlife-app:end -->

This service will convert a .tck file to .trk file format using nibabel. 

### Authors
- Paolo Avesani (pavesani@iu.edu)

### Contributors
- Soichi Hayashi (hayashis@iu.edu)

### Project Director
- Franco Pestilli (franpest@indiana.edu)

### Funding 
[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)

### Reference
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1464282.svg)](https://doi.org/10.5281/zenodo.1464282)

## Running the App 

### On Brainlife.io

You can submit this App online at [https://doi.org/10.25663/brainlife.app.133](https://doi.org/10.25663/brainlife.app.133) via the "Execute" tab.

### Running Locally (on your machine)

1. git clone this repo.

2. Inside the cloned directory, create `config.json` with something like the following content with paths to your input files.

```json
{
        "tck": "./input/track/track.tck",
	"dwi": "./input/dtiinit/dwi_aligned_trilin_noMEC.nii.gz"
}
```

If you have singularity installed on your local machine:

3. Launch the App by executing `main`

```bash
./main
```

Otherwise:

3. Ensure you have the proper dependencies installed for python and execute main.py directly. 

### Sample Datasets

If you don't have your own input file, you can download sample datasets from Brainlife.io, or you can use [Brainlife CLI](https://github.com/brain-life/cli).

```
npm install -g brainlife
bl login
mkdir input
bl dataset download 5a0e604116e499548135de87 && mv 5a0e604116e499548135de87 input/track
bl dataset download 5a0dcb1216e499548135dd27 && mv 5a0dcb1216e499548135dd27 input/dtiinit
```

## Output

The main output of this App is a file called `track.trk`. 


### Dependencies

This App only requires [singularity](https://www.sylabs.io/singularity/) to run. If you don't have singularity, you will need to install following dependencies.  

  - NIBABEL: https://github.com/nipy/nibabel

