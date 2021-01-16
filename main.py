import zipfile
import nibabel as nib
import time, os
import matplotlib.pyplot as plt
import numpy as np

def main():

	input_folder = os.path.join(".", "data", "MICCAI_BraTS_2018_Data_Training")

	data_type = "HGG"
	dataset_folder = os.path.join(input_folder, data_type)
	patients = os.listdir(dataset_folder)

	

	for p in patients:
		load_patient(os.path.join(dataset_folder, p))

	exit()


	print(img.shape)
	print(plt.imshow(img[:, :, 100]) ) 

	plt.show()

	time.sleep(3)


def load_patient(path):

	y = nib.load(os.path.join(path, os.path.basename(path) + "_seg.nii.gz")).get_fdata()


	channels = ["t1", "t1ce", "t2", "flair"]

	tmp = []

	for c in channels:

		tmp.append(
			nib.load(os.path.join(path, os.path.basename(path) + "_" + c + ".nii.gz")).get_fdata()
		)

	x = np.stack(tmp, axis=3)

	return x, y

def get_metadata(id, csv_path):
	pass





main()
