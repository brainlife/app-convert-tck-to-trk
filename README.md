<h1 align="center">Convert tck to trk</h1>

<p align="center">
  A TrackVis <code>.trk</code> tractogram from an MRtrix <code>.tck</code> tractogram, with the header taken from a T1-weighted or DWI reference image.
</p>

<p align="center">
  <a href="https://github.com/brainlife/abcd-spec"><img src="https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg" alt="ABCD Spec v1.1"></a>
  <a href="https://doi.org/10.25663/brainlife.app.133"><img src="https://img.shields.io/badge/Brainlife-brainlife.app.133-blue.svg" alt="Run on brainlife.io"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-lightgrey.svg" alt="MIT license"></a>
</p>

> 📍 **This branch, `1.0`, runs 2 brainlife.io Apps** that share the same code:
>
> - Convert tck to trk in T1 space ([doi:10.25663/brainlife.app.133](https://doi.org/10.25663/brainlife.app.133))
> - Convert tck to trk in DWI space ([doi:10.25663/brainlife.app.132](https://doi.org/10.25663/brainlife.app.132))
>
> The other Apps in this repository are listed under **Versions on brainlife.io** below.

## 🧠 At a glance

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

### 🧩 Convert tck to trk in T1 space

> **Converts an MRtrix .tck tractogram to TrackVis .trk format with nibabel, using a T1-weighted image as the reference space for the trk header; a format conversion utility.**

Loads the .tck streamlines with nibabel and saves them as track.trk with the voxel-to-RAS affine, voxel sizes, dimensions and voxel order taken from the T1-weighted NIfTI. Use it when a downstream tool needs .trk; the streamlines are not transformed, so the tractogram must already be in the space of the T1-weighted image.

| | |
|---|---|
| 📥 **Inputs** | `neuro/anat/t1w` · `neuro/track/tck` |
| 📤 **Outputs** | `neuro/track/trk` |
| 🐳 **Container** | `brainlife/dipy:0.13` |
| ⚙️ **Resources** | 8 CPUs · 0.17 h walltime |
| 🔗 **Run it** | [doi.org/10.25663/brainlife.app.133](https://doi.org/10.25663/brainlife.app.133) |

#### 📥 Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `t1` | `neuro/anat/t1w` | yes | T1-weighted NIfTI image that provides the reference space (affine, voxel size, dimensions) for the output trk header. The tck streamlines must already be in the space of this T1 image. |
| `tck` | `neuro/track/tck` | yes | A tractogram encoded according to the Mrtrix specifications. |

#### 📤 Outputs

| Output | Datatype | Description |
|---|---|---|
| `trk` | `neuro/track/trk` | The tractogram encoded following the TRK specifications. The reference space of streamlines is redefined according to the space of the T1 file given in input. |

### 🧩 Convert tck to trk in DWI space

> **Converts an MRtrix .tck tractogram to TrackVis .trk format with nibabel, using a DWI image as the reference space for the trk header; a format conversion utility.**

Loads the .tck streamlines with nibabel and saves them as track.trk with the voxel-to-RAS affine, voxel sizes, dimensions and voxel order taken from the DWI NIfTI. Use it when a downstream tool needs .trk; the streamlines are not transformed, so the tractogram must already be in the space of the DWI image.

| | |
|---|---|
| 📥 **Inputs** | `neuro/dwi` · `neuro/track/tck` |
| 📤 **Outputs** | `neuro/track/trk` |
| 🐳 **Container** | `brainlife/dipy:0.13` |
| ⚙️ **Resources** | 8 CPUs · 0.17 h walltime |
| 🔗 **Run it** | [doi.org/10.25663/brainlife.app.132](https://doi.org/10.25663/brainlife.app.132) |

#### 📥 Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `dwi` | `neuro/dwi` | yes | The DWI file will provide the reference space for the tractogram in output stored according to the TRK specifications. The tck streamlines must already be in the space of this DWI image. |
| `tck` | `neuro/track/tck` | yes | A tractogram encoded according to the Mrtrix specifications. |

#### 📤 Outputs

| Output | Datatype | Description |
|---|---|---|
| `trk` | `neuro/track/trk` | The tractogram encoded following the TRK specifications. The reference space of streamlines is redefined according to the space of the DWI file given in input. |

<!-- brainlife-app:end -->

## 🏷️ Versions on brainlife.io

Both Apps are built from the [`1.0`](https://github.com/brainlife/app-convert-tck-to-trk/tree/1.0) branch and run the same code; they differ only in the reference image you give them.

| App | Reference image | Branch | Run it | Status |
|---|---|---|---|---|
| **Convert tck to trk in T1 space** (this branch) | T1-weighted (`neuro/anat/t1w`) | [`1.0`](https://github.com/brainlife/app-convert-tck-to-trk/tree/1.0) | [doi:10.25663/brainlife.app.133](https://doi.org/10.25663/brainlife.app.133) | current |
| **Convert tck to trk in DWI space** (this branch) | DWI (`neuro/dwi`) | [`1.0`](https://github.com/brainlife/app-convert-tck-to-trk/tree/1.0) | [doi:10.25663/brainlife.app.132](https://doi.org/10.25663/brainlife.app.132) | current |

## 🔬 How it works

The App loads the `.tck` streamlines with [nibabel](https://nipy.org/nibabel/) and saves them as `track.trk`, with the voxel-to-RAS affine, voxel sizes, dimensions and voxel order of the trk header taken from the reference NIfTI image. The streamlines themselves are not transformed, so the tractogram must already be in the space of the reference image.

## 🚀 Running the App

### ☁️ On brainlife.io

Open the App at [doi.org/10.25663/brainlife.app.133](https://doi.org/10.25663/brainlife.app.133) (T1 space) or [doi.org/10.25663/brainlife.app.132](https://doi.org/10.25663/brainlife.app.132) (DWI space), choose a `neuro/track/tck` tractogram and the matching reference image from your project and press **Execute**. The converted tractogram is archived to your project as a `neuro/track/trk` dataset, tagged `t1` or `dwi` after the reference space.

### 💻 Locally

You need [Singularity/Apptainer](https://apptainer.org/). `main` runs the conversion inside the `brainlife/dipy:0.13` container. Without Singularity, install Python with nibabel and run `./convert_tck_to_trk.py` directly.

1. Clone this repository and check out the App's branch: `git checkout 1.0`.
2. Create `config.json` with the paths to your tractogram and reference image. The reference image always goes under the key `dwi`, whether it is a DWI or a T1-weighted image:

   ```json
   {
       "tck": "./input/track/track.tck",
       "dwi": "./input/dtiinit/dwi_aligned_trilin_noMEC.nii.gz"
   }
   ```

3. Run the App:

   ```bash
   ./main
   ```

### 🧪 Sample data

Download a sample tractogram and DWI from brainlife.io with the [brainlife CLI](https://github.com/brainlife/cli):

```bash
npm install -g brainlife
bl login
mkdir input
bl dataset download 5a0e604116e499548135de87 && mv 5a0e604116e499548135de87 input/track
bl dataset download 5a0dcb1216e499548135dd27 && mv 5a0dcb1216e499548135dd27 input/dtiinit
```

## 📦 Outputs

```text
trk/
└── track.trk    the tractogram in TrackVis format
```

## 🩺 Troubleshooting

- **`failed`**: `track.trk` was not written or is empty. Check that the `.tck` file is valid and that the reference image is a readable NIfTI.

## 📚 Citing

> [!TIP]
> If you use this App in your work, please cite the App, the software it builds on and brainlife.io (below). GitHub's **Cite this repository** button gives the App citation in APA and BibTeX.

- app-convert-tck-to-trk. Zenodo. [doi:10.5281/zenodo.1464282](https://doi.org/10.5281/zenodo.1464282)
- Convert tck to trk in T1 space. brainlife.io App. [doi:10.25663/brainlife.app.133](https://doi.org/10.25663/brainlife.app.133)
- Convert tck to trk in DWI space. brainlife.io App. [doi:10.25663/brainlife.app.132](https://doi.org/10.25663/brainlife.app.132)
- Avesani P, McPherson B, Hayashi S, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. Sci Data 6, 69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)
- Tournier et al. MRtrix3: A fast, flexible and open software framework for medical image processing and visualisation. *NeuroImage* 202:116137 (2019). [doi:10.1016/j.neuroimage.2019.116137](https://doi.org/10.1016/j.neuroimage.2019.116137)
- Garyfallidis et al. Dipy, a library for the analysis of diffusion MRI data. *Frontiers in Neuroinformatics* 8 (2014). [doi:10.3389/fninf.2014.00008](https://doi.org/10.3389/fninf.2014.00008)
- Hayashi S, Caron BA, Heinsfeld AS, et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. *Nature Methods* 21:809–813 (2024). [doi:10.1038/s41592-024-02237-2](https://doi.org/10.1038/s41592-024-02237-2)

## 👥 Authors

- Franco Pestilli (project director)
- Paolo Avesani

**Contributors:** Soichi Hayashi

## 💰 Funding

[![Wellcome-226486/Z/22/Z](https://img.shields.io/badge/Wellcome-226486%2FZ%2F22%2FZ-purple.svg)](https://wellcome.org/)
[![NIH-NINDS-U24NS140384](https://img.shields.io/badge/NIH_NINDS-U24NS140384-green.svg)](https://reporter.nih.gov/project-details/11261037)
[![NIH-NINDS-UM1NS132207](https://img.shields.io/badge/NIH_NINDS-UM1NS132207-green.svg)](https://reporter.nih.gov/project-details/11411328)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://reporter.nih.gov/project-details/10262925)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://reporter.nih.gov/project-details/10428625)
[![NIH-NIMH-R01MH126699](https://img.shields.io/badge/NIH_NIMH-R01MH126699-green.svg)](https://reporter.nih.gov/project-details/10460628)
[![NIH-NIDCD-R01DC020088](https://img.shields.io/badge/NIH_NIDCD-R01DC020088-green.svg)](https://reporter.nih.gov/project-details/11140284)
[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-2203524](https://img.shields.io/badge/NSF_BCS-2203524-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2203524)
[![NSF-IIS-1636893](https://img.shields.io/badge/NSF_IIS-1636893-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-OAC-2148729](https://img.shields.io/badge/NSF_OAC-2148729-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148729)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NSF-IIS-2148700](https://img.shields.io/badge/NSF_IIS-2148700-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148700)
[![NSF-OAC-1916518](https://img.shields.io/badge/NSF_OAC-1916518-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1916518)

<sub>brainlife.io is publicly funded, and acknowledging that support helps keep it running. This App was developed with support from Wellcome, the U.S. National Institutes of Health (including the BRAIN Initiative BRAIN CONNECTS program: The Axonal Projectome EXchange, U24NS140384, and the Center for Mesoscale Connectomics, UM1NS132207) and the U.S. National Science Foundation.</sub>

## ⚖️ License

[MIT](LICENSE). nibabel is distributed under its own [license](https://github.com/nipy/nibabel/blob/master/COPYING).
