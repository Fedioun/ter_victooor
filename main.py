import zipfile
import nibabel as nib
import time, os

def main():

	input_folder = os.path.join(".", "data", "MICCAI_BraTS_2018_Data_Training")

	subfolder = "HGG"

	stuff = os.listdir(os.path.join(input_folder, subfolder))


	for f in stuff:
		for k in os.listdir(os.path.join(input_folder, subfolder, f)):

			if k.endswith("nii.gz"):

				print(k)

				filename = os.path.join(input_folder, subfolder, f, k)

				img = nib.load(filename)
				img.shape


				time.sleep(1)


main()
