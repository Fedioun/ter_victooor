import zipfile
import nibabel as nib
import time, os
import matplotlib.pyplot as plt
import numpy as np
import csv

def main():

	input_folder = os.path.join(".", "data", "MICCAI_BraTS_2018_Data_Training")

	data_type = "HGG"
	dataset_folder = os.path.join(input_folder, data_type)
	patients = os.listdir(dataset_folder)


	csv_path = os.path.join(input_folder, "survival_data.csv")


	patients_dict = get_metadata(os.path.join(input_folder, "survival_data.csv"))

	x1, y1 = load_patient(os.path.join(dataset_folder, patients[0]))

	x2, y2 = load_patient(os.path.join(dataset_folder, patients[1]))

	print( get_IoU(y1, y2, 1) )

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



def get_metadata(csv_path):
	patients_dict = {}

	with open(csv_path) as csv_file:
		lines = [line for line in csv.reader(csv_file, delimiter=',', quotechar='|')][1:]

		for line in lines:
			dt = {
				'Age' : line[1],
				'Survival' : line[2],
				'ResectionStatus' : line[3]
			}
			patients_dict[line[0]] = dt

	return patients_dict



def get_IoU(x, y, label):

	x = np.where(x == label, True, False)
	y = np.where(y == label, True, False)

	print(x.shape)

	print(x.sum())

	overlap = x * y  # Logical AND
	union = x + y    # Logical OR

	return overlap.sum()/float(union.sum())


def get_DSC(x, y, label):
	x = np.where(x == label, True, False)
	y = np.where(y == label, True, False)

	overlap = x * y

	return 2 * overlap.sum() / (x.sum() + y.sum())


def get_metrics(x, y, label):
	x = np.where(x == label, True, False)
	y = np.where(y == label, True, False)

	tp = x * y
	tn = np.logical_not(x) * np.logical_not(y)



	sensitivity = overlap.sum() / x.sum()
	specificity = 12











main()
