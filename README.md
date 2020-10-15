[![Abcdspec-compliant](https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg)](https://github.com/brain-life/abcd-spec)
[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-bl.app.132-blue.svg)](https://doi.org/10.25663/brainlife.app.132)
[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-bl.app.133-blue.svg)](https://doi.org/10.25663/brainlife.app.133)

# app-convert-tck-to-trk

This service will convert a .tck file to .trk file format using nibabel. 

### Authors
- Paolo Avesani (pavesani@iu.edu)

### Contributors
- Soichi Hayashi (hayashis@iu.edu)

### Project Director
- Franco Pestilli (franpest@indiana.edu)

### Funding Acknowledgment
brainlife.io is publicly funded and for the sustainability of the project it is helpful to Acknowledge the use of the platform. We kindly ask that you acknowledge the funding below in your publications and code reusing this code.

[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-ACI-1916518](https://img.shields.io/badge/NSF_ACI-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://grantome.com/grant/NIH/R01-EB029272-01)

### Citation
We kindly ask that you cite the following article when publishing papers and code using this code: 
1. Avesani, P., McPherson, B., Hayashi, S. et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. Sci Data 6, 69 (2019). [https://doi.org/10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

### Reference
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1464282.svg)](https://doi.org/10.5281/zenodo.1464282)

## Running the App 

### On Brainlife.io

You can submit this App online at [https://doi.org/10.25663/bl.app.132](https://doi.org/10.25663/bl.app.132) via the "Execute" tab.

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

