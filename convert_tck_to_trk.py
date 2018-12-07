#!/usr/bin/env python

import json
import nibabel as nib
from nibabel.streamlines import Field
from nibabel.orientations import aff2axcodes


def main():

        with open('config.json') as config_json:
                config = json.load(config_json)
    
	tck_file = config["tck"]
	anatomy_file = config["dwi"]
	trk_file = 'track.trk'

        nii = nib.load(anatomy_file)
        
        header = {}
	header[Field.VOXEL_TO_RASMM] = nii.affine.copy()
        header[Field.VOXEL_SIZES] = nii.header.get_zooms()[:3]
	header[Field.DIMENSIONS] = nii.shape[:3]
	header[Field.VOXEL_ORDER] = "".join(aff2axcodes(nii.affine))

	tck = nib.streamlines.load(tck_file)
        nib.streamlines.save(tck.tractogram, trk_file, header=header)

        
if __name__ == '__main__':
        main()
