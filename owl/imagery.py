# methods used to manipulate the image data

# sobel kernel for edge detection
kernel_x = 3
kernel_y = 3
sobel_kernel = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]

# filters the given image using the specified mask
def sobel_filter(img, mask):

	# mask dimension, assert that uneven square matrix
	dim_mask_x = len(mask)
	dim_mask_y = len(mask[0])

	assert(dim_mask_x == dim_mask_y and dim_mask_x % 2 == 1)

	dim_mask = dim_mask_x

	# image dimension
	dim_x = len(img)
	dim_y = len(img[0])

	assert(dim_x > dim_mask_x and dim_y > dim_mask_y)

	# generate the new image from the mask

	output = []

	for x in range(dim_mask / 2, dim_x - dim_mask / 2):
		for y in range(dim_mask / 2, dim_y - dim_mask / 2):
			subimage = img[]
